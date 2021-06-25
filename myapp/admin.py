from django.contrib import admin
from myapp import models

# Register your models here.
admin.site.register(models.Topic)
admin.site.register(models.Webpage)
