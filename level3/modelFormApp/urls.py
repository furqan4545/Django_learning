from django.conf.urls import url
from modelFormApp import views

urlpatterns = [
    url(r'^$', views.users, name= 'users'),
]

