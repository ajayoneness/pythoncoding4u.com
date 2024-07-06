from django.db import models



# Model for Service Process
class ServiceProcess(models.Model):
    image = models.ImageField(upload_to='service_process/')
    title = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    description = models.TextField()
    top_tag = models.TextField(default="")
    bottom_tag = models.TextField(default="")


    def __str__(self):
        return self.title



# Model for Service
class Service(models.Model):
    service_name = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=555)
    meta_description = models.TextField()
    long_description = models.TextField()
    process = models.ManyToManyField(ServiceProcess)
    image = models.ImageField(upload_to='services/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.meta_title
