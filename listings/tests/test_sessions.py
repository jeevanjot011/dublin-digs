from django.test import TestCase, Client
from django.urls import reverse

class PreferredAreaSessionTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_set_preferred_area(self):
        response = self.client.post(reverse('set_preferred_area'), {'area': 'D1'})
        session = self.client.session
        self.assertEqual(session.get('preferred_area'), 'D1')
