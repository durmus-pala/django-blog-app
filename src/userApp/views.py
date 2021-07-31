from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm, UserForm, LoginForm
from django.contrib.auth.models import User
from .models import UserProfile
# login imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


@login_required
def profile(request):
    user = request.user
    # profile = UserProfile.objects.get(user=user.id)
    # aşağıdaki şekilde yapmak daha doğru. yukardaki şekilde arama yapınca DB'de bulamazsa app çöker
    profile = get_object_or_404(UserProfile, user=user.id)
    content = {
        'profile': profile
    }
    return render(request, 'userApp/profile.html', content)


def register(request):
    form_user = UserForm(request.POST or None)
    form_profile = UserProfileForm(request.POST or None)

    if form_user.is_valid() and form_profile.is_valid():
        user = form_user.save()

        profile = form_profile.save(commit=False)
        profile.user = user

        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']
        profile.save()
        messages.success(request, "Register successful")
        return redirect('home')
    context = {
        'form_profile': form_profile,
        'form_user': form_user
    }
    return render(request, 'userApp/register.html', context)


@login_required
def user_logout(request):
    messages.success(request, "You Logout Succesfully!")
    logout(request)
    return redirect('home')


def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                messages.success(request, "Login successfully")
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Account is not active")
                return render(request, 'userApp/user_login.html', {"form": form})
        else:
            messages.error(request, "Password or Username is wrong!")
            return render(request, 'userApp/user_login.html', {"form": form})
    return render(request, 'userApp/user_login.html', {"form": form})
