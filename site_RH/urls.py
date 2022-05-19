import imp
from xml.etree.ElementInclude import include

from django.urls import path
from site_RH.views import my_view

urlpatterns = [
    path('', my_view)
]
