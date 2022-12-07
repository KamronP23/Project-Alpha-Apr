from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project


def project_list(request):
    list_projects = Project.objects.all()
    context = {
        "list_projects": list_projects
    }
    return render(request, "projects/list.html", context)

