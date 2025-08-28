from django.contrib import admin

# Register your models here.
from .models import Medico, Especialidade
admin.site.register(Medico)
admin.site.register(Especialidade)