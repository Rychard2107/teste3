from django.db import models


class Caso_Model(models.Model):
    nome_do_oficial = models.CharField(max_length=50)
    sexo_do_oficial = models.CharField(max_length=10)
    cpf_do_oficial = models.IntegerField
    patente = models.CharField(max_length=100)
    unidade = models.CharField(max_length=50)
    numero_tj = models.IntegerField
    descricao_do_caso = models.TextField(max_length=255)


'''''
CAMPOS:
nome_do_oficial
sexo_do_oficial
cpf_do_oficial
patente
unidade
numero_tj
descricao_do_caso
'''''