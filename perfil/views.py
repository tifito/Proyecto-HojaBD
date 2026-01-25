from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from .models import (
    DatosPersonales,
    CursoRealizado,
    Reconocimientos,
    ProductosAcademicos,
    ProductoLaboral,
    VentaGarage,
    ExperienciaLaboral
)

# -------------------------
# UTILIDAD
# -------------------------
def perfil_activo():
    perfil = DatosPersonales.objects.first()
    return perfil if perfil and perfil.perfilactivo else None


# -------------------------
# HOME
# -------------------------
def home(request):
    perfil = perfil_activo()
    return render(request, 'home.html', {'perfil': perfil})


# -------------------------
# CURSOS (ordenados por fecha inicio)
# -------------------------
def cursos(request):
    perfil = perfil_activo()
    cursos = (
        CursoRealizado.objects
        .filter(activarparaqueseveaenfront=True)
        .order_by('-fechainicio')
        if perfil else None
    )
    return render(request, 'cursos.html', {
        'perfil': perfil,
        'cursos': cursos
    })


# -------------------------
# RECONOCIMIENTOS (ordenados por fecha reconocimiento)
# -------------------------
def reconocimientos(request):
    perfil = perfil_activo()
    datos = (
        Reconocimientos.objects
        .filter(activarparaqueseveaenfront=True)
        .order_by('-fechareconocimiento')
        if perfil else None
    )
    return render(request, 'reconocimientos.html', {
        'perfil': perfil,
        'reconocimientos': datos
    })


# -------------------------
# PRODUCTOS ACADÉMICOS
# (no llevan fecha → no se ordenan)
# -------------------------
def academico(request):
    perfil = perfil_activo()
    datos = (
        ProductosAcademicos.objects
        .filter(activarparaqueseveaenfront=True)
        if perfil else None
    )
    return render(request, 'academico.html', {
        'perfil': perfil,
        'academico': datos
    })


# -------------------------
# PRODUCTO LABORAL (ordenado por fecha producto)
# -------------------------
def laboral(request):
    perfil = perfil_activo()
    productos = (
        ProductoLaboral.objects
        .filter(activarparaqueseveaenfront=True)
        .order_by('-fechaproducto')
        if perfil else None
    )
    return render(request, 'laboral.html', {
        'perfil': perfil,
        'productolaboral': productos
    })


# -------------------------
# VENTA DE GARAGE (ordenado por fecha publicación)
# -------------------------
def garage(request):
    perfil = perfil_activo()
    productos = (
        VentaGarage.objects
        .filter(activarparaqueseveaenfront=True)
        .order_by('-fechapublicacion')
        if perfil else None
    )
    return render(request, 'garage.html', {
        'perfil': perfil,
        'ventagarage': productos
    })


# -------------------------
# EXPERIENCIA LABORAL
# (ordenada por fecha inicio)
# -------------------------
def experiencia(request):
    perfil = perfil_activo()
    datos = (
        ExperienciaLaboral.objects
        .filter(activarparaqueseveaenfront=True)
        .order_by('-fechainiciogestion')
        if perfil else None
    )
    return render(request, 'experiencia.html', {
        'perfil': perfil,
        'experiencias': datos
    })


# -------------------------
# PDF CV (respetando orden cronológico)
# -------------------------
def cv_pdf(request):
    perfil = perfil_activo()

    context = {
        'perfil': perfil,
        'academico': ProductosAcademicos.objects.filter(activarparaqueseveaenfront=True),
        'cursos': CursoRealizado.objects.filter(
            activarparaqueseveaenfront=True
        ).order_by('-fechainicio'),
        'experiencias': ExperienciaLaboral.objects.filter(
            activarparaqueseveaenfront=True
        ).order_by('-fechainiciogestion'),
        'productos': ProductoLaboral.objects.filter(
            activarparaqueseveaenfront=True
        ).order_by('-fechaproducto'),
        'reconocimientos': Reconocimientos.objects.filter(
            activarparaqueseveaenfront=True
        ).order_by('-fechareconocimiento'),
    }

    template = get_template('cvpdf.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="cv.pdf"'
    pisa.CreatePDF(html, dest=response)

    return response
