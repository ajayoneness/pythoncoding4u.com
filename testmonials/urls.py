from django.urls import path
from . import views


urlpatterns = [
    path('testmonail-list-api', views.testimonial_list, name="testimonial_lists"),
]

