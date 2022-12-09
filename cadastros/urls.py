from django.urls import path

# Importa as views que a gente criou
from .views import StatusCreate, SituacaoCreate, ClasseCreate
from .views import ServidorUpdate, StatusUpdate, SituacaoUpdate, ClasseUpdate
from .views import StatusDelete, SituacaoDelete, ClasseDelete
from .views import  StatusList, SituacaoList, ClasseList, FrequenciaList, LancarFreqList

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [

    path('cadastrar/status/', StatusCreate.as_view(), name="cadastrar-status"),
    path('cadastrar/situacao/', SituacaoCreate.as_view(), name="cadastrar-situacao"),
    path('cadastrar/classe/', ClasseCreate.as_view(), name="cadastrar-classe"),




    path('editar/status/<int:pk>/', StatusUpdate.as_view(), name="editar-status"),
    path('editar/situacao/<int:pk>/', SituacaoUpdate.as_view(), name="editar-situacao"),
    path('editar/classe/<int:pk>/', ClasseUpdate.as_view(), name="editar-classe"),



    path('excluir/status/<int:pk>/', StatusDelete.as_view(), name="excluir-status"),
    path('excluir/situacao/<int:pk>/', SituacaoDelete.as_view(), name="excluir-situacao"),
    path('excluir/classe/<int:pk>/', ClasseDelete.as_view(), name="excluir-classe"),



    path('listar/status/', StatusList.as_view(), name="listar-status"),
    path('listar/situacoes/', SituacaoList.as_view(), name="listar-situacao"),
    path('listar/classes/', ClasseList.as_view(), name="listar-classe"),
    path('listar/frequencia/', FrequenciaList.as_view(), name="listar-frequencia"),
    path('listar/lancar_freq_6a/', LancarFreqList.as_view(), name="listar-lancar_freq_6a"),


]
