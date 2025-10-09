from django import forms
from .models import Especialidade, Medico

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nome_especialidade']

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome','sobrenome', 'email', 'nome_especialidade']