#!/usr/bin/env python3

import datetime
from django.utils.dateparse import parse_datetime
from rest_framework import viewsets, pagination
from rest_framework.response import Response
from django.db.models import Q
from django.conf import settings
from news.models import Entrada, Categoria, Multimedia, Corresponsal, Configuracion, Imagen, Formato
from news.api.serializers import EntradaSerializer, CategoriaSerializer, MultimediaSerializer, CorresponsalSerializer, ConfiguracionSerializer, CorresponsalEntradaSerializer, ImagenSerializer, FormatoSerializer
from itertools import chain
from functools import reduce


class NewsPagination(pagination.LimitOffsetPagination):
       page_size = 3

class NewsViewSet(viewsets.ModelViewSet):

    serializer_class = EntradaSerializer
    pagination_class = NewsPagination

    def get_queryset(self):
        queryset = Entrada.objects.filter(publicado=True, estado=Entrada.PUBLICADO).order_by("-fecha")

        if "categoria" in self.request.GET:
            queryset = queryset.filter(categoria__nombre=self.request.GET["categoria"])

        if "nivel" in self.request.GET:
            queryset = queryset.filter(nivel=self.request.GET["nivel"])

        if "etiqueta" in self.request.GET:
            queryset = queryset.filter(etiqueta__nombre=self.request.GET["etiqueta"])

        if "formato" in self.request.GET:
            queryset = queryset.filter(formato__sigla=self.request.GET["formato"])

        if "corresponsal" in self.request.GET:
            queryset = queryset.filter(corresponsal=self.request.GET["corresponsal"])

        return queryset

    def retrieve(self, request, *args, **kwargs):
        noticia = self.get_object()
        if noticia.visitas is not None:
            noticia.visitas = noticia.visitas + 1
        else:
            noticia.visitas = 1
        noticia.save()
        return super(NewsViewSet, self).retrieve(request, *args, **kwargs)

class CategoriasViewSet(viewsets.ModelViewSet):

    queryset = Categoria.objects.filter(estado="ACTIVO")
    serializer_class = CategoriaSerializer

class CategoriasBuscadorViewSet(viewsets.ModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class FormatoViewSet(viewsets.ModelViewSet):

    queryset = Formato.objects.all()
    serializer_class = FormatoSerializer

class MultimediaViewSet(viewsets.ModelViewSet):

    serializer_class = MultimediaSerializer
    queryset = Multimedia.objects.all().order_by("-fecha")
    pagination_class = NewsPagination

class CorresponsalViewSet(viewsets.ModelViewSet):

    serializer_class = CorresponsalEntradaSerializer
    pagination_class = NewsPagination

    def get_queryset(self):
        queryset = Corresponsal.objects.all()

        if "perfil" in self.request.GET:
            queryset = queryset.filter(perfil__sigla=self.request.GET["perfil"])

        return queryset

class CorresponsalEntradaViewSet(viewsets.ModelViewSet):

    serializer_class = EntradaSerializer
    pagination_class = NewsPagination

    def get_queryset(self):
        queryset = Entrada.objects.filter(publicado=True, corresponsal=self.kwargs['pk'])

        if "formato" in self.request.GET:
            queryset = queryset.filter(formato__sigla=self.request.GET["formato"])

        return queryset

class ConfiguracionViewSet(viewsets.ModelViewSet):

    serializer_class = ConfiguracionSerializer
    queryset = Configuracion.objects.all()

class BusquedaMultimediaViewSet(viewsets.ModelViewSet):

    serializer_class = MultimediaSerializer
    pagination_class = NewsPagination

    def get_queryset(self):
        query = self.request.GET['q']
        queryset = Multimedia.objects.filter(Q(titulo__icontains=query) | Q(pie__icontains=query)).order_by("-fecha")

        if "inicio" in self.request.GET:
            queryset = queryset.filter(fecha__gte=self.request.GET["inicio"])

        if "fin" in self.request.GET:
            fin = parse_datetime(self.request.GET["fin"]) + datetime.timedelta(days=1)
            queryset = queryset.filter(fecha__lte=fin)

        return queryset

class BusquedaViewSet(viewsets.ModelViewSet):

    serializer_class = EntradaSerializer
    pagination_class = NewsPagination

    def get_queryset(self):
        query = self.request.GET['q']
        queryset = Entrada.objects.filter(Q(titulo__icontains=query) | Q(lead__icontains=query) | Q(cuerpo__icontains=query)).order_by("-fecha")

        if "categoria" in self.request.GET:
            queryset = queryset.filter(categoria=self.request.GET["categoria"])

        # if "etiqueta" in self.request.GET:
        #     queryset = queryset.filter(etiqueta__nombre=self.request.GET["etiqueta"])

        if "formato" in self.request.GET:
            queryset = queryset.filter(formato=self.request.GET["formato"])

        if "inicio" in self.request.GET:
            queryset = queryset.filter(fecha__gte=self.request.GET["inicio"])

        if "fin" in self.request.GET:
            fin = parse_datetime(self.request.GET["fin"]) + datetime.timedelta(days=1)
            queryset = queryset.filter(fecha__lte=fin)

        return queryset

class EntradasRelacionadasViewSet(viewsets.ModelViewSet):

    serializer_class = EntradaSerializer
    pagination_class = NewsPagination

    def get_queryset(self):
        entrada = Entrada.objects.get(pk=self.kwargs['pk'])
        etiquetas = [e for e in entrada.etiqueta.all()]
        if len(etiquetas) == 0:
            return Entrada.objects.none()
        elif len(etiquetas) == 1:
            return Entrada.objects.filter(etiqueta=etiquetas[0])
        elif len(etiquetas) > 1:
            # options = [e.nombre for e in etiquetas]
            # query = reduce(lambda x, y: Q(etiqueta=x) | Q(etiqueta=y), options)
            # print(query, type(query))
            # queryset = Entrada.objects.filter(query)
            # return queryset
            return Entrada.objects.filter(etiqueta=etiquetas[0])

class ContadorViewSet(viewsets.ModelViewSet):

    serializer_class = ImagenSerializer
    queryset = Imagen.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs['pk'])
        instance.descargas += 1
        instance.save()
        return Response(self.serializer_class(instance).data)
