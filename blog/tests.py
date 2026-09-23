from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Publicacion
# Create your tests here.
class PruebasBlog(TestCase):
    @classmethod
    def setUpTestData(cls):
     cls.user = get_user_model().objects.create_user(
        username='usuarioprueba',
        email= 'prueba@email.com',
        password= 'secreto'
    )

     cls.publicacion = Publicacion.objects.create(
        titulo='Un buen titulo',
        contenido='Excelente contenido',
        autor=cls.user,
     )

     def test_modelo_publicacion(self):
        self.assertEqual(self.publicacion.titulo, 'Un buen titulo')
        self.assertEqual(self.publicacion.contenido, 'Excelente contenido')
        self.assertEqual(self.publicacion.autor.username, 'usuarioprueba')
        self.assertEqual(str(self.publicacion), 'Un buen titulo')
        self.assertEqual(self.publicacion.get_absolute_url(), '/pub/1/')

     def test_publicacion_listview(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Excelente contenido')
        self.assertTemplateUsed(respuesta, 'inicio.html')

    def test_publicacion_detailview(self):
     respuesta = self.client.get(reverse('detalle_publicacion',kwargs=
({'pk': self.publicacion.pk})))
     sin_respuesta = self.client.get('/pub/1000000/')
     self.assertEqual(respuesta.status_code, 200) 
     self.assertEqual(sin_respuesta.status_code, 404) 
     self.assertContains(respuesta, 'Un buen titulo')
     self.assertTemplateUsed(respuesta, 'detalle_publicacion.html')