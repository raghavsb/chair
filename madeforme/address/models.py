from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from customer.models import BuyerProfile

# Create your models here.

Karnataka = 'KR'
Maharashtra = 'MH'
Tamil_Nadu = 'TN'

Bangalore = 'BLR'
Mumbai = 'BOM'
Chennai = 'MAD'

STATES = ((Karnataka, 'Karnataka'),(Maharashtra, 'Maharashtra'), (Tamil_Nadu, 'Tamil Nadu'))

CITIES = ((Bangalore, 'Bangalore'),(Mumbai, 'Mumbai'),(Chennai, 'Chennai'))

class BuyerAddress(models.Model):
	buyer = models.OneToOneField(BuyerProfile)
	address_line1 = models.CharField(max_length=50)
	address_line2 = models.CharField(max_length=50)
	landmark = models.CharField(max_length=20)
	city = models.CharField(max_length=20, choices=CITIES)
	state = models.CharField(max_length=20, choices=STATES)
	pincode = models.CharField(max_length=6, default='560001')

	class Meta:
		verbose_name = _('address')
		verbose_name_plural = _('addresses')
		ordering = ['buyer']

	def get_buyer(self):
		return self.buyer