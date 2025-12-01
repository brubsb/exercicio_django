from django import forms
from .models import Especialidade, Medicos

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nome_especialidade']

class MedicosForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ['nome','sobrenome', 'email', 'nome_especialidade']