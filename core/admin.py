from django.contrib import admin
from medicos.models import *
from accounts.models import *
# Register your models here.

admin.site.register(Medicos)
admin.site.register(Especialidade)
admin.site.register(UserProfile)