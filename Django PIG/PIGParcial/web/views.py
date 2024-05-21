from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import redirect
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    
    #Accedo a la BBDD a traves de los modelos
    context = {
        'nombre': 'Carlos',
        'fecha_hora': datetime.datetime.now()
    }
    
    return render(request, 'web/index.html', context)

# def saludar(request, nombre):
#     print(request.method)
#     return HttpResponse(f"Bienvenid@ {nombre}")

# def alumnos_por_año(request, year):
#     alumnos = ["Carlos", "Maria", "Jose"]
#     return HttpResponse(f"listado de alumnos: {year} \n {alumnos}")

# def listado_alumnos(request):
    
#     contexto = {
#         'alumnos': [
#             'Carlos Lopez',
#             'Maria Del Cerro',
#             'Gaston Perez'
#         ],
        
#         'cuota_al_dia': True
#     }
    
#     return render(request, 'web/listado_alumnos.html', contexto)

# def alta_alumno(request):
    
#     contexto = {}
    
#     if request.method == "GET":
#         contexto['alta_alumno_form'] = AltaAlumnoForm()
        
#     else: #Asumo que es un POST
#         form = AltaAlumnoForm(request.POST)
#         contexto['alta_alumno_form'] = form
        
#         if form.is_valid():
#             #Si el form cumple las validaciones, redirijo a una vista segura (ej index)
            
#             messages.success(request, 'El alumno fue dado de alta con éxito')
            
#             return redirect('index')
        
#         #Si no es valido renderizo un form con mensajes de error
    
#     return render(request, 'web/alta_alumno.html', contexto)

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Tu consulta ha sido enviada con éxito')
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, 'web/contacto.html', {'form': form})

def seguimiento(request):
    if request.method == 'POST':
        form = SeguimientoForm(request.POST)
        if form.is_valid():
            numero_orden = form.cleaned_data['numero_orden']
            dni = form.cleaned_data['dni']
            #orden de simulacion
            orden = {
                'numero_orden': numero_orden,
                'dni': dni,
                'estado': 'En progreso',
                'descripcion': 'Reparación de pantalla',
                'fecha_ingreso': '2024-05-20'
            }
            return render(request, 'web/detalle_orden.html', {'orden': orden})
    else:
        form = SeguimientoForm()
    return render(request, 'web/seguimiento.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            numero_admin = form.cleaned_data['numero_admin']
            contraseña = form.cleaned_data['contraseña']
            #simula validacion de administrador
            if numero_admin == 'admin' and contraseña == 'admin123':
                return redirect('administracion')
            else:
                messages.error(request, 'Credenciales de administrador inválidas')
    else:
        form = AdminLoginForm()
    return render(request, 'web/admin_login.html', {'form': form})

def administracion(request):
    #con BBDD va a ser agregar, modificar o eliminar ordenes
    contexto = {
        'ordenes': [
            {'numero_orden': '001', 'dni': '12345678', 'estado': 'Finalizado'},
            {'numero_orden': '002', 'dni': '87654321', 'estado': 'En progreso'}
        ]
    }
    return render(request, 'web/administracion.html', contexto)