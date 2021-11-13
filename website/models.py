from django.db import models

class Cadastro(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10)

def __srt__(self):
    return self.name