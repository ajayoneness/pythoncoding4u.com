from django.urls import path
from . import views


urlpatterns = [
    path('', views.allservices, name="services"),
    path('service-api', views.service_list, name="serviceapi"),
    path('<slug:slug>/', views.singleservice, name='single_service'),
]

