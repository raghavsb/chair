from django.conf.urls import patterns, include, url

from .views import AddressTemplateView, CreateAddressView, UpdateAddressView

# Urls for buyer address management

urlpatterns = patterns('',
    
    # Buyer address management urls
    url(r'view/$', AddressTemplateView.as_view(), name='buyeraddressview'),
    url(r'create/$', CreateAddressView.as_view(), name='buyeraddresscreate'),
    url(r'update/$', UpdateAddressView.as_view(), name='buyeraddressupdate'),

)