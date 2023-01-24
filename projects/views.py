from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.models import Project

@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        'projects_object': projects,
    }
    return render(request, 'projects/list_projects.html', context)


@login_required
def show_project(request, id):
    projects = get_object_or_404(Project, id=id)
    context = {
        'specific_object': projects,
    }
    return render(request, 'projects/detail_view.html', context)
