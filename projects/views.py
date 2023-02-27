from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
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


@login_required(login_url='login')
def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.profile
            project.save()
            messages.success(request, 'Project created')
            return redirect(projects)

    context = {
        'form_title': 'Create Project',
        'form': form,
    }
    return render(request, "form_template.html", context)


@login_required(login_url='login')
def update_project(request, pk):
    project = request.user.profile.project_set.get(project_id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated')
            return redirect('account')

    context = {
        'form_title': 'Update Project',
        'form': form,
    }
    return render(request, "form_template.html", context)


@login_required(login_url='login')
def delete_project(request, pk):
    project = request.user.profile.project_set.get(project_id=pk)
    context = {
        'object_type': 'project',
        'object': project
    }
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted')
        return redirect('account')
    return render(request, 'delete_template.html', context)
