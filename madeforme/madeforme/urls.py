from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .views import HomepageView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'madeforme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    # Homepage urls
    url(r'^$', HomepageView.as_view(), name='homepage'),

    # Customer urls to manage registration and update of buyer, maker profile 
    url(r'^customer/', include('customer.urls', namespace='customer')),

    # Address urls to manage buyer address management 
    url(r'^address/', include('address.urls', namespace='address')),

    # Facebook authentication
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Admin urls - default
    url(r'^admin/', include(admin.site.urls)),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
