from django.urls import path
from . import views


urlpatterns = [
    path('', views.allBlog, name="blogs"),
    path('<slug:slug>/', views.singleblog, name='single_blog'),
]

