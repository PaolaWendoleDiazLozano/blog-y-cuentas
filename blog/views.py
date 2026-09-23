from django.shortcuts import render, get_object_or_404
from .models import Publicacion

# Create your views here.
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request,'inicio.html',{'publicaciones' : publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)#llave primaria que recibimos
    return render(request, 'detalle_publicacion.html', {'publicacion':
    publicacion})

