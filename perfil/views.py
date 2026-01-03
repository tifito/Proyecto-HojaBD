from django.shortcuts import render
from .models import DatosPersonales, CursoRealizado, Reconocimientos, ProductosAcademicos, ProductoLaboral, VentaGarage, ExperienciaLaboral

def home(request):
    perfil = DatosPersonales.objects.first()  # Toma el primer perfil que tengas
    context = {
        'perfil': perfil
    }
    return render(request, 'home.html', context)

def cursos(request):
    cursos = CursoRealizado.objects.filter(activarparaqueseveaenfront=True)
    context = {
        'cursos': cursos
    }
    return render(request, 'cursos.html', context)

def reconocimientos(request):
    datos = Reconocimientos.objects.all()  
    context = {'reconocimientos': datos}
    return render(request, 'reconocimientos.html', context)

def academico(request):
    datos = ProductosAcademicos.objects.all()
    context = {'academicos': datos}
    return render(request, 'academico.html', context)

def laboral(request):
    datos = ProductoLaboral.objects.all()
    context = {'laborales': datos}
    return render(request, 'laboral.html', context)

def garage(request):
    datos = VentaGarage.objects.all()
    context = {'garages': datos}
    return render(request, 'garage.html', context)

def experiencia(request):
    datos = ExperienciaLaboral.objects.all()
    context = {'experiencias': datos}
    return render(request, 'experiencia.html', context)
