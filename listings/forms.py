from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['property_name', 'area_code', 'monthly_rent', 'contact_info', 'address', 'description']
        widgets = {
            'property_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Cozy Studio'}),
            'area_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., D8'}),
            'monthly_rent': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 1200.00'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 871234567'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'e.g., 123 Main St, Rathmines'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add any details about the property...'}),
        }