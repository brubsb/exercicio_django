# medico/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicos, Especialidade
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EspecialidadeForm, MedicosForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from django.http import HttpResponse

def lista_especialidades(request):
    #Busca e exibe todas as especialidades cadastradas.
    contexto = {'especialidades': Especialidade.objects.all()}
    return render(request, 'medicos/lista_especialidades.html', context=contexto)

def lista_medicos(request):
    #Busca e exibe todos os médicos cadastrados.
    contexto = {'medicos': Medicos.objects.all()}
    return render(request, 'medicos/lista_medicos.html', context=contexto)

def cadastro_especialidade(request):
    #Exibe o formulário (GET) e salva os dados (POST).
    if request.method == 'POST':
        nome_digitado = request.POST.get('nome_especialidade')
        if nome_digitado:
            Especialidade.objects.create(nome_especialidade=nome_digitado)
        return redirect('lista_especialidades')
    
    return render(request, 'medicos/cadastro_especialidade.html')

def cadastro_medico(request):
    #Exibe o formulário com as especialidades (GET) e salva os dados (POST).
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        ids_especialidades = request.POST.getlist('especialidades')

        novo_medico = Medicos.objects.create(nome=nome, sobrenome=sobrenome, email=email)
        novo_medico.nome_especialidade.set(ids_especialidades)
        
        return redirect('lista_medicos')

    contexto = {'especialidades': Especialidade.objects.all()}
    return render(request, 'medico/cadastro_medico.html', context=contexto)

def deletar_especialidade(request, id_especialidade):
    #Encontra uma especialidade pelo seu ID e a deleta.
    # Busca a especialidade específica que queremos deletar
    especialidade_para_deletar = Especialidade.objects.get(id=id_especialidade)
    # Deleta o objeto do banco de dados
    especialidade_para_deletar.delete()
    # Redireciona de volta para a lista de especialidades
    return redirect('lista_especialidades')

def deletar_medico(request, id_medico):
    #Encontra um médico pelo seu ID e o deleta.
    # Busca o médico específico
    medicos_para_deletar = Medicos.objects.get(id=id_medico)
    # Deleta o objeto
    medicos_para_deletar.delete()
    # Redireciona de volta para a lista de médicos
    return redirect('lista_medicos')

def editar_especialidade(request, id_especialidade):
    #Busca uma especialidade existente para edição (GET) e salva as alterações (POST).
    # 1. Busca no banco a instância específica da especialidade que queremos editar.
    especialidade_para_editar = Especialidade.objects.get(id=id_especialidade)

    # 2. Se o formulário for enviado (POST), salva as alterações.
    if request.method == 'POST':
        novo_nome = request.POST.get('nome_especialidade')
        if novo_nome:
            # Atualiza o campo 'nome_especialidade' com o novo valor.
            especialidade_para_editar.nome_especialidade = novo_nome
            # Salva a alteração no banco de dados.
            especialidade_para_editar.save()
        return redirect('lista_especialidades')

    # 3. Se for um acesso normal (GET), mostra o formulário preenchido com os dados existentes.
    contexto = {'especialidade': especialidade_para_editar}
    return render(request, 'medicos/editar_especialidade.html', context=contexto)


def editar_medico(request, id_medico):
    #Busca um médico existente para edição (GET) e salva as alterações (POST).
    # 1. Busca a instância específica do médico.
    medicos_para_editar = Medicos.objects.get(id=id_medico)

    # 2. Se o formulário for enviado (POST), salva as alterações.
    if request.method == 'POST':
        # Pega os novos dados do formulário.
        medicos_para_editar.nome = request.POST.get('nome')
        medicos_para_editar.sobrenome = request.POST.get('sobrenome')
        medicos_para_editar.email = request.POST.get('email')
        ids_especialidades = request.POST.getlist('especialidades')
        
        # Salva as alterações dos campos simples.
        medicos_para_editar.save()
        # Atualiza o relacionamento ManyToMany.
        medicos_para_editar.nome_especialidade.set(ids_especialidades)
        
        return redirect('lista_medicos')

    # 3. Se for um acesso normal (GET), prepara os dados para o template.
    contexto = {
        'medico': medicos_para_editar,
        'especialidades': Especialidade.objects.all() # Envia todas para preencher o select.
    }
    return render(request, 'medicos/editar_medico.html', context=contexto)


class EspecialidadeListView(LoginRequiredMixin, ListView):
    model = Especialidade
    template_name = 'especialidade_list.html'
   

class EspecialidadeCreateView(LoginRequiredMixin, CreateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'especialidade_form.html'
    success_url = reverse_lazy('especialidade_list')


class EspecialidadeUpdateView(LoginRequiredMixin,UpdateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'especialidade_form.html'
    success_url = reverse_lazy('especialidade_list')


class EspecialidadeDeleteView(LoginRequiredMixin, DeleteView):
    model = Especialidade
    template_name = 'especialidade_confirm_delete.html'
    success_url = reverse_lazy('especialidade_list')


class MedicosListView(LoginRequiredMixin, ListView):
    model = Medicos
    template_name = 'medico_list.html'
   

class MedicosCreateView(LoginRequiredMixin, CreateView):
    model = Medicos
    form_class = MedicosForm
    template_name = 'medicos_form.html'
    success_url = reverse_lazy('medico_list')


class MedicosUpdateView(LoginRequiredMixin, UpdateView):
    model = Medicos
    form_class = MedicosForm
    template_name = 'medicos_form.html'
    success_url = reverse_lazy('medico_list')


class MedicosDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicos
    template_name = 'medicos_confirm_delete.html'
    success_url = reverse_lazy('medico_list')


def home(request):
    return render(request, 'medicos/home.html')