from django.db.models import Q
from users.models import Profile, Skill


def search_profiles(search_query):
    skills = Skill.objects.filter(name__icontains=search_query)

    profiles_query = Profile.objects.distinct().filter(
        Q(name__icontains=search_query)
        | Q(short_intro__icontains=search_query)
        | Q(skills__in=skills)
    )
    return profiles_query