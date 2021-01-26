from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import Equipment
from rest_framework import status
from django.utils.http import urlencode
from django.contrib.auth.models import User

class EquipmentTests(APITestCase):
    def post_equipment(self, _name, _type, _destiny,_login=False,_username='',_email='',_password=''):
        user = None
        if _login:
            user = User.objects.create_user(_username, _email, _password)
            user = user.id
            self.client.login(username = _username, password=_password)
        url = reverse(views.EquipmentList.name)
        data = {
            'name': _name,
            'type': _type,
            'destiny': _destiny,
            'user': user
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_equipment_without_login(self):
        response = self.post_equipment('stick', 'iron','to back exercise',False)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # no login

    def test_post_equipment_with_login(self):
        response = self.post_equipment('stick', 'iron', 'to back exercise',True, 'login123','mail@test.pl','haslo123')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # log in

    def test_equipment_user(self):
        response = self.post_equipment('stick', 'iron', 'to back exercise',True, 'login123','mail@test.pl','haslo123')
        user = User.objects.filter(id=response.data['user'])[0]
        self.assertEqual(user.username, 'login123')
        self.assertEqual(user.email, 'mail@test.pl')
        self.assertTrue(user.check_password('haslo123'))

    def test_count_objects(self):
        self.post_equipment('stick', 'iron', 'to back exercise',True, 'login123', 'mail@test.pl','haslo123')
        self.post_equipment('stick', 'iron', 'to back exercise',True, 'login123566', 'mail@test.pl','haslo123')
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_equipment_return_string(self):
        self.post_equipment('stick', 'iron', 'to back exercise',True, 'login123', 'mail@test.pl','haslo123')
        equipment = Equipment.objects.all()[0]
        self.assertEqual(str(equipment), 'stick')
