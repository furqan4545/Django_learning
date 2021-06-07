from django.shortcuts import render
from appTwo.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    # accessing data from database or model
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'access_records' : webpages_list
    }
    return render(request, 'appTwo/index.html', context= date_dict)