from django.shortcuts import render
from modelFormApp.models import User 
from django.http import HttpResponse
from modelFormApp.forms import NewUserForm


# Create your views here.
def index(request):
    return render(request, 'modelFormApp/index.html')

def users(request):
    # user_list = User.objects.order_by('first_name')
    # # A way to access users
    # user_dict = {'users': user_list}
    # return render(request, 'modelFormApp/users.html', context=user_dict) 

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)

        else:
            print("Error form Invalid!")

    return render(request, 'modelFormApp/users.html', {'form': form})





