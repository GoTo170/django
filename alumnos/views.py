from django.shortcuts import render
from .models import Genero, Alumnos

# Create your views here.
def index(request):
    Alumnos = Alumnos.objects.all()#select * from
    context = {"alumnos":Alumnos}
    return render(request, "alumnos/index.html", context)

def index2(request):
    Alumnos = Alumnos.raw('SELECT * FROM alumnos_alumno')#select * from
    context = {"alumnos":Alumnos}
    return render(request, "alumnos/listadoSQL.html", context)