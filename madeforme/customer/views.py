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

# Customer creation and login views

class BuyerSignupView(CreateView):
	"""
		Buyer registration view, uses betterforms to combine profile and user models
	"""
	form_class = BuyerCreationMultiForm
	success_url = reverse_lazy('homepage')
	template_name = 'registration.html'
	success_url = reverse_lazy('homepage')

class MakerSignupView(CreateView):
	"""
		Maker registration view, uses betterforms to combine profile and user models
	"""
	form_class = MakerCreationMultiForm
	success_url = reverse_lazy('homepage')
	template_name = 'registration.html'
	success_url = reverse_lazy('homepage')

class CustomerRedirectView(CheckProfileMixin, RedirectView):
	"""
		Provides automative redirect based on whether the logged in user is a buyer or a maker
	"""

	def get(self, request, *args, **kwargs):
		self.url = self.get_profile_type().url
		return super(CustomerRedirectView, self).get(request, *args, **kwargs)

class ProfileView(LoginRequiredMixin, CheckProfileMixin, TemplateView):
	"""
		Injects the required profile details in the templateview, users can maneuver the specific menu
	"""
	template_name = 'homepage.html'

	def get_context_data(self,**kwargs): # increase the fields added to the context - reduce database hits
		context = super(ProfileView,self).get_context_data(**kwargs)
		profile = self.get_profile_type().profile
		context['profile'] = profile
		context['flag'] = profile.is_maker
		return context

class BuyerProfileUpdateView(LoginRequiredMixin, UpdateView):
	"""
		Allows buyers to update the profile details
	"""

	form_class = BuyerProfileForm
	template_name = 'profile_edit_form.html'
	success_message = 'Your profile has been updated'
	success_url = reverse_lazy('homepage') # change to profile detail view

	def get_object(self):
		return get_object_or_404(BuyerProfile, user = self.request.user)

class MakerProfileUpdateView(LoginRequiredMixin, UpdateView): # Check if this can be transformed into a single method
	"""
		Allows maker to update the profile details
	"""
	form_class = MakerProfileForm
	template_name = 'profile_edit_form.html'
	success_message = 'Your profile has been updated'
	success_url = reverse_lazy('homepage') # change to profile detail view

	def get_object(self):
		return get_object_or_404(MakerProfile, user = self.request.user)


class ProfileDetailView(LoginRequiredMixin, CheckProfileMixin, DetailView): 
	template_name = 'test.html' #Change the template
	context_object_name = 'profile'

	def get_object(self):
		profile = self.get_profile_type().profile
		return profile

	def get_context_data(self,**kwargs):
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
		profile = self.get_profile_type().profile
		if profile.is_maker: # change the logic here
			context['name'] = profile.user.name
			context['email'] = profile.user.email
		else:
			context['name'] = profile.user.name
			context['email'] = profile.user.email
		return context


class LoginView(authviews.LoginView):
	"""
		Login for the users, uses django-authtools for low level implementation
	"""
	template_name = "login.html"

class LogoutView(authviews.LogoutView):
	"""
		Logout for the users, uses django-authtools for low level implementation
	"""
	template_name = 'homepage.html'

class PasswordChangeView(authviews.PasswordChangeView):
	"""
		Presents a form to update the password
	"""
	template_name = 'password_change_form.html'
	success_url = reverse_lazy('homepage')

class PasswordResetView(authviews.PasswordResetView):
	"""
		Sends an email to the user's registered account to process password reset
	"""
	template_name = 'password_reset_form.html'
	success_url = reverse_lazy('homepage')
	subject_template_name = 'password_reset_subject.txt'
	email_template_name = 'password_reset_email.html'

	def form_valid(self,form):
		messages.success(self.request,"Your password details sent to your registered email, ""Please check")
		return super(PasswordResetView,self).form_valid(form)

class PasswordResetConfirmView(authviews.PasswordResetConfirmAndLoginView):
	"""
		Confirms the change in password when the user clicks the link sent to the registered email
	"""
	template_name = 'password_reset_confirm.html'

