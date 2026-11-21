from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Publicacion


class PruebasBlog(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='usuarioprueba',
            email='prueba@email.com',
            password='secreto'
        )

        cls.publicacion = Publicacion.objects.create(
            titulo='Un buen titulo',
            contenido='Excelente contenido',
            autor=cls.user,
        )

    # --- Práctica 5 (Tema 2.10: Listado y Detalle) ---
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
        respuesta = self.client.get(reverse('detalle_publicacion', kwargs={'pk': self.publicacion.pk}))
        sin_respuesta = self.client.get('/pub/1000000/')
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(sin_respuesta.status_code, 404)
        self.assertContains(respuesta, 'Un buen titulo')
        self.assertContains(respuesta, 'Volver al inicio')
        self.assertContains(respuesta, reverse('inicio'))
        self.assertTemplateUsed(respuesta, 'detalle_publicacion.html')

    # --- Práctica 6 (Tema 2.11: Formularios CRUD) + Práctica 7 (Requiere sesión) ---
    def test_vista_creacion_publicacion(self):
        self.client.login(username='usuarioprueba', password='secreto')  # Práctica 7
        respuesta = self.client.post(
            reverse('nueva_publicacion'),
            {
                'titulo': 'Nuevo titulo',
                'contenido': 'Nuevo texto',
            }
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(Publicacion.objects.last().titulo, 'Nuevo titulo')
        self.assertEqual(Publicacion.objects.last().contenido, 'Nuevo texto')
        self.assertEqual(Publicacion.objects.last().autor, self.user)  # Práctica 7: autor automático

    def test_vista_edicion_publicacion(self):
        self.client.login(username='usuarioprueba', password='secreto')  # Práctica 7
        respuesta = self.client.post(
            reverse('edicion_publicacion', args='1'),
            {
                'titulo': 'Titulo actualizado',
                'contenido': 'Texto actualizado',
            },
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(Publicacion.objects.last().titulo, 'Titulo actualizado')
        self.assertEqual(Publicacion.objects.last().contenido, 'Texto actualizado')

    def test_vista_eliminar_publicacion(self):
        self.client.login(username='usuarioprueba', password='secreto')  # Práctica 7
        respuesta = self.client.post(
            reverse('eliminar_publicacion', args='1')
        )
        self.assertEqual(respuesta.status_code, 302)

    def test_vista_eliminar_publicacion_get(self):
        self.client.login(username='usuarioprueba', password='secreto')  # Práctica 7
        respuesta = self.client.get(
            reverse('eliminar_publicacion', args='1')
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, 'eliminar_publicacion.html')
        self.assertTrue(Publicacion.objects.filter(pk=self.publicacion.pk).exists())

    # --- Práctica 7 (Tema 2.12: Cuentas de usuario y protección de rutas) ---
    def test_redirige_sin_sesion(self):
        respuesta = self.client.get(reverse('nueva_publicacion'))
        self.assertEqual(respuesta.status_code, 302)
        self.assertRedirects(respuesta, f"{reverse('login')}?next={reverse('nueva_publicacion')}")

    def test_vista_registro(self):
        respuesta = self.client.get(reverse('signup'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, 'registration/signup.html')