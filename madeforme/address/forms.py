from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django import forms

from .models import BuyerAddress

class BuyerAddressForm(forms.ModelForm):
	class Meta:
		model = BuyerAddress
		fields = ('address_line1','address_line2', 'landmark', 'city', 'state', 'pincode')