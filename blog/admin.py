from django.contrib import admin
from.models import Publicacion

class PublicacionAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'autor',
        'contenido',
    )
# Register your models here.
admin.site.register(Publicacion, PublicacionAdmin)