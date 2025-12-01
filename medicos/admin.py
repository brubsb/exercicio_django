from django.contrib import admin

# Register your models here.
from .models import Medicos, Especialidade
admin.site.register(Medicos)
admin.site.register(Especialidade)