#!/usr/bin/env python3

from django.db import models


class Formato(models.Model):

    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=100,
        blank=False,
        null=True,
    )

    sigla = models.CharField(
        verbose_name="Sigla",
        max_length=20,
        blank=False,
        null=True,
    )

    descripcion = models.CharField(
        verbose_name="Descripción",
        max_length=1000,
        blank=True,
        null=True,
    )

    fecha_actualizacion = models.DateTimeField(
        verbose_name="Fecha actualización",
        blank=True,
        null=True,
        auto_now=True,
    )

    usuario_actualizacion = models.ForeignKey(
        to="Usuario",
        verbose_name="Usuario actualización",
        related_name="formatos",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    transaccion = models.CharField(
        verbose_name="Transacción",
        max_length=100,
        blank=True,
        null=True,
    )

    estado = models.CharField(
        verbose_name="Estado",
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nombre
