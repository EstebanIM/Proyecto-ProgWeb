from django.urls import path
from .views import agregar_producto, eliminar_producto, home, historial, limpiar_carrito, publicarproducto, quienessomos, bandanascompra, restar_producto, stock, modificarproducto, eliminarproducto

urlpatterns = [
    path('', home, name="home"),
    path('historial', historial, name="historial"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('Productos', bandanascompra, name="bandanascompra"),
    path('stock', stock, name="stock"),
    path('publicarproducto',publicarproducto, name="publicarproducto"),
    path('modificarproducto/<id>/',modificarproducto, name="modificarproducto"),
    path('eliminarproducto/<id>/',eliminarproducto, name="eliminarproducto"),
    path('agregar/<producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<producto_id>/', eliminar_producto, name="Del"),
    path('restar/<producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]

