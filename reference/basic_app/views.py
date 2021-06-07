from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'basic_app/index.html'


class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School   
    

class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")
    model = models.School  

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    context_object_name = "school"
    model = models.School
    success_url = reverse_lazy('basic_app:list')













