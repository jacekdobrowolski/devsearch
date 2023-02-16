from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from users.models import Profile
from django.shortcuts import render, redirect


def profiles(request):
    profiles_query = Profile.objects.all()
    context = {'profiles': profiles_query}
    return render(request, 'users/profiles.html', context)


@login_required(login_url='login')
def user_profile(request, pk):
    profile_query = Profile.objects.get(profile_id=pk)
    skills_with_description = profile_query.skill_set.exclude(description__exact="")
    other_skills = profile_query.skill_set.filter(description="")
    context = {
        'profile': profile_query,
        'skills_with_description': skills_with_description,
        'other_skills': other_skills,   
    }
    return render(request, 'users/user-profile.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Username does not exist')
        else:
            if user := authenticate(request, username=username, password=password):
                login(request, user)
                return redirect('profiles')
            else:
                messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def register_user(request):
    context = {}
    return render(request, 'users/login_register.html', context)
