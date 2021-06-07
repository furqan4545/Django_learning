from django.conf.urls import url, include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name = "list"),
    url(r'^create/$', views.SchoolCreateView.as_view(), name = "create"),
    # OVer here you might get an error of <Field 'id' expected a number but got 'create'>. So all you need to do is to just change the location of url line.
    # bring the line upword and try again and see it worked.
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name = "detail"),
    # OVer here we r saying grab the basic_app extension of the domain name/ and whatever number u detect over here is the primary key, grab it and take the user
    # to that specific primary key school detail. 
    # this regular expression is just being used to grab the primary key. 
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name = "update"),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name = "delete"),
]
 