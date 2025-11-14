from django.test import TestCase, Client
from django.urls import reverse
from listings.models import Listing

class BrowseListingsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a sample listing
        Listing.objects.create(
            property_name='Test House',
            area_code='D1',
            monthly_rent=1200.00,
            contact_info='871234567',
            address='123 Example Street',
            description='Nice house'
        )

    def test_browse_listings_status_code(self):
        response = self.client.get(reverse('browse_listings'))
        self.assertEqual(response.status_code, 200)

    def test_browse_listings_context(self):
        response = self.client.get(reverse('browse_listings'))
        self.assertIn('listings_with_distance', response.context)
        self.assertEqual(len(response.context['listings_with_distance']), 1)
