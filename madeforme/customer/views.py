from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView, UpdateView, RedirectView, TemplateView

from .forms import BuyerCreationMultiForm, MakerCreationMultiForm
from .models import BuyerProfile, MakerProfile

# Customer creation and login views

class BuyerSignupView(CreateView):
	form_class = BuyerCreationMultiForm
	success_url = reverse_lazy('homepage')
	template_name = 'registration.html'

class MakerSignupView(CreateView):
	form_class = MakerCreationMultiForm
	success_url = reverse_lazy('homepage')
	template_name = 'registration.html'

class CustomerRedirectView(RedirectView):
	
	def get(self, request, *args, **kwargs):
		user = self.request.user
		try:
			buyer = user.buyerprofile # check this logic of adding data to self.buyer
			buyername = buyer.get_full_name()
			self.url = reverse('customer:buyerprofileview', kwargs = {'user_name': buyername})
			return super(CustomerRedirectView, self).get(request, *args, **kwargs)
		except ObjectDoesNotExist as NotaBuyer:
			try:
				maker = user.makerprofile # check this logic of adding data to self.maker
				makername = maker.get_full_name()
				self.url = reverse('customer:makerprofileview', kwargs = {'user_name': makername})
			except ObjectDoesNotExist as NotaMaker:
				messages.warning(request, 'Profile Does not Exist')
				return reverse('homepage')
		return super(CustomerRedirectView, self).get(request, *args, **kwargs)
			

class BuyerProfileView(TemplateView):
	pass

class MakerProfileView(TemplateView):
	pass
