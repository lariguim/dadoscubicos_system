from django import forms
from .models import CustomerProfile

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['company_name', 'phone', 'address']