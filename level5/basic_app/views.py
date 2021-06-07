from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # Here we are hashing the passsword. 
            user.save()  # save the hash password to database.admin/

            # Now i m gonna deal with extra info i.e. profile pic and portfolio.

            profile = profile_form.save(commit = False) # commit = False means dont store info in the database right now. 
            # blc i wanna connect my 2 databases into one. so That they dont overwrite each other information
            # that's y we set one to one relationship before. So thats mean i m adding additional info to my exisiting database.
            profile.user = user  # user is the database defined above, in which we stored the information. 
            # so here we r adding extra profile attributes to the same database. i.e. doing one to one relationship blw 2 databases

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        # Here we are setting the forms again.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registeration.html', {'user_form': user_form,
                                                            'profile_form': profile_form,
                                                            'registered': registered
                                                            })



###############################################################################
# From here creating login view

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password) # this will automatically authenticate user for u. 

        if user:
            if user.is_active:
                login(request, user) # this will automatically logged in the user. 
                return HttpResponseRedirect(reverse('index'))  # this is used for redirecting the user to another page. 
                # if the user is active and logged in. the above line will redirect him to the homepage. 

            else: # if the user is not active 
                return HttpResponse("ACCOUNT NOT ACTIVE") # This will simply give us a message. 
            
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'basic_app/login.html', {})

@login_required
def special(request):
    return HttpResponse("You are logged in , Nice!")




@login_required
def user_logout(request):
    logout(request) # this function automatically logs out the user. 
    return HttpResponseRedirect(reverse('index'))  # redirect the user to index page. 

    # here in order to logout the user needs to login. blc if the user clicks logout without first loggin in. the app will throw errors.
    # so for this we simply add django decorator above the function name @login_required
 










