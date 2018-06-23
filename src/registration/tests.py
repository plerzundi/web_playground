from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

"""
Algoritmo de prueba para comprobar si el usuario despues
de crearlo se enlaza con un perfil automáticamente
"""


class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)
