from django.conf.urls import url

from .views import *

urlpatterns = [
    url('^$', index, name='index'),
]
