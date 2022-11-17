from django.contrib import admin
from .models import Superhero, Article, Photo
# Register your models here.
admin.site.register(Superhero)
admin.site.register(Article)
admin.site.register(Photo)
