# medico/urls.py
from django.urls import path
# Importe a TemplateView, que é a view genérica do Django para renderizar templates
from django.views.generic import TemplateView

urlpatterns = [
    # URL: /medicos/ -> Renderiza diretamente o template 'lista_medicos.html'
    path(
        'medicos/', 
        TemplateView.as_view(template_name='medico/lista_medicos.html'), 
        name='lista_medicos'
    ),

    # URL: /medicos/cadastrar/ -> Renderiza 'cadastro_medico.html'
    path(
        'medicos/cadastrar/', 
        TemplateView.as_view(template_name='medico/cadastro_medico.html'), 
        name='cadastrar_medico'
    ),

    # URL: /especialidades/ -> Renderiza 'lista_especialidades.html'
    path(
        'especialidades/', 
        TemplateView.as_view(template_name='medico/lista_especialidades.html'), 
        name='lista_especialidades'
    ),

    # URL: /especialidades/cadastrar/ -> Renderiza 'cadastro_especialidade.html'
    path(
        'especialidades/cadastrar/', 
        TemplateView.as_view(template_name='medico/cadastro_especialidade.html'), 
        name='cadastrar_especialidade'
    ),
]
