#from django.shortcuts import render, get_object_or_404
#from .models import Publicacion

# Create your views here.

#def lista_publicaciones(request):
   # publicaciones = Publicacion.objects.all()
   # return render(request,'inicio.html',{'publicaciones' : publicaciones})

#def detalle_publicacion(request, pk):
   # publicacion = get_object_or_404(Publicacion, pk=pk)#llave primaria que recibimos
   # return render(request, 'detalle_publicacion.html', {'publicacion':
    #publicacion})

from django.views.generic import ListView, DetailView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls import reverse_lazy
from .models import Publicacion


class VistaListaBlog(ListView):
    model = Publicacion
    template_name = 'inicio.html'
    context_object_name = 'publicaciones'


class VistaDetalleBlog(DetailView):
    model = Publicacion
    template_name = 'detalle_publicacion.html'


#class VistaCreacionBlog(CreateView):
  #  model = Publicacion
   # template_name = 'nueva_publicacion.html'
   # fields = ['titulo', 'autor', 'contenido']
   # success_url = reverse_lazy('inicio')  # Redirige tras crear con éxito


#class VistaEdicionBlog(UpdateView):
   # model = Publicacion
   ## template_name = 'edicion_publicacion.html'
   # fields = ['titulo', 'contenido']
   # success_url = reverse_lazy('inicio')  # Redirige tras editar con éxito


#class VistaEliminarBlog(DeleteView):
  ##  model = Publicacion
   # template_name = 'eliminar_publicacion.html'
   # success_url = reverse_lazy('inicio')

   #ListView
   #MultipleObjectTemplateResponseMixin
   #TemplateResponseMixin
   #BaseListView
   #MultipleObjectMixin
   #ConextMixin
   #View


