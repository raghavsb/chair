from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, RedirectView, TemplateView

from .forms import BuyerCreationMultiForm, MakerCreationMultiForm

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
			buyer = user.buyerprofile
			buyername = buyer.get_full_name()
			self.url = reverse('customer:buyerprofileview', kwargs = {'user_name': buyername})
		except user.RelatedObjectDoesNotExist as NotaBuyer:
			maker = user.makeprofile
			makername = maker.get_full_name()
			self.url = reverse('customer:makerprofileview', kwargs = {'user_name': makername})

class BuyerProfileView(TemplateView):
	pass

class MakerProfileView(TemplateView):
	pass
