from django.shortcuts import render, redirect
from .forms import UserProfileForm, UserForm, LoginForm
from django.contrib.auth.models import User
# login imports
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, "userApp/home.html")


def register(request):
    form_user = UserForm(request.POST or None)
    # form_profile = UserProfileForm(request.POST or None)

    if form_user.is_valid():  # and form_profile.is_valid():
        user = form_user.save()

        #profile = form_profile.save(commit=False)
        #profile.user = user

        # if 'profile_pic' in request.FILES:
        #     profile.profile_pic = request.FILES['profile_pic']
        # profile.save()
        messages.success(request, "Register successful")
        return redirect('home')
    context = {
        # 'form_profile': form_profile,
        'form_user': form_user
    }
    return render(request, 'userApp/register.html', context)
