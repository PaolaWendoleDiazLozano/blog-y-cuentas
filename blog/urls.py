from django.urls import path
from .views import (
    VistaListaBlog, 
    VistaDetalleBlog, 
    # --- Práctica 6 (Tema 2.11: Formularios) ---
    VistaCreacionBlog,
    VistaEdicionBlog,
    VistaEliminarBlog,
)

urlpatterns = [
    # --- Práctica 5 (Tema 2.10: Listado y Detalle) ---
    path('', VistaListaBlog.as_view(), name='inicio'),
    path('pub/<int:pk>/', VistaDetalleBlog.as_view(), name='detalle_publicacion'),
    # --- Práctica 6 (Tema 2.11: Formularios CRUD) ---
    path('pub/nvo/', VistaCreacionBlog.as_view(), name='nueva_publicacion'),
    path('pub/<int:pk>/edit', VistaEdicionBlog.as_view(), name='edicion_publicacion'),
    path('pub/<int:pk>/elim/', VistaEliminarBlog.as_view(), name='eliminar_publicacion'),
]