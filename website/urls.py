from django.urls import path
from .views import home, cadastro, login, req
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('home/', home),
    path('req/', req, name = 'req'),
    path('cadastro/', cadastro, name = 'cadastro'),
    path('login/', login, name = 'login'),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view())
]