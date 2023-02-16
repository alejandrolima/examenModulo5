#!/usr/bin/env python3

from django.db import models


class Lugar(models.Model):

    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=100,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.nombre
