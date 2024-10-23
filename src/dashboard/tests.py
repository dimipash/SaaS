from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class DashboardTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_dashboard_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/main.html')

    def test_dashboard_unauthenticated(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'landing/main.html')
