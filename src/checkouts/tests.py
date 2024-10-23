from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class CheckoutTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_checkout_redirect(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('stripe-checkout-start'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('pricing', response.url)