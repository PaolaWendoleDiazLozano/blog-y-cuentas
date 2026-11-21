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

# --- Práctica 7 (Tema 2.12: Cuentas de usuario - Protección de vistas) ---
from django.contrib.auth.mixins import LoginRequiredMixin
# --- Práctica 5 (Vistas basadas en clases) ---
from django.views.generic import ListView, DetailView
# --- Práctica 6 (Tema 2.11: Formularios) ---
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Publicacion


# --- Práctica 5 (Vistas de inicio y detalle) ---
class VistaListaBlog(ListView):
    model = Publicacion
    template_name = 'inicio.html'
    context_object_name = 'publicaciones'


class VistaDetalleBlog(DetailView):
    model = Publicacion
    template_name = 'detalle_publicacion.html'


# --- Práctica 6 (Tema 2.11: Formularios CRUD) y Práctica 7 (LoginRequiredMixin y autor) ---
class VistaCreacionBlog(LoginRequiredMixin, CreateView):
    model = Publicacion
    template_name = 'nueva_publicacion.html'
    fields = ['titulo', 'contenido']  # Práctica 7: se quita 'autor' para asignarlo automáticamente

    def form_valid(self, form):  # Práctica 7: asigna el usuario actual como autor
        form.instance.autor = self.request.user
        return super().form_valid(form)


class VistaEdicionBlog(LoginRequiredMixin, UpdateView):
    model = Publicacion
    template_name = 'edicion_publicacion.html'
    fields = ['titulo', 'contenido']


class VistaEliminarBlog(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = 'eliminar_publicacion.html'
    success_url = reverse_lazy('inicio')

   #ListView
   #MultipleObjectTemplateResponseMixin
   #TemplateResponseMixin
   #BaseListView
   #MultipleObjectMixin
   #ConextMixin
   #View