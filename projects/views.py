from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from projects.models import Project


def projects(request):
    projects_query = Project.objects.all()
    context = {
        'projects': projects_query,
    }
    return render(request=request,
                  template_name='projects/projects.html',
                  context=context)

def project(request, pk):
    try:
        project_query = Project.objects.get(project_id=pk)
    except Project.DoesNotExist:
        return HttpResponseNotFound()

    return render(request=request,
                template_name='projects/single-project.html',
                context={'project': project_query})
