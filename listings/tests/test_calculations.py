from django.test import TestCase
from dublindistance.calculations import calculate_distance

class DistanceCalculationTest(TestCase):
    def test_distance_between_postals(self):
        distance = calculate_distance('D1', 'D2')
        self.assertIsNotNone(distance)
        self.assertTrue(distance > 0)

    def test_invalid_area_returns_none(self):
        self.assertIsNone(calculate_distance('D1', 'INVALID'))

    def test_same_area_distance_is_zero(self):
        self.assertEqual(calculate_distance('D1', 'D1'), 0)
