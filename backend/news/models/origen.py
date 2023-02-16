#!/usr/bin/env python3

from django.db import models


class Origen(models.Model):

    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=100,
        blank=False,
        null=True,
    )

    descripcion = models.CharField(
        verbose_name="Descripción",
        max_length=1000,
        blank=True,
        null=True,
    )

    sigla = models.CharField(
        verbose_name="Sigla",
        max_length=20,
        blank=True,
        null=True,
    )

    fecha_creacion = models.DateTimeField(
        verbose_name="Fecha creación",
        blank=True,
        null=True,
        auto_now_add=True,
    )

    usuario_creacion = models.ForeignKey(
        to="Usuario",
        verbose_name="Usuario creación",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    estado = models.CharField(
        verbose_name="Estado",
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nombre
