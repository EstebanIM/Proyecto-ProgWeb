from django.urls import path

from LocoRene.views import agregar_pro_car, bandanascompra, eliminar_pro_car, eliminarproducto, historial, home, limpiar_pro_car, modificarproducto, publicarproducto, quienessomos, registro, restar_pro_car, stock, suscribirse, versuscripcion


urlpatterns = [
    path('', home, name="home"),
    path('historial', historial, name="historial"),
    path('versuscripcion', versuscripcion, name= "versuscripcion"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('Productos', bandanascompra, name="bandanascompra"),
    path('stock', stock, name="stock"),
    path('suscribirse', suscribirse, name="suscribirse"),
    path('registro', registro, name="registro"),
    path('publicarproducto',publicarproducto, name="publicarproducto"),
    path('modificarproducto/<id>/',modificarproducto, name="modificarproducto"),
    path('eliminarproducto/<id>/',eliminarproducto, name="eliminarproducto"),
    path('agregar/<producto_id>/', agregar_pro_car, name="agregar_producto"),
    path('eliminar/<producto_id>/', eliminar_pro_car, name="eliminar_producto"),
    path('restar/<producto_id>/', restar_pro_car, name="Sub"),
    path('limpiar/', limpiar_pro_car, name="CLS"),

]

