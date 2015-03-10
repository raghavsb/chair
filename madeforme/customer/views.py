from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView, UpdateView, RedirectView, TemplateView

from braces.views import LoginRequiredMixin

from .forms import BuyerCreationMultiForm, MakerCreationMultiForm
from .models import BuyerProfile, MakerProfile
from .mixins import CheckProfileMixin 

# Customer creation and login views

class BuyerSignupView(CreateView):
	form_class = BuyerCreationMultiForm
	success_url = reverse_lazy('homepage')
	template_name = 'registration.html'

class MakerSignupView(CreateView):
	form_class = MakerCreationMultiForm
	success_url = reverse_lazy('homepage')
	template_name = 'registration.html'

class CustomerRedirectView(CheckProfileMixin, RedirectView):

	def get(self, request, *args, **kwargs):
		self.url = self.get_profile_type().url
		return super(CustomerRedirectView, self).get(request, *args, **kwargs)

class ProfileView(LoginRequiredMixin, CheckProfileMixin, TemplateView):
	template_name = 'homepage.html'

	def get_context_data(self,**kwargs):
		context = super(ProfileView,self).get_context_data(**kwargs)
		profile = self.get_profile_type().profile
		context['profile'] = profile
		context['flag'] = profile.is_maker
		return context


