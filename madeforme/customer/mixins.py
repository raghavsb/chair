from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, PermissionDenied, ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy, reverse

# Mixins used in the customer app

class CheckProfileMixin(object):
	"""
		Mixin to check the type of profile and respond with the appropriate profile of a buyer or a maker 
	"""

	def get_profile_type(self):
		user = self.request.user
		try:
			self.profile = user.buyerprofile
			buyername = self.profile.get_full_name()
			self.url = reverse('customer:profileview', kwargs = {'user_name': buyername})
			return self
		except ObjectDoesNotExist as NotaBuyer:
			try:
				self.profile = user.makerprofile # check this logic of adding data to self.buyer
				makername = self.profile.get_full_name()
				self.url = reverse('customer:profileview', kwargs = {'user_name': makername})
				return self
			except ObjectDoesNotExist as NotaMaker:
				messages.warning(request, 'Profile Does not Exist')
				return reverse('homepage')


