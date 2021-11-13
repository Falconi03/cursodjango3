from django.contrib import admin
from .models import Cadastro

class CadastroAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'confirm_password')



admin.site.register(Cadastro, CadastroAdmin)
# Register your models here.
