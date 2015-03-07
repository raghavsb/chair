from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

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
