from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import Equipment
from rest_framework import status
from django.utils.http import urlencode
from django.contrib.auth.models import User

class EquipmentTests(APITestCase):
    def post_equipment(self, _name, _type, _destiny,_login,_username,_email,_password):
        user = User.objects.create_user(_username, _email, _password)
        if _login:
            self.client.login(username = _username, password=_password)
        url = reverse(views.EquipmentList.name)
        data = {
            'name': _name,
            'type': _type,
            'destiny': _destiny,
            'user': user.id
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_equipment_without_login(self):
        response = self.post_equipment('stick', 'iron', 'to back exercise')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # no login

    def test_post_equipment_with_login(self):
        response = self.post_equipment('stick', 'iron', 'to back exercise')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # log in

    def test_equipment_user(self):
        response = self.post_equipment('stick', 'iron', 'to back exercise', 'login123', 'haslo123', 'mail@test.pl')
        user = User.objects.filter(id=response.data['user'])[0]
        self.assertEqual(user.username, 'login123')
        self.assertEqual(user.email, 'mail@test.pl')
        self.assertTrue(user.check_password('haslo123'))

    def test_count_objects(self):
        self.post_equipment('stick', 'iron', 'to back exercise', 'login123', 'haslo123', 'mail@test.pl')
        self.post_equipment('stick', 'iron', 'to back exercise', 'login123566', 'haslo123', 'mail@test.pl')
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 3)

    def test_equipment_return_string(self):
        self.post_equipment('stick', 'iron', 'to back exercise', 'login123', 'haslo123', 'mail@test.pl')
        equipment = Equipment.objects.all()[0]
        self.assertEqual(str(equipment), 'stick')
