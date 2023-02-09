from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from projects.models import Project
from projects.forms import ProjectForm

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


def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, "projects/project_form.html", context)
