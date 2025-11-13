from django.db import models
from django.core.validators import RegexValidator

class Listing(models.Model):
    property_name = models.CharField(max_length=100)
    area_code = models.CharField(max_length=10)

    monthly_rent = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Enter rent in euros (e.g., 1200.00)"
    )

    contact_info = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex=r'^\d{9}$',
                message="Enter a valid 9-digit Irish mobile number (e.g., 871234567)"
            )
        ],
        help_text="Only 9 digits. +353 will be added automatically."
    )

    address = models.TextField(help_text="Full address including street and area")
    description = models.TextField(blank=True, help_text="Optional: Add details about the property")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property_name} ({self.area_code})"

    def formatted_contact(self):
        return f"+353 {self.contact_info}"
