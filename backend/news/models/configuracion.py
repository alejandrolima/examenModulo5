#!/usr/bin/env python3

from django.db import models


class Configuracion(models.Model):

    nombre = models.CharField(
        verbose_name="Nombre de sección",
        max_length=100,
        blank=False,
        null=False,
    )

    limite = models.IntegerField(
        verbose_name="Límite de noticias a mostrar",
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.nombre
