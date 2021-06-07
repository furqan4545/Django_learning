from django.conf.urls import url
from appTwo import views

urlpatterns = [
    url(r'^$', views.index, name = "index")
]
