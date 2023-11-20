from django.contrib import admin
from todo.models import Task ,File,History,CustomUser

@admin.register(File)
@admin.register(History)
@admin.register(CustomUser)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['id']


