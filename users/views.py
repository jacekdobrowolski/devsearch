from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from users.models import Profile
from users.forms import CustomUserCreationForm, ProfileForm, SkillForm
from search_profiles import search_profiles


def profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    context = {
        'profiles': search_profiles(search_query),
        'search_query': search_query
    }
    return render(request, 'users/profiles.html', context)


@login_required(login_url='login')
def user_profile(request, pk):
    profile_query = Profile.objects.get(profile_id=pk)
    context = {
        'profile': profile_query,
        'skills_with_description': profile_query.skill_set.exclude(description__exact=""),
        'other_skills': profile_query.skill_set.filter(description=""),
    }
    return render(request, 'users/user_profile.html', context)


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

    return render(request, 'users/login_register.html', context={'page': 'login'})


def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def register_user(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            login(user)
            return redirect('edit-profile')
        else:
            messages.error(request, 'An error has occurred during registration')

    context = {
        'page': 'register',
        'form': form
    }
    return render(request, 'users/login_register.html', context)


@login_required(login_url='login')
def user_account(request):
    context = {
        'profile': request.user.profile,
        'skills': request.user.profile.skill_set.all(),
        'projects': request.user.profile.project_set.all(),
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated')
            return redirect('account')
    context = {
        'form_title': 'Update Account',
        'form': ProfileForm(instance=request.user.profile)
    }
    return render(request, 'form_template.html', context)


@login_required(login_url='login')
def create_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user.profile
            form.save()
            messages.success(request, 'Skill added')
            return redirect('account')

    context={
        'form_title': 'Add Skill',
        'form': SkillForm(),
        }
    return render(request, 'form_template.html', context)


@login_required(login_url='login')
def update_skill(request, pk):
    skill = request.user.profile.skill_set.get(skill_id=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated')
            return redirect('account')

    context={
        'form_title': 'Update Skill',
        'form': form,
        }
    return render(request, 'form_template.html', context)


@login_required(login_url='login')
def delete_skill(request, pk):
    skill = request.user.profile.skill_set.get(skill_id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted')
        return redirect('account')

    context = {
        'object_type': 'skill',
        'object': skill
    }
    return render(request, 'delete_template.html', context)
