from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm  ##formulario para crear usuarios
from django.urls import reverse_lazy ##hace la carga de url hasta que termine el proceso,como una funcion
from django.views.generic import CreateView

# Create your views here.
class VistaRegistro(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('inicio') ##redirige al inicio ya con la sesión iniciada
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        respuesta = super().form_valid(form)
        login(self.request, self.object)
        return respuesta