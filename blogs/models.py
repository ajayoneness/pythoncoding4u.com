from django.db import models

# Create your models here.

# Model for Blog Category
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# Model for Blog
class BlogTable(models.Model):
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    long_description = models.TextField()
    code = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blogs/')
    slug = models.SlugField(unique=True)
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.meta_title