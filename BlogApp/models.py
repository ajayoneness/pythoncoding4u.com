from django.db import models


# Model for Blog Category
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
    

class Steps(models.Model):
    image = models.ImageField(upload_to='blog_steps/',blank=True, null=True)
    title = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title
    


# Model for Blog
class BlogTable(models.Model):
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    long_description = models.TextField()
    code = models.TextField(blank=True, null=True)
    process = models.ManyToManyField(Steps)
    image = models.ImageField(upload_to='blogs/' ,blank=True, null=True)
    slug = models.SlugField(unique=True)
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blogs')
    conclusion = models.TextField(blank=True, null=True)  
    author = models.CharField(max_length=255, default="codeAj")

    def __str__(self):
        return self.slug