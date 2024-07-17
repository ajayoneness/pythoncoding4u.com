from django.contrib import admin
from .models import BlogCategory, BlogTable, Steps


admin.site.register(BlogTable)
admin.site.register(BlogCategory)
admin.site.register(Steps)
