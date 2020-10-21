from rest_framework.test import APITestCase

from rest_framework.test import APIRequestFactory

from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from django.contrib.auth.models import User

from django.urls import reverse

from rest_framework import status

from api import apiviews

from .models import Poll

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object
        """
        url = reverse('user_create')
        data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'password': 'test',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')
        self.assertEqual(User.objects.get().email, 'test@test.com')
        self.assertEqual(User.objects.get().first_name, 'test')
        self.assertEqual(User.objects.get().last_name, 'test')

class TestPoll(APITestCase):
    def setUp(self):
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
    
    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            username='test',
            first_name='test',
            last_name= 'test',
            email= 'test@test.com',
            password= 'test',
        )

    def test_create_poll(self):
        """
        Ensure we can create a new poll
        """
        self.client.login(username='test', password='test')
        data = {
            'question': 'Do you like chicken ?',
            'created_by': 1,
        }
        response = self.client.post(self.uri, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Poll.objects.count(), 1)
        self.assertEqual(Poll.objects.get().question, 'Do you like chicken ?')
        