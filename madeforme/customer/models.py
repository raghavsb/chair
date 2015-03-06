from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


# Models for Buyers and Makers on madeforme

class Buyer(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='buyer')
	name = models.CharField(max_length=25)
	pincode = models.CharField(max_length=6)
	date_joined = models.DateTimeField(auto_now=False)
	is_maker = models.BooleanField(default=False)

	objects = models.Manager() # default manager for the buyer

	class Meta:
        verbose_name = _('buyer')
        verbose_name_plural = _('buyers')
        ordering = ['email']

    def get_full_name(self):
    	return self.name.strip()

    def get_date_joined(self):
    	return self.date_joined

    def get_location(self):
    	return self.pincode

    def check_maker(self):
    	if is_maker:
    		return True
    	return False


def MakerApprovedManager(models.Manager):
	def get_queryset(self):
		return super(MakerApprovedManager, self).get_queryset().filter(is_approved=True)

class Maker(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='maker')
	name = models.CharField(max_length=25)
	pincode = models.CharField(max_length=6)
	date_joined = models.DateTimeField(auto_now=False)
	is_maker = models.BooleanField(default=True)
	is_approved = models.BooleanField(default=False)

	objects = models.Manager() # default manager for the maker
	approved = models.MakerApprovedManager() # manager for approved makers

	class Meta:
        verbose_name = _('maker')
        verbose_name_plural = _('makers')
        ordering = ['email']

    def get_full_name(self):
    	return name.strip()

    def get_date_joined(self):
    	return self.date_joined

    def get_location(self):
    	return self.pincode

    def check_maker(self):
    	if is_maker:
    		return True
    	return False

    def get_status(self):
    	if is_approved:
    		return True
    	return False