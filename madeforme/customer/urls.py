from django.conf.urls import patterns, include, url

from .views import BuyerSignupView, MakerSignupView, CustomerRedirectView, ProfileView

# Because of strong linkages with django-authtools, template folder of this app is named registration

urlpatterns = patterns('',
    

    # Buyer and Maker signup urls
    url(r'buyer/signup/$', BuyerSignupView.as_view(), name='buyersignup'),
    url(r'maker/signup/$', MakerSignupView.as_view(), name='makersignup'),

    # Authentication urls as per django-authtools
    url(r'^', include('authtools.urls')),

    # Login redirect urls - distinguish between a buyer and a maker
    url(r'redirect/$', CustomerRedirectView.as_view(), name='customerredirect'),

    # Profile view urls for buyers and makers
    url(r'profile/(?P<user_name>\w+)/$', ProfileView.as_view(), name='profileview'),

)