from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Project
from django.http import JsonResponse
# Create your views here.


def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        data = []
        for project in projects:
            data.append({
                'category': project.category.name,
                'meta_title': project.meta_title,
                'meta_description': project.meta_description,
                'long_description': project.long_description,
                'features': [feature.title for feature in project.features.all()],
                'applications': [application.title for application in project.Applications.all()],
                'youtube_link': project.youtube_link,
                'image_one': project.image_one.url if project.image_one else None,
                'image_two': project.image_two.url if project.image_two else None,
                'image_three': project.image_three.url if project.image_three else None,
                'slug': project.slug,
            })
        return JsonResponse(data, safe=False)


def projects(request):
    projectss = Project.objects.all()
    return render(request, 'project-list.html',{"projects":projectss})



def singleProject(request, slug):
    projectDetails = get_object_or_404(Project, slug=slug)
    # print("projetc : ",projectDetails.features.title)
    return render(request, 'project-details.html',{"projects" : projectDetails})



def singleprojectapi(request,slug):
    projectDetails = get_object_or_404(Project, slug=slug)
    data={
                'category': projectDetails.category.name,
                'meta_title': projectDetails.meta_title,
                'meta_description': projectDetails.meta_description,
                'long_description': projectDetails.long_description,
                'features': [feature.title for feature in projectDetails.features.all()],
                'applications': [application.title for application in projectDetails.Applications.all()],
                'youtube_link': projectDetails.youtube_link,
                'image_one': projectDetails.image_one.url if projectDetails.image_one else None,
                'image_two': projectDetails.image_two.url if projectDetails.image_two else None,
                'image_three': projectDetails.image_three.url if projectDetails.image_three else None,
                'slug': projectDetails.slug,
            }
    return JsonResponse(data, safe=False)




