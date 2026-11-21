# cuentas/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PruebasRegistro(TestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/cuentas/signup/")
        self.assertEqual(respuesta.status_code, 200)

    def test_vista_registro(self):
        respuesta = self.client.get(reverse("signup"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "registration/signup.html")

    def test_formulario_registro(self):
        respuesta = self.client.post(
            reverse("signup"),
            {
                "username": "nuevousuario",
                "password1": "Clave-segura-2026",
                "password2": "Clave-segura-2026",
            },
        )
        self.assertRedirects(respuesta, reverse("inicio"))
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.first().username, "nuevousuario")


class PruebasSesion(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(
            username="usuarioprueba", password="Clave-segura-2026"
        )

    def test_iniciar_sesion(self):
        respuesta = self.client.post(
            reverse("login"),
            {"username": "usuarioprueba", "password": "Clave-segura-2026"},
        )
        self.assertRedirects(respuesta, reverse("inicio"))
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta, "Hola usuarioprueba")

    def test_cerrar_sesion(self):
        self.client.login(username="usuarioprueba", password="Clave-segura-2026")
        respuesta = self.client.post(reverse("logout"))
        self.assertRedirects(respuesta, reverse("inicio"))
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta, "Acceder")