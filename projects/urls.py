from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.projects, name="projects"),
    path('projects-api/', views.project_list, name='project-list'),
    path('<slug:slug>/', views.singleProject, name='single_project'),
    path('api/<slug:slug>/', views.singleprojectapi, name='single_project_api'),
    
]

