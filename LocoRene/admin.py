from django.contrib import admin

from LocoRene.models import Producto, Usuario

# Register your models here.
class ProductoAdmin(admin.ModelAdmin): 
    list_display = ["nombre", "precio", "stock", "imagen"]
    list_editable = ["precio"]
admin.site.register(Producto, ProductoAdmin)

class UsuarioAdmin(admin.ModelAdmin): 
    list_display = ["nombre", "apellido", "correo", "password"]
admin.site.register(Usuario, UsuarioAdmin)