from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Forum)
admin.site.register(models.Discussion)
