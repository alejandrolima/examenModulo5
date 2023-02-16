#!/usr/bin/env python3

from rest_framework import serializers
from news.models import Entrada, Multimedia, Categoria, Multimedia, Corresponsal, Configuracion, Etiqueta, Imagen, Formato


class ImageURLSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        response = super(ImageURLSerializer, self).to_representation(instance)
        if instance.imagen:
            response['imagen'] = instance.imagen.url
        return response


corresponsal_serializer_fields = [
    "id",
    "nombre_completo",
    "cargo",
    "foto",
    "web",
    "twitter",
    "linkedin",
    "email",
    "telefono",
    "biografia",
    "entidad",
    "estado",
    "persona",
]


class ImageSerializer(ImageURLSerializer):

    class Meta:
        model = Multimedia
        fields = ['titulo', 'imagen', 'pie']


class FormatoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Formato
        fields = ["id", "nombre", "sigla"]

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'sigla', 'descripcion', 'color', 'estado']


class CorresponsalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Corresponsal
        fields = corresponsal_serializer_fields

    def to_representation(self, instance):
        response = super(CorresponsalSerializer, self).to_representation(instance)
        if instance.foto:
            response['foto'] = instance.foto.url
        return response

class EtiquetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Etiqueta
        fields = ["nombre"]

class ImagenSerializer(ImageURLSerializer):

    class Meta:
        model = Imagen
        fields = ["id", "nombre", "imagen", "descargas", "imagen_full"]

# class MultimediaSerializer(serializers.ModelSerializer):
class MultimediaSerializer(ImageURLSerializer):

    imagenes = ImagenSerializer(many=True)

    class Meta:
        model = Multimedia
        fields = [
            "id",
            "titulo",
            "imagenes",
            "imagen",
            "pie",
            "fecha",
            "visitas",
            "descargas",
            "lugar",
            "autor",
            "etiqueta",
        ]

    def to_representation(self, instance):
        response = super(MultimediaSerializer, self).to_representation(instance)
        if instance.autor:
            response['autor'] = instance.autor.nombre_completo
        if instance.lugar:
            response['lugar'] = instance.lugar.nombre
        return response

class EntradaSerializer(ImageURLSerializer):

    multimedia = MultimediaSerializer(many=True)
    categoria = CategoriaSerializer(many=True)
    corresponsal = CorresponsalSerializer()
    etiqueta = EtiquetaSerializer(many=True)

    class Meta:
        model = Entrada
        fields = [
            "id",
            "categoria",
            "multimedia",
            "corresponsal",
            "titulo",
            "imagen",
            "lead",
            "autor",
            "cuerpo",
            "enlace",
            "visitas",
            "fecha",
            "nivel",
            "origen",
            "lugar",
            "etiqueta",
            "formato",
        ]

    def to_representation(self, instance):
        response = super(EntradaSerializer, self).to_representation(instance)
        if instance.lugar:
            response['lugar'] = instance.lugar.nombre
        if instance.origen:
            response['origen'] = instance.origen.nombre
        if instance.formato:
            response['formato'] = instance.formato.nombre
        if not instance.imagen:
            if len(instance.multimedia.all()) > 0:
                if len(instance.multimedia.all()[0].imagenes.all()) > 0:
                    response['imagen'] = instance.multimedia.all()[0].imagenes.all()[0].imagen.url

        return response

class EntradaTituloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entrada
        fields = ["id", "titulo"]

class CorresponsalEntradaSerializer(CorresponsalSerializer):

    ultima_entrada = EntradaTituloSerializer()

    class Meta:
        model = Corresponsal
        fields = corresponsal_serializer_fields + ["ultima_entrada"]

class ConfiguracionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Configuracion
        fields = ["nombre", "limite"]
