from django.conf.urls import patterns, include, url

from .views import BuyerSignupView, MakerSignupView, CustomerRedirectView, ProfileView, ProfileUpdateView, \
LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView

# Because of strong linkages with django-authtools, template folder of this app is named registration

urlpatterns = patterns('',
    

    # Buyer and Maker signup urls
    url(r'buyer/signup/$', BuyerSignupView.as_view(), name='buyersignup'),
    url(r'maker/signup/$', MakerSignupView.as_view(), name='makersignup'),

    # Authentication urls as per django-authtools
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),
    url(r'password_change/$', PasswordChangeView.as_view(), name='passwordchange'),
    url(r'password_reset/$', PasswordResetView.as_view(), name='passwordreset'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$$', PasswordResetConfirmView.as_view(), name='passwordresetconfirm'),

    # Login redirect urls - distinguish between a buyer and a maker
    url(r'redirect/$', CustomerRedirectView.as_view(), name='customerredirect'),

    # Profile view urls for buyers and makers
    url(r'profile/(?P<user_name>\w+)/$', ProfileView.as_view(), name='profileview'),

)