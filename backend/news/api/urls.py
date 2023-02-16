#!/usr/bin/env python3

from django.urls import path
from news.api.views import NewsViewSet, CategoriasViewSet, MultimediaViewSet, CorresponsalViewSet, CorresponsalEntradaViewSet, ConfiguracionViewSet, EntradasRelacionadasViewSet, BusquedaViewSet, ContadorViewSet, BusquedaMultimediaViewSet, FormatoViewSet, CategoriasBuscadorViewSet


app_name = 'news'

urlpatterns = [

    path(
        'noticias/',
        NewsViewSet.as_view({'get': 'list'}),
        name='news'
    ),

    path(
        'noticias/<pk>',
        NewsViewSet.as_view({'get': 'retrieve'}),
        name='news'
    ),

    path(
        'noticias/<pk>/relacionadas',
        EntradasRelacionadasViewSet.as_view({'get': 'list'}),
        name='news-related'
    ),

    path(
        'categorias/buscador',
        CategoriasBuscadorViewSet.as_view({'get': 'list'}),
        name='menu-buscador'
    ),

    path(
        'categorias/',
        CategoriasViewSet.as_view({'get': 'list'}),
        name='menu'
    ),

    path(
        'formatos/',
        FormatoViewSet.as_view({'get': 'list'}),
        name='formatos'
    ),

    path(
        'multimedia/',
        MultimediaViewSet.as_view({'get': 'list'}),
        name='multimedia'
    ),

    path(
        'multimedia/<pk>',
        MultimediaViewSet.as_view({'get': 'retrieve'}),
        name='multimedia'
    ),

    path(
        'corresponsales/',
        CorresponsalViewSet.as_view({'get': 'list'}),
        name='corresponsales'
    ),

    path(
        'corresponsales/<pk>',
        CorresponsalViewSet.as_view({'get': 'retrieve'}),
        name='corresponsales'
    ),

    path(
        'corresponsal/<pk>/entradas',
        CorresponsalEntradaViewSet.as_view({'get': 'list'}),
        name='corresponsal-entradas'
    ),

    path(
        'multimedia/buscar/',
        BusquedaMultimediaViewSet.as_view({'get': 'list'}),
        name='buscar-multimedia'
    ),

    path(
        'noticias/buscar/',
        BusquedaViewSet.as_view({'get': 'list'}),
        name='buscar'
    ),

    path(
        'configuracion/',
        ConfiguracionViewSet.as_view({'get': 'list'}),
        name='configuracion'
    ),

    path(
        'multimedia/contador/<pk>',
        ContadorViewSet.as_view({'get': 'retrieve'}),
        name='contador'
    ),
]
