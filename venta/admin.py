from django.contrib import admin

from django.contrib.admin import ModelAdmin, register, TabularInline, StackedInline

from .models import *

admin.site.site_header = "Urbanizacion Store"

admin.site.site_title = "Urbanizacion Store"

admin.site.index_title = "Bienvenido al Sistema"

@register(Cliente)

class ClienteAdmin(ModelAdmin):

    list_display = ('nombres', 'apellidos', 'telefono', 'fecha_nacimiento')

    list_display_links = ('nombres', 'apellidos')

    search_fields = ['telefono', 'nombres', 'apellidos']

    ordering = ['nombres', 'apellidos']

    fieldsets = [

        ('Datos personales', {'fields': [('nombres', 'apellidos'), ('genero', 'fecha_nacimiento')]}),

        ('Datos de contacto', {'fields': [('telefono', 'email'), ]}),

    ]

@register(Contrato)

class ContratoAdmin(ModelAdmin):

    list_display = ('fecha_inicial', 'fecha_final', 'monto_total', 'tipo_pago', 'cliente_titular', 'lote', 'estado')

    list_display_links = ('fecha_inicial', 'fecha_final',)

    search_fields = ['tipo_pago', 'monto_total']

    ordering = ['lote', 'representante']

    fieldsets = [

        ('Datos', {'fields': [('fecha_inicial', 'fecha_final', 'monto_total'), ('lote', 'tipo_pago')]}),

        ('Cliente', {'fields': [('cliente_titular', 'cliente_testigo', 'estado')]}),

        ('Empresa', {'fields': [('representante')]}),

    ]

@register(Cuota)

class CuotaAdmin(ModelAdmin):

    list_display = ('fecha', 'numero', 'vencimiento', 'total_pago', 'deuda_inicial', 'saldo', 'contrato',)

    list_display_links = ('numero', 'fecha')

    search_fields = ['numero', 'fecha', ]

    ordering = ['contrato', 'numero']

@register(Lote)

class LoteAdmin(ModelAdmin):

    list_display = ('codigo', 'numero', 'estado', 'superficie', 'valor_m2', 'precio', 'manzano')

    list_display_links = ('codigo', 'manzano')

    search_fields = ['superficie', 'valor_m2', ]

    ordering = ['manzano', 'numero']

    fieldsets = [

        ('', {'fields': [('numero', 'codigo', 'manzano',), ('estado')]}),

        ('', {'fields': [('superficie', 'valor_m2', 'precio')]}),

    ]

@register(Manzano)

class ManzanoAdmin(ModelAdmin):

    list_display = ('numero', 'superficie_total', 'precio_total')

    list_display_links = ('numero', 'superficie_total', 'precio_total')

    search_fields = ['numero', ]

    ordering = ['superficie_total', 'precio_total']

    fieldsets = [

        ('', {'fields': [('numero', 'superficie_total', 'precio_total')]}),

    ]

@register(Recibo)

class ReciboAdmin(ModelAdmin):

    pass

@register(Representante)

class RepresentanteAdmin(ModelAdmin):

    list_display = ('nombres', 'apellidos', 'genero', 'telefono',)

    list_display_links = ('nombres', 'apellidos')

    search_fields = ['telefono', 'nombres', 'apellidos']

    ordering = ['apellidos', 'nombres']

    fieldsets = [

        ('', {'fields': [('nombres', 'apellidos'), ('genero', 'telefono')]}),

    ]
