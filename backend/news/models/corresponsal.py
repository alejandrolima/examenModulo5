#!/usr/bin/env python3

from django.db import models


class Corresponsal(models.Model):

    persona = models.OneToOneField(
        to="Persona",
        verbose_name="Persona",
        blank=False,
        null=True,
        on_delete=models.SET_NULL
    )

    cargo = models.CharField(
        verbose_name="Cargo",
        max_length=100,
        blank=True,
        null=True,
    )

    foto = models.ImageField(
        verbose_name="Foto",
        blank=True,
        null=True,
    )

    web = models.CharField(
        verbose_name="Web",
        max_length=100,
        blank=True,
        null=True,
    )

    twitter = models.CharField(
        verbose_name="Twitter",
        max_length=100,
        blank=True,
        null=True,
    )

    linkedin = models.CharField(
        verbose_name="Linkedin",
        max_length=100,
        blank=True,
        null=True,
    )

    email = models.CharField(
        verbose_name="Email",
        max_length=100,
        blank=True,
        null=True,
    )

    telefono = models.CharField(
        verbose_name="Teléfono",
        max_length=100,
        blank=True,
        null=True,
    )

    biografia = models.TextField(
        verbose_name="Biografía",
        max_length=2000,
        blank=True,
        null=True,
    )

    entidad = models.CharField(
        verbose_name="Entidad",
        max_length=100,
        blank=True,
        null=True,
    )

    perfil = models.ForeignKey(
        to="Perfil",
        verbose_name="Tipo",
        related_name="corresponsales",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    fecha_inicio = models.DateTimeField(
        verbose_name="Fecha inicio",
        blank=True,
        null=True,
    )

    fecha_fin = models.DateTimeField(
        verbose_name="Fecha fin",
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
        related_name="corresponsales",
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

    @property
    def nombre_completo(self):
        return self.persona.nombre_completo

    @property
    def ultima_entrada(self):
        if len(self.entradas.all()) > 0:
            return self.entradas.all().order_by('-fecha')[0]
        else:
            return None

    def __str__(self):
        return self.persona.nombre_completo
