from django.urls import path, include, re_path
# from .views import GetIp

from .views import LoginView, AccountView
from rest_framework import routers


# router = routers.SimpleRouter()


urlpatterns = [
    re_path(r'^login/$', LoginView.as_view()),
    re_path(r'^register/$', AccountView.as_view())
]
