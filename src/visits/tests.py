from django.test import TestCase
from django.urls import reverse
from .models import PageVisit

class PageVisitTestCase(TestCase):
    def test_page_visit_creation(self):
        initial_count = PageVisit.objects.count()
        self.client.get(reverse('home'))
        self.assertEqual(PageVisit.objects.count(), initial_count + 1)

    def test_page_visit_path(self):
        self.client.get(reverse('home'))
        latest_visit = PageVisit.objects.latest('id')
        self.assertEqual(latest_visit.path, '/')