from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django import forms

from authtools.forms import UserCreationForm
from betterforms.multiform import MultiModelForm

from .models import BuyerProfile, MakerProfile

# Forms for buyer and maker registration and profile update

class BuyerProfileForm(forms.ModelForm):
	class Meta:
		model = BuyerProfile
		fields = ('pincode',)

class MakerProfileForm(forms.ModelForm):
	class Meta:
		model = MakerProfile
		fields = ('pincode',)

class BuyerCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': UserCreationForm,
        'profile': BuyerProfileForm,
    }

    def save(self, commit=True):
        objects = super(BuyerCreationMultiForm, self).save(commit=False)

        if commit:
            user = objects['user']
            user.save()
            profile = objects['profile']
            profile.user = user
            profile.save()

        return objects

class MakerCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': UserCreationForm,
        'profile': MakerProfileForm,
    }

    def save(self, commit=True):
        objects = super(MakerCreationMultiForm, self).save(commit=False)

        if commit:
            user = objects['user']
            user.save()
            profile = objects['profile']
            profile.user = user
            profile.save()

        return objects
