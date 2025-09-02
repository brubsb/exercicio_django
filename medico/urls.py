# medico/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.lista_medicos, name='lista_medicos' ),
    path('medicos/cadastrar/', views.cadastro_medico, name='cadastrar_medico' ),
    path('medicos/editar/<int:id_medico>/', views.editar_medico, name='editar_medico' ),
    path('medicos/deletar/<int:id_medico>/', views.deletar_medico, name='deletar_medico' ),
    path('especialidades/', views.lista_especialidades, name='lista_especialidades' ),
    path('especialidades/cadastrar/', views.cadastro_especialidade, name='cadastrar_especialidade' ),
    path('especialidades/editar/<int:id_especialidade>/', views.editar_especialidade, name='editar_especialidade' ),
    path('especialidades/deletar/<int:id_especialidade>/', views.deletar_especialidade, name='deletar_especialidade' ),
]
