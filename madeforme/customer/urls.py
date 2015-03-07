from django.conf.urls import patterns, include, url
from .views import BuyerSignupView, MakerSignupView

urlpatterns = patterns('',
    

    # Buyer and Maker signup urls
    url(r'buyer/signup/$', BuyerSignupView.as_view(), name='buyersignup'),
    url(r'maker/signup/$', MakerSignupView.as_view(), name='makersignup'),

)