from django.urls import path
from .views import (
    IndexTemplateView,
    FuncionarioCreateView,
    FuncionarioListView,
    FuncionarioUpdateView,
    FuncionarioDeleteView
)

app_name = 'website'

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("funcionarios/novo/", FuncionarioCreateView.as_view(), name="cadastro_funcionario"),
    path(
        "funcionarios/",
        FuncionarioListView.as_view(),
        name="lista_funcionarios"
    ),
    path(
        "funcionarios/<int:pk>/atualizar/",
        FuncionarioUpdateView.as_view(),
        name="atualiza_funcionario"
    ),
    path(
        "funcionario/excluir/<int:pk>/",
        FuncionarioDeleteView.as_view(),
        name="deleta_funcionario",
    ),

]
