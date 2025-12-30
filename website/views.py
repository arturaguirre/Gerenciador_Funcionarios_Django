from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Funcionario
from .forms import InsereFuncionarioForm


class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = InsereFuncionarioForm
    template_name = "website/cadastro-funcionario.html"
    success_url = reverse_lazy("website:lista_funcionarios")


class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "website/lista.html"
    context_object_name = "funcionarios"


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = InsereFuncionarioForm
    template_name = "website/atualiza.html"
    success_url = reverse_lazy("website:lista_funcionarios")
class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "website/exclui.html"
    success_url = reverse_lazy("website:lista_funcionarios")
    context_object_name = "funcionario"