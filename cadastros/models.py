from django.db import models
from django.contrib.auth.models import User

# Métodos e Choices


def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)


# Classes (modelos)



class Servidor(models.Model):
    nome_completo = models.CharField(max_length=100)
    siape = models.CharField(max_length=10)
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="usuário")


class Status(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="descrição")

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)


class Situacao(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    detalhes = models.CharField(max_length=255, blank=True, null=True)


class Classe(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="descrição", null=True, blank=True)
