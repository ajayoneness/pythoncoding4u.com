from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.


def projects(request):
    projectss = Project.objects.all()
    return render(request, 'project-list.html',{"projects":projectss})



def singleProject(request, slug):
    projectDetails = get_object_or_404(Project, slug=slug)
    # print("projetc : ",projectDetails.features.title)
    return render(request, 'project-details.html',{"projects" : projectDetails})