from django.test import TestCase, Client
from django.urls import reverse
from visits.models import PageVisit

class LandingPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_landing_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Designed for business teams like yours')

    def test_page_visit_count(self):
        initial_count = PageVisit.objects.count()
        self.client.get(reverse('home'))
        self.assertEqual(PageVisit.objects.count(), initial_count + 1)
