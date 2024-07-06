from django.db import models



class ProjectCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    

# Model for Service Process
class ProjectFeatures(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    


class ProjectApplications(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    



class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    long_description = models.TextField()
    features = models.ManyToManyField(ProjectFeatures)
    Applications = models.ManyToManyField(ProjectApplications)
    youtube_link = models.URLField(blank=True, null=True)
    image_one = models.ImageField(upload_to='projects/')
    image_two = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_three = models.ImageField(upload_to='projects/', blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.meta_title
