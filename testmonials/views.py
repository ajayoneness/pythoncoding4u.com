from django.shortcuts import render
from django.http import JsonResponse
from .models import Testimonial

def testimonial_list(request):
    if request.method == 'GET':
        testimonials = Testimonial.objects.all()
        data = []
        for testimonial in testimonials:
            data.append({
                'name': testimonial.name,
                'designation': testimonial.designation,
                'feedback': testimonial.feedback,
                'rating': testimonial.rating,
            })
        return JsonResponse(data, safe=False)
    
    
