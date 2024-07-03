from django.contrib import admin
from .models import Project,ProjectCategory,ProjectFeatures,ProjectApplications

# Register your models here.

admin.site.register(ProjectCategory)
admin.site.register(Project)
admin.site.register(ProjectFeatures)
admin.site.register(ProjectApplications)