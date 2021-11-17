from django.shortcuts import render
from django.http import HttpResponse
from .models import Cadastro
from validate_email import validate_email
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import CadastroSerializer
import requests
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from time import sleep
from rest_framework.permissions import IsAuthenticated


class CadastroViewset(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email', 'password']


def home(request):
    return render(request, 'index.html')


def req(request):
    email = request.GET['email']
    if email == '':
        verificacao = 'o email incorretos'
        return render(request, 'index.html', {'verificacao': verificacao})
    else:
        api = (f"http://localhost:8000/api/cadastro/?email={email}")
        requisicao = requests.get(api)
        try:
            lista = requisicao.json()
        except:
            print("A resposta não chegou com o formato esperado.")
        if len(lista)==0:
            verificacao = 'conta não encontrada'
            return render(request, 'index.html', {'verificacao': verificacao})
        else:
            biblioteca = {}
            for k ,v in lista[0].items():
                if k == 'name' or k == 'email':
                    biblioteca[k] = v
            teste = {
                "cadastros":biblioteca
            }
            return render(request, "req.html", teste)    
    
    
def login(request):
    email = request.GET['email']
    password = request.GET['password']
    if email == '' or password == '':
        verificacao = 'o password ou email incorretos'
        return render(request, 'index.html', {'verificacao': verificacao})
    else:
        api = (f"http://localhost:8000/api/cadastro/?email={email}")
        requisicao = requests.get(api)
        try:
            lista = requisicao.json()
        except ValueError:
            print("A resposta não chegou com o formato esperado.")
        if len(lista)==0:
            verificacao = 'conta não encontrada'
            return render(request, 'index.html', {'verificacao': verificacao})
        else:
            for i,v in lista[0].items():
                if i == 'password':
                    if v != password:
                        verificacao = 'o password ou email incorretos'
                        return render(request, 'index.html', {'verificacao': verificacao})
                    else:    
                        return render(request, 'login.html')


def cadastro(request):
    verificacao = ''
    name = request.POST['name']
    email = request.POST['email']
    is_valid = validate_email(email)
    api = (f"http://localhost:8000/api/cadastro/?email={email}")
    requisicao = requests.get(api)
    try:
        lista = requisicao.json()
    except:
        print("A resposta não chegou com o formato esperado.")
    if len(lista)==1:
            verificacao = 'já existe uma conta com esse email'
            return render(request, 'index.html', {'verificacao': verificacao})
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
