#!/usr/bin/env python3

from django.db import models
from PIL import Image
from os.path import join, dirname
from django.conf import settings


class Imagen(models.Model):

    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=100,
        blank=False,
        null=True,
    )

    imagen = models.ImageField(
        verbose_name="Imagen",
        blank=True,
        null=True,
    )

    multimedia = models.ForeignKey(
        to="Multimedia",
        verbose_name="Multimedia",
        related_name="imagenes",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    descargas = models.IntegerField(
        verbose_name="Descargas",
        blank=True,
        null=True,
        default=0
    )

    def __str__(self):
        return self.nombre if self.nombre is not None else self.imagen.url

    @property
    def get_fullpath(self):
        filename = self.imagen.path.split("/")[-1]
        return join(settings.MEDIA_ROOT, "full", filename)

    @property
    def imagen_full(self):
        filename = self.imagen.path.split("/")[-1]
        return join("/media", "full", filename)

    def save(self):

        if not self.id and not self.imagen:
            return

        if self.id is None:
            image = Image.open(self.imagen)
        else:
            try:
                image = Image.open(self.get_fullpath)
            except Exception:
                image = Image.open(self.imagen)

        super(Imagen, self).save()

        (width, height) = image.size

        new_width = 600
        new_height = height * new_width / width

        size = (int(new_width), int(new_height))
        image_resized = image.resize(size, Image.ANTIALIAS)

        image.save(self.get_fullpath)
        image_resized.save(self.imagen.path)

