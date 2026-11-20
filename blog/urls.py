from django.urls import path
from .views import (
    VistaListaBlog, 
    VistaDetalleBlog, 
    # VistaCreacionBlog,
    # VistaEdicionBlog,
    # VistaEliminarBlog,
)

urlpatterns = [
    path('', VistaListaBlog.as_view(), name='inicio'),
    path('pub/<int:pk>/', VistaDetalleBlog.as_view(), name='detalle_publicacion'),
    # path('pub/nvo/', VistaCreacionBlog.as_view(), name='nueva_publicacion'),
    # path('pub/<int:pk>/edit', VistaEdicionBlog.as_view(), name='edicion_publicacion'),
    # path('pub/<int:pk>/elim/', VistaEliminarBlog.as_view(), name='eliminar_publicacion'),
]