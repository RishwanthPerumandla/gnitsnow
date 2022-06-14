from django.contrib import admin

# Register your models here.
from .models import Post, Achievement

admin.site.register(Post)
admin.site.register(Achievement)