from django.contrib import admin

# Importar as classes
from .models import Servidor, Status, Situacao, Classe

# Register your models here.

admin.site.register(Servidor)
admin.site.register(Status)
admin.site.register(Situacao)
admin.site.register(Classe)

