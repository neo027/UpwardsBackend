from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'socialLogin', views.social_login, name='socialLogin'),
    url(r'^(?P<customer_id>[0-9]+)/homepage$',
        views.homepage, name='homepage'),
    url(r'linkedin', views.linkedin, name='linkedin'),
    url(r'linkedin2', views.linkedin2, name='linkedin2'),
    url(r'config', views.config, name='config'),

]
