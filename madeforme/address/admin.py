from django.contrib import admin

from .models import BuyerAddress

# Models registered to the admin


class BuyerAddressAdmin(admin.ModelAdmin):
	fields = ('buyer', 'address_line1','address_line2', 'landmark', 'city', 'state', 'pincode')

admin.site.register(BuyerAddress,BuyerAddressAdmin)