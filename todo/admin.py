from django.contrib import admin
from.import models

# Register your models here.
@admin.register(models.Todo)
class Todoadmin(admin.ModelAdmin):
    pass
