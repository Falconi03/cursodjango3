from django.shortcuts import render


def hello_blog(request):
    lista = [
        'Django','Python', 'Git', 'Html',
        'Banco de dados', 'Linux', 'Nginx', 'Uwsgi',
        'Sistemctl'
        ]
    data = {'name': 'Curso de django 3','lista_tecnologias': lista}
    return render(request, 'index.html', data)
