from django.shortcuts import render
from .forms import user_info_form,profile_info_form
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    registered = False
    if request.method == "POST":
        user_form = user_info_form(request.POST)
        profile_form = profile_info_form(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = user_info_form()
        profile_form = profile_info_form()
    my_dict = {'user_form':user_form,'profile_form':profile_form,'registered':registered}
    return render(request,'basic_app/registration.html',context=my_dict)



@login_required
def special(request):
    return HttpResponse('YOU ARE LOGGED IN ')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("SOMEONE TRIED TO LOGIN AND FAILED")
            print("USERNAME : {} and password : {}".format(username,password))

    else:
        return render(request,'basic_app/login.html')
