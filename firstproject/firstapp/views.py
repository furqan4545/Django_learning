from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {
        'insert_me': "Hey Insert my data here"
    }        
    return render(request, 'firstapp/index.html', context= my_dict)
