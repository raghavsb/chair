from django.conf.urls import patterns, include, url
from .views import BuyerSignupView, MakerSignupView, CustomerRedirectView, BuyerProfileView, MakerProfileView

# Because of strong linkages with django-authtools, template folder of this app is named registration

urlpatterns = patterns('',
    

    # Buyer and Maker signup urls
    url(r'buyer/signup/$', BuyerSignupView.as_view(), name='buyersignup'),
    url(r'maker/signup/$', MakerSignupView.as_view(), name='makersignup'),

    # Authentication urls as per django-authtools
    url(r'', include('authtools.urls')),

    # Login redirect urls - distinguish between a buyer and a maker
    url(r'redirect/$', CustomerRedirectView.as_view(), name='customerredirect'),

    # Profile view urls for buyers and makers
    url(r'buyer/(?P<user_name>\w+)/$', BuyerProfileView.as_view(), name='buyerprofileview'),
    url(r'maker/(?P<user_name>\w+)/$', MakerProfileView.as_view(), name='makerprofileview'),

)