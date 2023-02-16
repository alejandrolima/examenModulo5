#!/usr/bin/env python3

from django.db import models


class Perfil(models.Model):

    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=100,
        blank=False,
        null=True,
    )

    sigla = models.CharField(
        verbose_name="Sigla",
        max_length=20,
        blank=True,
        null=True,
    )

    descripcion = models.CharField(
        verbose_name="Descripción",
        max_length=1000,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nombre
