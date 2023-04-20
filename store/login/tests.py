from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from login.models import User, EmailVerification


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'Valeriys', 'last_name': 'fgsfg',
            'username': 'valeriys', 'email': 'Val@mail.ru',
            'password1': '12345678pP', 'password2': '12345678pP',
        }
        self.username = self.data['username']
        self.path = reverse('regist')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/registration.html')

    def test_user_registration_post_success(self):


        self.assertFalse(User.objects.filter(username=self.username).exists())
        response = self.client.post(self.path, self.data)

        #check creating of user
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username=self.username).exists())

        #check creation of email verification
        email_verification = EmailVerification.objects.filter(user__username=self.username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(email_verification.first().expiration.date(), (now() + timedelta(hours=24)).date())
