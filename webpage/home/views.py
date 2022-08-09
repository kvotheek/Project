from django.shortcuts import render, redirect
# from .models import Registro  #Y este Registro debe ser un modelo creado en donde se va a registrar los datos necesarios para el registro de la persona.

# Create your views here.
def inicio(request):

    return render(request, 'inicio.html') #devuelve la pagina de inicio del home 

def registro(request):
    return render (request, 'registro.html') #retorna la pagina de registro 

def registro_exitoso(request):
    """
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtNombre']
    mail=request.POST['txtNombre']
    usuario=request.POST['txtNombre']
    clave=request.POST['txtNombre']

    usuario= Registro.objects.create(nombre=nombre, apellido=apellido, mail=mail, usuario=usuario, clave=clave)
    """
    return render (request, 'registro_exitoso.html')

