from django.shortcuts import render, redirect
from .models import *
from .forms import ProjectForm

# Create your views here.

def projects(request):
    reviews_p = Review.objects.filter(value='yaxshi')
    review_m = Review.objects.filter(value='yomon')
    projects = Project.objects.filter(project_review__isnull=True)
    context = {
        "projects": projects,
        'review_m': review_m,
        'reviews_p': reviews_p
    }
    return render(request, "projects.html", context)


def project(request,id):
    project = Project.objects.get(id=id)
    tags = project.tag.all()
    context = {
        'project': project,
        'tags': tags
    }
    return render(request, 'project.html', context)


def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm()
    context = {
        'form': form
    }
    return render(request, 'project_add.html', context)


def project_edit(request):
    context = {

    }
    return render(request, 'project_edit.html', context)

