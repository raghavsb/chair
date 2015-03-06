from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomepageView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'madeforme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    # Homepage urls
    url(r'^$', HomepageView.as_view(), name='homepage'),

    # Authentication urls as per django-authtools
    url(r'^accounts/', include('authtools.urls')),

    # Admin urls - default
    url(r'^admin/', include(admin.site.urls)),
)
