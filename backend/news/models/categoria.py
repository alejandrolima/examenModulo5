#!/usr/bin/env python3

from django.db import models


class Categoria(models.Model):

    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"

    estados = [
        (ACTIVO, "Activo"),
        (INACTIVO, "Inactivo"),
    ]

    sigla = models.CharField(
        verbose_name="Sigla",
        max_length=20,
        blank=True,
        null=True,
    )

    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=200,
        blank=True,
        null=True,
    )

    descripcion = models.CharField(
        verbose_name="Descripción",
        max_length=2000,
        blank=True,
        null=True,
    )

    color = models.CharField(
        verbose_name="Color",
        max_length=20,
        blank=True,
        null=True,
    )

    fecha_actualizacion = models.DateTimeField(
        verbose_name="Fecha de actualización",
        blank=True,
        null=True,
        auto_now=True,
    )

    usuario_actualizacion = models.ForeignKey(
        to="Usuario",
        verbose_name="Usuario de actualizacion",
        related_name="categorias",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    transaccion = models.CharField(
        verbose_name="Transacción",
        max_length=20,
        blank=True,
        null=True,
    )

    estado = models.CharField(
        verbose_name="Estado",
        choices=estados,
        default=ACTIVO,
        max_length=20,
        blank=True,
        null=True,
        help_text='Marque "Activo" para habilitar esta categoría en el menú, "Inactivo" para ocultarla.'
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
