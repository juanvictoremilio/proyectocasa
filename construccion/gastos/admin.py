from django.contrib import admin

# Register your models here.

from .models import Material, Servicios

admin.site.site_header = "Relación de Gastos en el Proyecto de nuestra casa "

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'concepto', 'proveedor', 'cantidad']
    search_fields = ['concepto', 'proveedor']
    readonly_fields = []
    list_filter = ['fecha', 'concepto', 'proveedor']
    list_editable = ['proveedor', 'concepto',]
    list_per_page = 15

admin.site.register(Material, MaterialAdmin)


class ServiciosAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'concepto', 'proveedor', 'cantidad']
    search_fields = ['concepto', 'proveedor']
    readonly_fields = []
    list_filter = ['fecha', 'concepto', 'proveedor']
    list_editable = ['proveedor', 'concepto',]
    list_per_page = 15
admin.site.register(Servicios, ServiciosAdmin)

