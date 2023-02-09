from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(projects)

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def updateProject(request, pk):
    project = Project.objects.get(project_id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(projects)

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(project_id=pk)
    context = {'object': project}
    if request.method == 'POST':
        project.delete()
        return redirect(projects)
    return render(request, 'delete_template.html', context)
