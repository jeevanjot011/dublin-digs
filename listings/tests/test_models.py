from django.test import TestCase
from listings.models import Listing

class ListingModelTest(TestCase):
    def test_string_representation(self):
        listing = Listing(
            property_name="Test House",
            area_code="D1",
            monthly_rent=1200.00,
            contact_info="871234567",
            address="123 Example Street",
            description="Nice house"
        )
        self.assertEqual(str(listing), "Test House (D1)")
