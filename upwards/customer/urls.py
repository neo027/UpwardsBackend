from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'socialLogin', views.social_login, name='socialLogin'),
    url(r'^(?P<customer_id>[0-9]+)/homepage$',
        views.homepage, name='homepage'),
]
