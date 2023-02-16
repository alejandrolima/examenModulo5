#!/usr/bin/env python3

from django.db import models
from functools import reduce


class Multimedia(models.Model):

    titulo = models.CharField(
        verbose_name="Título",
        max_length=610,
        blank=False,
        null=True,
    )

    imagen = models.ImageField(
        verbose_name="Imagen",
        blank=True,
        null=True,
    )

    pie = models.CharField(
        verbose_name="Pie",
        max_length=1000,
        blank=True,
        null=True,
    )

    fecha = models.DateTimeField(
        verbose_name="Fecha",
        blank=True,
        null=True,
    )

    lugar = models.ForeignKey(
        to="Lugar",
        verbose_name="Lugar",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    enlace = models.CharField(
        verbose_name="Enlace",
        max_length=100,
        blank=True,
        null=True,
    )

    ruta = models.CharField(
        verbose_name="Ruta",
        max_length=100,
        blank=True,
        null=True,
    )

    autor = models.ForeignKey(
        to="Persona",
        verbose_name="Autor",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
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

    visitas = models.IntegerField(
        verbose_name="Visitas",
        blank=True,
        null=True,
        default=0
    )

    etiqueta = models.ManyToManyField(
        to="Etiqueta",
        verbose_name="Etiqueta",
        related_name="multimedia",
        blank=True,
    )

    descargas = models.IntegerField(
        verbose_name="Descargas",
        blank=True,
        null=True,
        default=0
    )

    def __str__(self):
        return self.titulo

    @property
    def descargas(self):
        return reduce(lambda x, y: x+y, [i.descargas for i in self.imagenes.all()], 0)
