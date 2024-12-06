from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    altura = models.FloatField(help_text="Altura em cm")
    peso = models.FloatField(help_text="Peso em kg")
    imc = models.FloatField(null=True, blank=True, help_text="Índice de Massa Corporal")

    def __str__(self):
        return self.nome
