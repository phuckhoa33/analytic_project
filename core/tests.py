from django.test import TestCase
from .models import MyUser as User

# Create your tests here.
class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="phuckhoa81@gmail.com", password="332003")
    def test_login(self):
        response = self.client.post('/login/', {'email': 'phuckhoa81@gmail.com', 'password': '3333'})
        self.assertEqual(response.status_code, 200)