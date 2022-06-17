from django.contrib import admin

from LocoRene.models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin): 
    list_display = ["nombre", "precio", "stock", "imagen"]
    list_editable = ["precio"]
admin.site.register(Producto, ProductoAdmin)