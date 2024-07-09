from django.shortcuts import render


def allBlog(request):
    return render(request, 'blog-list.html')


def singleblog(request, slug):
    print(slug)
    return render(request, 'blog-details.html')

