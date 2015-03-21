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
		Profile page after the user signs up, this will have the account, project menu for the user to navigate
	"""
	template_name = 'homepage.html'

	def get_context_data(self, **kwargs): # Change this to add more data to the template
		context = super(ProfileView,self).get_context_data(**kwargs)
		profile = self.get_profile_type().profile
		context['profile'] = profile
		context['flag'] = profile.check_maker()
		return context

class ProfileDetailView(LoginRequiredMixin, CheckProfileMixin, DetailView): 
	"""
		Detailed fields, depending on the user type buyer or maker
	"""
	template_name = 'test.html' #Change the template
	context_object_name = 'profile'

	def get_object(self):
		profile = self.get_profile_type().profile
		return profile

	def get_context_data(self, **kwargs): # Change this to add more data to the template
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
		profile = self.get_profile_type().profile
		if profile.is_maker: # Change the logic here to inject the required data into the template
			context['name'] = profile.user.name
			context['email'] = profile.user.email
		else:
			context['name'] = profile.user.name
			context['email'] = profile.user.email
		return context

class ProfileUpdateView(LoginRequiredMixin, CheckProfileMixin, UpdateView):
	"""
		Allows buyers to update the profile details, will be presented in template based on user type
	"""
	fields = ('pincode',)
	template_name = 'profile_edit_form.html'
	success_message = 'Your profile has been updated'

	def get_object(self):
		profile = self.get_profile_type().profile
		return profile

	def get_context_data(self, **kwargs): # Change this to add more data to the template
		context = super(ProfileUpdateView, self).get_context_data(**kwargs)
		profile = self.get_profile_type().profile
		context['flag'] = profile.check_maker()
		return context

	def get_success_url(self):
		"""
			Explicit success_url method to customize the url for specific username
		"""
		messages.success(self.request, self.success_message)
		return reverse('customer:profileview', kwargs={'user_name': self.request.user.name})

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

def save_profile(strategy, details, response, user=None, *args, **kwargs):
	"""
		Update user details using the data from facebook
	"""
	if user:
		if kwargs['is_new']:
			attrs = {'user': user}
			attrs = dict(attrs.items())
			BuyerProfile.objects.create(**attrs)

