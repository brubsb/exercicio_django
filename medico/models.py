from django.db import models

# Create your models here.
class Especialidade(models.Model):
    nome_especialidade = models.CharField(max_length=60)

    def __str__(self):
        return self.nome_especialidade
    
class Medico(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    nome_especialidade = models.ManyToManyField(Especialidade)

    def __str__(self):
        return self.nome