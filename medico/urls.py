# medico/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ==================================================
    # ROTAS PARA MÉDICOS
    # ==================================================
    
    # Rota para a página que lista todos os médicos (Read)
    # Ex: http://127.0.0.1:8000/medicos/
    path('medicos/', views.lista_medicos, name='lista_medicos' ),
    
    # Rota para a página com o formulário de cadastro de um novo médico (Create)
    # Ex: http://127.0.0.1:8000/medicos/cadastrar/
    path('medicos/cadastrar/', views.cadastro_medico, name='cadastrar_medico' ),
    
    # Rota para a página de EDIÇÃO de um médico específico (Update)
    # Ex: http://127.0.0.1:8000/medicos/editar/5/
    path('medicos/editar/<int:id_medico>/', views.editar_medico, name='editar_medico' ),
    
    # Rota para DELETAR um médico específico pelo seu ID (Delete)
    # Ex: http://127.0.0.1:8000/medicos/deletar/5/
    path('medicos/deletar/<int:id_medico>/', views.deletar_medico, name='deletar_medico' ),

    # ==================================================
    # ROTAS PARA ESPECIALIDADES
    # ==================================================
    
    # Rota para a página que lista todas as especialidades (Read)
    # Ex: http://127.0.0.1:8000/especialidades/
    path('especialidades/', views.lista_especialidades, name='lista_especialidades' ),
    
    # Rota para a página com o formulário de cadastro de uma nova especialidade (Create)
    # Ex: http://127.0.0.1:8000/especialidades/cadastrar/
    path('especialidades/cadastrar/', views.cadastro_especialidade, name='cadastrar_especialidade' ),

    # Rota para a página de EDIÇÃO de uma especialidade específica (Update)
    # Ex: http://127.0.0.1:8000/especialidades/editar/3/
    path('especialidades/editar/<int:id_especialidade>/', views.editar_especialidade, name='editar_especialidade' ),

    # Rota para DELETAR uma especialidade específica pelo seu ID (Delete)
    # Ex: http://127.0.0.1:8000/especialidades/deletar/3/
    path('especialidades/deletar/<int:id_especialidade>/', views.deletar_especialidade, name='deletar_especialidade' ),
]
