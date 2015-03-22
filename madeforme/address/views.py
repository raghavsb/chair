from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView, UpdateView, TemplateView
from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin

from .models import BuyerAddress
from .forms import BuyerAddressForm

# Views related address management

class AddressTemplateView(LoginRequiredMixin, TemplateView):
	"""
		Displays address of the buyer or requests buyer to provide an address
	"""
	template_name = 'address_display.html' # Change later when template section is overhauled
	noaddress_message = 'No address added, please address'

	def get_context_data(self, **kwargs):
		context = super(AddressTemplateView, self).get_context_data(**kwargs)
		profile = self.request.user.buyerprofile
		try:
			address = BuyerAddress.objects.get(buyer=profile)
			context['address'] = address
			profile = self.request.user.buyerprofile
			context['makerflag'] = profile.check_maker()
			return context
		except ObjectDoesNotExist as noaddress:
			messages.success(self.request,self.noaddress_message)
			return context

class CreateAddressView(LoginRequiredMixin, CreateView):
	"""
		Create an address object for the buyer
	"""
	form_class = BuyerAddressForm
	template_name = 'profile_edit_form.html'
	success_url = reverse_lazy('homepage')

	def get_success_url(self):
		"""
			Explicit success_url method to customize the url for specific username
		"""
		return reverse('customer:profiledetail', kwargs={'user_name': self.request.user.name})

	def form_valid(self, form):
		"""
			Check for form valid and associate the existing buyer to address
		"""
		buyer = self.request.user.buyerprofile
		form.instance.buyer = buyer
		form.save()
		return super(CreateAddressView, self).form_valid(form)


class UpdateAddressView(LoginRequiredMixin, UpdateView):
	"""
		Allows buyers to update the profile address
	"""
	fields = ('address_line1','address_line2', 'landmark', 'city', 'state', 'pincode')
	template_name = 'profile_edit_form.html'
	success_message = 'Your address has been updated'

	def get_object(self):
		try:
			profile = self.request.user.buyerprofile
			address = profile.buyeraddress
			return address
		except ObjectDoesNotExist as noaddress:
			return reverse('customer:profiledetail', kwargs={'user_name': self.request.user.name})

	def get_context_data(self, **kwargs): # Change this to add more data to the template
		context = super(UpdateAddressView, self).get_context_data(**kwargs)
		return context

	def get_success_url(self):
		"""
			Explicit success_url method to customize the url for specific username
		"""
		messages.success(self.request, self.success_message)
		return reverse('customer:profiledetail', kwargs={'user_name': self.request.user.name})

