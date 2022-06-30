from math import prod
from django.shortcuts import redirect, render

from LocoRene.Carrito import Carrito
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .serializers import ProductoSerializer
# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def versuscripcion(request):
    return render(request, 'LocoRene/versuscripcion.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro Exitoso")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def suscribirse (request):
    return render (request, 'LocoRene/suscribirse.html')

def home(request):
    return render(request,  'LocoRene/home.html')

def historial(request):
    return render(request,  'LocoRene/historial.html')   

def quienessomos(request):
    return render(request,  'LocoRene/quienessomos.html')  

def bandanascompra(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request,  'LocoRene/bandanascompra.html',data)
@login_required
def stock(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request,  'LocoRene/adminstock.html',data)
@login_required
def publicarproducto(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario .save()
            messages.success(request, "Guardado Correctamente")
        else:
            data["form"]=formulario
    return render(request,  'LocoRene/publicarproducto.html',data)  

@login_required
def modificarproducto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario .save()
            messages.success(request, "Modificado Correctamente")
        data["form"]=formulario
        return redirect (to= "stock" )
    return render(request,  'LocoRene/Modificar_Producto.html',data) 

def eliminarproducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to= "stock")

# carrito
def agregar_pro_car(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("bandanascompra")

def eliminar_pro_car(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("bandanascompra")

def restar_pro_car(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("bandanascompra")

def limpiar_pro_car(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("bandanascompra")