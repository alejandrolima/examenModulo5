from django.contrib import admin
from .models import Categoria, Corresponsal, Entrada, Etiqueta, Formato, Lugar, Multimedia, Origen, Perfil, Persona, Usuario, Configuracion, Imagen

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    exclude = ["usuario_actualizacion", "transaccion"]
    list_display = ["nombre", "sigla", "descripcion", "estado"]

@admin.register(Corresponsal)
class CorresponsalAdmin(admin.ModelAdmin):
    exclude = ["usuario_actualizacion", "transaccion", "estado"]

# actions for EntradaAdmin

def publicar(modeladmin, request, queryset):
    for obj in queryset:
        obj.publicado = True
        obj.save()
publicar.short_description = 'Publicar entradas'

def no_publicar(modeladmin, request, queryset):
    for obj in queryset:
        obj.publicado = False
        obj.save()
no_publicar.short_description = 'No publicar entradas'

def nivel_primario(modeladmin, request, queryset):
    queryset.update(nivel=Entrada.PRIMARIO)
nivel_primario.short_description = 'Cambiar nivel a "Primario"'

def nivel_secundario(modeladmin, request, queryset):
    queryset.update(nivel=Entrada.SECUNDARIO)
nivel_secundario.short_description = 'Cambiar nivel a "Secundario"'

def nivel_terciario(modeladmin, request, queryset):
    queryset.update(nivel=Entrada.TERCIARIO)
nivel_terciario.short_description = 'Cambiar nivel a "Terciario"'

def nivel_especial(modeladmin, request, queryset):
    queryset.update(nivel=Entrada.ESPECIAL)
nivel_especial.short_description = 'Cambiar nivel a "Especial"'

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    # exclude = ["dependencia", "enlace", "usuario_creacion", "usuario_modificacion", "visitas", "estado"]
    fields = ["titulo", "imagen", "multimedia", "lead", "cuerpo", "corresponsal", "formato_firma", "publicado", "origen",
              "lugar", "etiqueta", "fecha", "formato", "categoria", "nivel"
    ]
    list_display = ["titulo", "estado", "publicado", "fecha", "nivel", "categorias", "visitas"]
    search_fields = ["titulo", "lead", "cuerpo"]
    filter_horizontal = ["multimedia", "etiqueta"]
    actions = [publicar, no_publicar, nivel_primario, nivel_secundario, nivel_terciario, nivel_especial]

    def categorias(self, obj):
        return ", ".join([c.nombre for c in obj.categoria.all()])

admin.site.register(Etiqueta)

@admin.register(Formato)
class FormatoAdmin(admin.ModelAdmin):
    exclude = ["usuario_actualizacion", "transaccion", "estado"]

admin.site.register(Lugar)

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    exclude = ["descargas"]
    list_display = ["nombre", "imagen", "descargas"]

class ImagenInline(admin.TabularInline):
    model = Imagen
    exclude = ["descargas"]

@admin.register(Multimedia)
class MultimediaAdmin(admin.ModelAdmin):
    exclude = ["enlace", "ruta", "imagen", "usuario_creacion", "visitas", "descargas"]
    list_display = ["titulo", "pie", "autor", "descargas"]
    search_fields = ["titulo", "pie"]
    inlines = [ImagenInline]

@admin.register(Origen)
class OrigenAdmin(admin.ModelAdmin):
    exclude = ["usuario_creacion", "estado"]

admin.site.register(Perfil)
admin.site.register(Persona)
# admin.site.register(Usuario)

@admin.register(Configuracion)
class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ["nombre", "limite"]
