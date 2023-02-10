from django.shortcuts import render
from users.models import Profile

# Create your views here.
def profiles(request):
    profiles_query = Profile.objects.all()
    context = {'profiles': profiles_query}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile_query = Profile.objects.get(profile_id=pk)
    skills_with_description = profile_query.skill_set.exclude(description__exact="")
    other_skills = profile_query.skill_set.filter(description="")
    context = {
        'profile': profile_query,
        'skills_with_description': skills_with_description,
        'other_skills': other_skills,   
    }
    return render(request, 'users/user-profile.html', context)
