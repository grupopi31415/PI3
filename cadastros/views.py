from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Servidor, Status, Situacao, Classe

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

# Create your views here.





class StatusCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')


class SituacaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Situacao
    fields = ['status', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-situacao')


class ClasseCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classe')









class ServidorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Servidor
    fields = ['nome_completo', 'siape', 'cpf', 'campus']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class StatusUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')


class SituacaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Situacao
    fields = ['status', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-situacao')


class ClasseUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classe')





class StatusDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Status
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-status')


class SituacaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Situacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-situacao')


class ClasseDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-classe')















################# LISTA #################




class StatusList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Status
    template_name = 'cadastros/listas/status.html'


class SituacaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Situacao
    template_name = 'cadastros/listas/situacao.html'


class ClasseList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/listas/classe.html'

class FrequenciaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/listas/frequencia.html'

class LancarFreqList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/listas/lancar_freq_6a.html'

