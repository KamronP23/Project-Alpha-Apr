from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required


@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": list_projects
    }
    return render(request, "projects/list.html", context)


def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project": project,
    }
    return render(request, "projects/detail.html", context)
