from django.urls import path
from .views import home, cadastro, login, req

urlpatterns = [
    path('home/', home),
    path('req/', req, name = 'req'),
    path('cadastro/', cadastro, name = 'cadastro'),
    path('login/', login, name = 'login')
]