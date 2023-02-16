#!/usr/bin/env python3

from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone


class Entrada(models.Model):

    NUEVA = "NUEVA"
    BORRADOR = "BORRADOR"
    PUBLICADO = "PUBLICADO"
    ELIMINADO = "ELIMINADO"
    EDITADO = "EDITADO"

    estados = [
        (NUEVA, "Nueva"),
        (BORRADOR, "Borrador"),
        (PUBLICADO, "Publicado"),
        (ELIMINADO, "Eliminado"),
        (EDITADO, "Editado"),
    ]

    PRIMARIO = "PRIMARIO"
    SECUNDARIO = "SECUNDARIO"
    TERCIARIO = "TERCIARIO"
    ESPECIAL = "ESPECIAL"

    niveles = [
        (PRIMARIO, "Primario"),
        (SECUNDARIO, "Secundario"),
        (TERCIARIO, "Terciario"),
        (ESPECIAL, "Especial"),
    ]

    NOMBRE_ORIGEN = "NOMBRE_ORIGEN"
    INICIAL_ORIGEN = "INICIAL_ORIGEN"
    ORIGEN = "ORIGEN"

    firmas = [
        (NOMBRE_ORIGEN, "Nombre Apellido / Origen"),
        (INICIAL_ORIGEN, "INICIALES / Origen"),
        (ORIGEN, "Origen"),
    ]
   
    titulo = models.CharField(
        verbose_name="Título",
        max_length=200,
        blank=False,
        null=True,
    )

    imagen = models.ImageField(
        verbose_name="Imagen",
        blank=True,
        null=True,
    )

    lead = models.TextField(
        verbose_name="Lead",
        max_length=1000,
        blank=True,
        null=True,
    )

    cuerpo = HTMLField(
        verbose_name="Cuerpo",
        max_length=20000,
        blank=True,
        null=True,
    )

    enlace = models.CharField(
        verbose_name="Enlace",
        max_length=200,
        blank=True,
        null=True,
    )

    dependencia = models.IntegerField(
        verbose_name="Dependencia",
        blank=True,
        null=True,
    )

    corresponsal = models.ForeignKey(
        to="Corresponsal",
        verbose_name="Corresponsal",
        related_name="entradas",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    formato_firma = models.CharField(
        verbose_name="Formato de firma",
        max_length=20,
        choices=firmas,
        default=ORIGEN,
        blank=False,
        null=True,
    )

    publicado = models.BooleanField(
        verbose_name="Publicado",
        default=True
    )

    origen = models.ForeignKey(
        to="Origen",
        verbose_name="Origen",
        related_name="entradas",
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

    lugar = models.ForeignKey(
        to="Lugar",
        verbose_name="Lugar",
        related_name="entradas",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    etiqueta = models.ManyToManyField(
        to="Etiqueta",
        verbose_name="Etiqueta",
        related_name="entradas",
        blank=True,
    )

    fecha = models.DateTimeField(
        verbose_name="Fecha",
        blank=True,
        null=True,
        default=timezone.now
    )

    fecha_creacion = models.DateTimeField(
        verbose_name="Fecha de creación",
        blank=True,
        null=True,
        auto_now_add=True,
    )

    fecha_modificacion = models.DateTimeField(
        verbose_name="Fecha de modificación",
        blank=True,
        null=True,
        auto_now=True,
    )

    usuario_creacion = models.ForeignKey(
        to="Usuario",
        verbose_name="Usuario creación",
        related_name="entradas_creadas",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    usuario_modificacion = models.ForeignKey(
        to="Usuario",
        verbose_name="Usuario modificación",
        related_name="entradas_modificadas",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    estado = models.CharField(
        verbose_name="Estado",
        max_length=200,
        choices=estados,
        default=NUEVA,
        blank=True,
        null=True,
    )

    formato = models.ForeignKey(
        to="Formato",
        verbose_name="Formato",
        related_name="entradas",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    categoria = models.ManyToManyField(
        to="Categoria",
        verbose_name="Categoría",
        blank=True,
        # null=True,
    )

    multimedia = models.ManyToManyField(
        to="Multimedia",
        verbose_name="Multimedia",
        blank=True,
        # null=True,
    )

    nivel = models.CharField(
        verbose_name="Nivel",
        max_length=50,
        blank=True,
        null=True,
        choices=niveles,
        default=TERCIARIO
    )

    @property
    def autor(self):
        if self.formato_firma == self.ORIGEN:
            return self.origen.nombre
        elif self.formato_firma == self.INICIAL_ORIGEN:
            return " / ".join([self.corresponsal.persona.iniciales, self.origen.nombre])
        elif self.formato_firma == self.NOMBRE_ORIGEN:
            return " / ".join([self.corresponsal.persona.nombre_completo, self.origen.nombre])
        elif self.formato.nombre.lower() == "opinion":
            return self.corresponsal.persona.nombre_completo


    def __str__(self):
        return self.titulo


    def save(self):
        if self.publicado:
            self.estado = self.PUBLICADO
        else:
            if self.estado == self.PUBLICADO:
                self.estado = self.EDITADO
            else:
                self.estado = self.BORRADOR
        super(Entrada, self).save()
        return

    def delete(self):
        self.estado = self.ELIMINADO
        self.save()
