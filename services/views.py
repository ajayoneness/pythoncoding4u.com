from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Service



def allservices(request):
    return render(request, "services.html")




def service_list(request):
    if request.method == 'GET':
        services = Service.objects.all()
        data = []
        for service in services:
            data.append({
                'service_name' : service.service_name,
                'meta_title': service.meta_title,
                'meta_description': service.meta_description,
                'long_description': service.long_description,
                'process': [
                    {
                        'title': process.title,
                        'number': process.number,
                        'description': process.description,
                        'image': process.image.url if process.image else None
                    } for process in service.process.all()
                ],
                'image': service.image.url if service.image else None,
                'slug': service.slug,
            })
        return JsonResponse(data, safe=False)
    



def singleservice(request,slug):

    serviceDEtails = get_object_or_404(Service, slug=slug)
    print(serviceDEtails)
    return render(request, 'service-details.html',{"services" : serviceDEtails})





