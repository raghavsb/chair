from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView, UpdateView, RedirectView, TemplateView, DetailView
from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin
from authtools import views as authviews

from .forms import BuyerCreationMultiForm, MakerCreationMultiForm, BuyerProfileForm, MakerProfileForm
from .models import BuyerProfile, MakerProfile
from .mixins import CheckProfileMixin 

class BuyerProfileUpdateView(LoginRequiredMixin, UpdateView):
	"""
		Allows buyers to update the profile details, will be presented in template based on user type
	"""

	form_class = BuyerProfileForm
	template_name = 'profile_edit_form.html'
	success_message = 'Your profile has been updated'
	success_url = reverse_lazy('homepage') # change to profile detail view

	def get_object(self):
		return get_object_or_404(BuyerProfile, user = self.request.user)

	def get_context_data(self, **kwargs): # Change this to add more data to the template
		context = super(BuyerProfileUpdateView, self).get_context_data(**kwargs)
		profile = self.get_object()
		context['flag'] = profile.check_maker()
		return context

class MakerProfileUpdateView(LoginRequiredMixin, UpdateView):
	"""
		Allows maker to update the profile details, will be presented in template based on user type
	"""
	form_class = MakerProfileForm
	template_name = 'profile_edit_form.html'
	success_message = 'Your profile has been updated'
	success_url = reverse_lazy('homepage')

	def get_object(self):
		return get_object_or_404(MakerProfile, user = self.request.user)

	def get_context_data(self, **kwargs): # Change this to add more data to the template
		context = super(MakerProfileUpdateView, self).get_context_data(**kwargs)
		profile = self.get_object()
		context['flag'] = profile.check_maker()
		return context