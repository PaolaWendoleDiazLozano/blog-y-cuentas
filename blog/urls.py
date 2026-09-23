from django.urls import path
from .views import lista_publicaciones, detalle_publicacion

urlpatterns = [
    path('',lista_publicaciones, name='inicio'),
    path('pub/<int:pk>/',  detalle_publicacion,
    name='detalle_publicacion'),
]