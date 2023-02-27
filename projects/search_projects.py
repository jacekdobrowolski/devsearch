from django.db.models import Q
from projects.models import Project, Tag


def search_projects(search_query):
    tags = Tag.objects.filter(name__icontains=search_query)

    return Project.objects.distinct().filter(
        Q(title__icontains=search_query)
        | Q(description__icontains=search_query)
        | Q(owner__name__icontains=search_query)
        | Q(tags__in=tags)
    )