from django.contrib.auth.forms import UserCreationForm  ##formulario para crear usuarios
from django.urls import reverse_lazy ##hace la carga de url hasta que termine el proceso,como una funcion
from django.views.generic import CreateView

# Create your views here.
class VistaRegistro(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') ##para que creando la cuenta inicie la sesion
    template_name = 'registration/signup.html'
    
