from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.startpage, name='startpage'),
    url(r'startinfo', views.startinfo, name='startinfo')
    ]
