from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Bodegas, Autores, Editoriales
from .forms import ProductoForms, BodegasForms, AutoresForms, EditorialesForms


def Home(request):
    return render(request, 'home.html')

def Sobrenosotros(request):
    return render(request, 'sobrenosotros.html')

def Mision(request):
    return render(request, 'mision.html')

def InicioSesion(request):
    return render(request, 'iniciosesion.html')

def Mantenedor(request):
    listado= Producto.objects.all()
    return render(request, 'mantenedor.html', {"listado": listado})

#Función que nos permite agregar productos hacia nuestra BD
def agregar_producto(request):
    data = {
        'form': ProductoForms()
    }

    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Agregado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'Mantenedor/agregarproducto.html', data)

#Función que nos permite agregar bodegas hacia nuestra BD
def agregar_bodegas(request):
    data = {
        'form': BodegasForms()
    }

    if request.method == 'POST':
        formulario = BodegasForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Agregado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'Mantenedor/agregarbodegas.html', data)

#Función que nos permite agregar autores hacia nuestra BD
def agregar_autores(request):
    data = {
        'form': AutoresForms()
    }

    if request.method == 'POST':
        formulario = AutoresForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Agregado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'Mantenedor/agregarautores.html', data)

#Función que nos permite agregar editoriales hacia nuestra BD
def agregar_editoriales(request):
    data = {
        'form': EditorialesForms()
    }

    if request.method == 'POST':
        formulario = EditorialesForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Agregado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'Mantenedor/agregareditoriales.html', data)
    
#Función que nos permite realizar modificaciones dentro dentro del mantenedor CRUD    
def modificar_producto(request, id):
    pro= Producto.objects.get(idproducto=id)
    data = {
        'form': ProductoForms(instance=pro)
    }

    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST, instance=pro)
        if formulario.is_valid():
            formulario.save()  
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario

    return render(request, 'Mantenedor/modificar.html', data)








#from django.views.generic import TemplateView


#class HomePageView(TemplateView):
    #template_name = "home.html"

#class AboutPageView(TemplateView):
    #template_name = "about.html"

#class MisionPageView(TemplateView):
    #template_name = "mision.html"

#class InicioSesionPageView(TemplateView):
    #template_name = "iniciosesion.html"

#class MantenedorPageView(TemplateView):
    #template_name = "mantenedor.html"




