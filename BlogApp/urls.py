from django.urls import path
from . import views


urlpatterns = [
    path('api/<slug:slug>/', views.get_blog, name='get_blog'),
    path('blogapi/', views.get_all_blogs, name='blogapi'),
    path('', views.allBlog, name="blogs"),
    path('<slug:slug>/', views.singleblog, name='single_blog'),
     
]

