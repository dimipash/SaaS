from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserSubscription


class SubscriptionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_subscription_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("user_subscription"))
        self.assertEqual(response.status_code, 200)

    def test_subscription_creation(self):
        self.client.force_login(self.user)
        initial_count = UserSubscription.objects.count()
        response = self.client.post(reverse("stripe-checkout-start"), {"plan": "basic"})
        self.assertEqual(response.status_code, 302)

        print(
            f"Initial count: {initial_count}, Final count: {UserSubscription.objects.count()}"
        )

        self.assertEqual(UserSubscription.objects.count(), initial_count + 1)

    def test_subscription_creation_process(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("stripe-checkout-start"), {"plan": "basic"})
        self.assertEqual(response.status_code, 302)

        subscription = UserSubscription.objects.filter(user=self.user).first()
        self.assertIsNotNone(subscription)
        self.assertEqual(subscription.plan, "basic")
