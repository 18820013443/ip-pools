from django.urls import path, include, re_path
# from .views import GetIp

from .views import IpsView


urlpatterns = [
    re_path(r'^ip/$', IpsView.as_view())
]
