from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name="projects"),
     path('<slug:slug>/', views.singleProject, name='single_project'),
]

