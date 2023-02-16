#!/usr/bin/env python3

from django.db import models


class Persona(models.Model):

    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=100,
        blank=False,
        null=False,
    )

    primer_apellido = models.CharField(
        verbose_name="Primer apellido",
        max_length=100,
        blank=True,
        null=True,
    )

    segundo_apellido = models.CharField(
        verbose_name="Segundo apellido",
        max_length=100,
        blank=True,
        null=True,
    )

    alias = models.CharField(
        verbose_name="Alias",
        max_length=30,
        blank=True,
        null=True,
    )

    iniciales = models.CharField(
        verbose_name="Iniciales",
        max_length=20,
        blank=True,
        null=True,
    )

    @property
    def nombre_completo(self):
        return " ".join([
            self.nombre if self.nombre is not None else "",
            self.primer_apellido if self.primer_apellido is not None else "",
            self.segundo_apellido if self.segundo_apellido is not None else ""])

    def __str__(self):
        return self.nombre_completo
