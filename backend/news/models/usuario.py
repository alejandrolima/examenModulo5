#!/usr/bin/env python3

from django.db import models
from news.models import Persona
from django.contrib.auth.models import User


class Usuario(User):

    persona = models.ForeignKey(
        to="Persona",
        verbose_name="Persona",
        related_name="usuarios",
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
