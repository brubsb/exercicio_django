from django.urls import path
from .views import (EspecialidadeListView, EspecialidadeCreateView, EspecialidadeUpdateView,
                    EspecialidadeDeleteView, MedicosListView, MedicosCreateView, MedicosUpdateView,
                    MedicosDeleteView)

urlpatterns = [
    path('especialidades/', EspecialidadeListView.as_view(), name='lista_especialidades'),
    path('especialidades/create/', EspecialidadeCreateView.as_view(), name='cadastrar_especialidade'),
    path('especialidades/<int:pk>/update/', EspecialidadeUpdateView.as_view(), name='cadastrar_especialidade'),
    path('especialidades/<int:pk>/delete/', EspecialidadeDeleteView.as_view(), name='editar_especialidade'),

    path('medicos/', MedicosListView.as_view(), name='lista_medicos'),
    path('medicos/create/', MedicosCreateView.as_view(), name='cadastro_medico'),
    path('medicos/<int:pk>/update/', MedicosUpdateView.as_view(), name='cadastro_medico'),
    path('medicos/<int:pk>/delete/', MedicosDeleteView.as_view(), name='editar_medico'),
]