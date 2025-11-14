from django.test import TestCase
from listings.forms import ListingForm

class ListingFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'property_name': 'Test House',
            'area_code': 'D1',
            'monthly_rent': 1200.00,
            'contact_info': '871234567',
            'address': '123 Example Street',
            'description': 'Nice house'
        }
        form = ListingForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_field(self):
        data = {
            'property_name': 'Test House',
            # area_code missing
            'monthly_rent': 1200.00,
            'contact_info': '871234567',
            'address': '123 Example Street',
            'description': 'Nice house'
        }
        form = ListingForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('area_code', form.errors)
