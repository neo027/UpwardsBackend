from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^customer/', include('customer.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^config/', 'configuration.urls'),
]
