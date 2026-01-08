from django.shortcuts import render
from .models import DatosPersonales, CursoRealizado, Reconocimientos, ProductosAcademicos, ProductoLaboral, VentaGarage, ExperienciaLaboral

def home(request):
    perfil = perfil_activo()
    return render(request,'home.html',{'perfil':perfil})

def cursos(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=True).first()
    cursos = CursoRealizado.objects.filter(activarparaqueseveaenfront=True) if perfil else None
    return render(request, 'cursos.html', {'perfil': perfil, 'cursos': cursos})


def reconocimientos(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=True).first()
    datos = Reconocimientos.objects.all() if perfil else None
    return render(request,'reconocimientos.html',{'perfil':perfil,'reconocimientos':datos})

def academico(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=True).first()
    datos = ProductosAcademicos.objects.filter(activarparaqueseveaenfront=True) if perfil else None
    return render(request,'academico.html',{'perfil':perfil,'academico':datos})

def laboral(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=True).first()
    productos = ProductoLaboral.objects.filter(activarparaqueseveaenfront=True) if perfil else None
    return render(request,'laboral.html',{'perfil':perfil,'productolaboral':productos})

def garage(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=True).first()
    productos = VentaGarage.objects.filter(activarparaqueseveaenfront=True) if perfil else None
    return render(request,'garage.html',{'perfil':perfil,'ventagarage':productos})

def experiencia(request):
    perfil = perfil_activo()
    if not perfil:
        return render(request,'experiencia.html',{'perfil':None})
    datos = ExperienciaLaboral.objects.all()
    return render(request,'experiencia.html',{'perfil':perfil,'experiencias':datos})

def perfil_activo():
    perfil = DatosPersonales.objects.first()
    return perfil if perfil and perfil.perfilactivo else None