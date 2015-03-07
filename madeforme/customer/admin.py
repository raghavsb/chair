from django.contrib import admin

from .models import BuyerProfile, MakerProfile

# Models registered to the admin


class BuyerAdmin(admin.ModelAdmin):
	list_display = ('user', 'pincode', 'date_joined','is_maker',)

class MakerAdmin(admin.ModelAdmin):
	list_display = ('user', 'pincode', 'date_joined','is_maker', 'is_approved',)

admin.site.register(BuyerProfile,BuyerAdmin)
admin.site.register(MakerProfile, MakerAdmin)
