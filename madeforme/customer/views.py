from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView, UpdateView, RedirectView, TemplateView

from braces.views import LoginRequiredMixin
from authtools import views as authviews

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

class ProfileUpdateView(UpdateView):
	pass

class LoginView(authviews.LoginView):
	template_name = "login.html"

class LogoutView(authviews.LogoutView):
	template_name = 'homepage.html'

class PasswordChangeView(authviews.PasswordChangeView):
	template_name = 'password_change_form.html'
	success_url = reverse_lazy('homepage')

class PasswordResetView(authviews.PasswordResetView):
	template_name = 'password_reset_form.html'
	success_url = reverse_lazy('homepage')
	subject_template_name = 'password_reset_subject.txt'
	email_template_name = 'password_reset_email.html'

	def form_valid(self,form):
		messages.success(self.request,"Your password details sent to your registered email, ""Please check")
		return super(PasswordResetView,self).form_valid(form)

class PasswordResetConfirmView(authviews.PasswordResetConfirmAndLoginView):
	template_name = 'password_reset_confirm.html'

