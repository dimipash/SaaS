from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.management import call_command

class MainTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('collectstatic', interactive=False, verbosity=0)
        User.objects.create_user(username='testuser', password='12345', email='testuser@example.com')

    def setUp(self):
        self.client = Client()

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_landing_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Designed for business teams like yours')

    def test_user_login(self):
        response = self.client.post(reverse('account_login'), {'login': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/confirm-email/')

    def test_subscription_creation(self):
        user = User.objects.get(username='testuser')
        self.client.force_login(user)
        response = self.client.post(reverse('stripe-checkout-start'), {'plan': 'basic'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('pricing', response.url)