from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_customer_creation(self):
        customer = Customer.objects.create(user=self.user)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.user, self.user)