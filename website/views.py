from django.shortcuts import render
from django.http import HttpResponse
from .models import Cadastro
from validate_email import validate_email
from rest_framework import viewsets
from .serializer import CadastroSerializer
import requests



def home(request):
    return render(request, 'index.html')

def req(request):
    api = "http://localhost:8000/api/cadastro/"
    requisicao = requests.get(api)
    try:
        lista = requisicao.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    biblioteca = {
        "cadastros": dicionario
    }
    return render(request, "req.html", biblioteca)


class CadastroViewset(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer    


def login(request):
    email = request.GET['email']
    password = request.GET['password']
    cadastro = Cadastro.objects.filter(email = email)
    if len(cadastro) == 0:
        verificacao = 'email incorreto'
        return render(request, 'index.html', {'verificacao': verificacao})
    else:
        for item in cadastro:
            if item.password != password:
                verificacao = 'o password ou email incorretos'
                return render(request, 'index.html', {'verificacao': verificacao})
            else:
                return render(request, 'login.html')

def cadastro(request):
    verificacao = ''
    name = request.POST['name']
    email = request.POST['email']
    is_valid = validate_email(email)
    if is_valid:
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            verificacao = 'o password não esta igual ao confirm password'
            return render(request, 'index.html', {'verificacao': verificacao})
        else:
            Cadastro.objects.create(
                name = name,
                email = email,
                password = password,
                confirm_password = confirm_password
            )
            return render(request, 'cadastro.html')
    else:
        verificacao = 'email incorreto'
        return render(request, 'index.html', {'verificacao': verificacao})
