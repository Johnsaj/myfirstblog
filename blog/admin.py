from django.contrib import admin

#Import the models here
from .models import Post

admin.site.register(Post)
