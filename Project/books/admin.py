from django.contrib import admin
from . import models


#if from .models import Book
admin.site.register(models.Book)  #then Book
admin.site.register(models.Author)
admin.site.register(models.Publisher)





