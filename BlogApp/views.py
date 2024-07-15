from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import BlogTable



def allBlog(request):
    return render(request, 'blog-list.html')


def singleblog(request, slug):
    blogDetails = get_object_or_404(BlogTable, slug=slug)
    print(blogDetails)
    return render(request, 'blog-details.html',{"blogs" : blogDetails})




def get_blog(request, slug):
    blog = get_object_or_404(BlogTable, slug=slug)
    steps = blog.process.all()
    steps_data = [{
        "title": step.title,
        "description": step.description,
        "code": step.code,
        "image": step.image.url if step.image else None,
    } for step in steps]

    blog_data = {
        "meta_title": blog.meta_title,
        "meta_description": blog.meta_description,
        "long_description": blog.long_description,
        "code": blog.code,
        "process": steps_data,
        "image": blog.image.url if blog.image else None,
        "slug": blog.slug,
        "date_time": blog.date_time,
        "category": {
            "name": blog.category.name,
            "description": blog.category.description,
            "slug": blog.category.slug
        }
    }
    return JsonResponse(blog_data)



def get_all_blogs(request):
    blogs = BlogTable.objects.all()
    blogs_data = []

    for blog in blogs:
        steps = blog.process.all()
        steps_data = [{
            "title": step.title,
            "description": step.description,
            "code": step.code,
            "image": step.image.url if step.image else None,
        } for step in steps]

        blog_data = {
            "meta_title": blog.meta_title,
            "meta_description": blog.meta_description,
            "long_description": blog.long_description,
            "code": blog.code,
            "process": steps_data,
            "image": blog.image.url if blog.image else None,
            "slug": blog.slug,
            "date_time": blog.date_time,
            "category": {
                "name": blog.category.name,
                "description": blog.category.description,
                "slug": blog.category.slug
            }
        }
        blogs_data.append(blog_data)

    return JsonResponse(blogs_data, safe=False)

