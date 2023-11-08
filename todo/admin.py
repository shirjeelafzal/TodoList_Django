from django.contrib import admin
from todo.models import Task ,File,History,CustomUser
# Register your models here.
# admin.site.register(Task)
@admin.register(File)
@admin.register(History)
@admin.register(CustomUser)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['id']
# class FileAdmin(admin.ModelAdmin):
#     list_display=['id']
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display=['id']
# class HistoryAdmin(admin.ModelAdmin):
#     list_display=['id']
# admin.site.register(File)
# admin.site.register(History)
# admin.site.register(CustomUser)

