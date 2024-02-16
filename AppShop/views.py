from django.shortcuts import render

import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

from AppShop import models, forms, funciones


# Create your views here.

def inicio(request):

    diccionario = {"hoy": datetime.datetime.now()}

    plantilla = loader.get_template('AppShop/inicio.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento) 

def cliente(request):
    if request.method == "POST":
        miFormulario = forms.Form_Cliente(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cliente = models.Cliente(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], ciudad=informacion["ciudad"])
            cliente.save()
            hoy = {'hoy': funciones.fecha()}
            return render(request, "AppShop/inicio.html", hoy) # vuela al inicio o a donde quieran
    else:
        miFormulario = forms.Form_Cliente() # Formulario vacio para construir el html
        contexto = {"miFormulario": miFormulario}
        return render(request, "AppShop/cliente.html", contexto)

def vendedor(request):
    if request.method == "POST":
        miFormulario = forms.Form_Vendedor(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            vendedor = models.Vendedor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], sucursal=informacion["sucursal"])
            vendedor.save()
            hoy = {'hoy': funciones.fecha()}
            return render(request, "AppShop/inicio.html", hoy) # vuela al inicio o a donde quieran
    else:
        miFormulario = forms.Form_Vendedor() # Formulario vacio para construir el html
        contexto = {"miFormulario": miFormulario}
        return render(request, "AppShop/vendedor.html", contexto)
    
def producto(request):
    if request.method == "POST":
        miFormulario = forms.Form_Producto(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            producto = models.Producto(marca=informacion["marca"], modelo=informacion["modelo"], costo=informacion["costo"], stock=informacion["stock"])
            producto.save()
            hoy = {'hoy': funciones.fecha()}
            return render(request, "AppShop/inicio.html", hoy) # vuela al inicio o a donde quieran
    else:
        miFormulario = forms.Form_Producto() # Formulario vacio para construir el html
        contexto = {"miFormulario": miFormulario}
        return render(request, "AppShop/producto.html", contexto)
    

def buscar(request):
  if request.GET['sucursal']:
    sucursal = request.GET['sucursal']
    vendedores = models.Vendedor.objects.filter(sucursal__icontains=sucursal)
    print(sucursal)
    print(vendedores)
    hoy = funciones.fecha()
    return render(request, 'AppShop/inicio.html', {'vendedores': vendedores, 'sucursal': sucursal, 'hoy': hoy})
  else:
    respuesta = 'No enviaste datos'
  return render(request, 'AppShop/inicio.html', {'respuesta': respuesta})

