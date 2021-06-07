from django.shortcuts import render
# from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import View, CreateView, UpdateView, DeleteView
from . import models  # . mean look in the current directory. 
from django.urls import reverse_lazy 

# Create your views here.
# Now we will explore template based Views Here.

class IndexView(TemplateView):
    template_name = "index.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)  # Just copy and paste this line. 
    #     # this is how u can use context in class based views. Context is basically template injection in index.html file.  
    #     context["injectme"] = "Basic Injection!"
    #     return context


#####################

# From Here we will talk about list view and Detail view. So far we have seen views and TemplateView.  
# For this first of all we need to create models. lets jump to model.py file

# I m gonna create a list view which is connected to a model. and it will fetch data from the model. 
class SchoolListView(ListView):
    # model = models.School
    # that's all u need  to do and u will be provided with a list of records stored in the school model(db)
    # it returns a list with the name school_list i.e. <MODEL_NAME>_list.
    # apart of this u can define your own context name i.e. 

    context_object_name = 'schools'
    model = models.School

# Now let's see what a detail view looks like. 
# Let's do the same thing for this class 
# Detail View
class SchoolDetailView(DetailView):
    # Note: DetialView class returns only model name lowercased.
    context_object_name = "school_detail"
    model = models.School
    # so here it will return school just.
    template_name = 'basic_app/school_detail.html'

# Create View
class SchoolCreateView(CreateView):
    # fields -> overhere we will define the fields that we will allow user to create.i.e. the fields that are defined in the database we need to create here as well.
    fields = ('name', 'principal', 'location')
    model = models.School

# Update View
class SchoolUpdateView(UpdateView):
    # again we will specify which fields you want to update. so below I m just changing school name and principal of school but not location.
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    # This is going to be slghtly different than the other views we created so far. 
    model = models.School
    success_url = reverse_lazy("basic_app:list") # list is the name of my view.