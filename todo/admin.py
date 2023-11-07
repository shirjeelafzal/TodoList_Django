from django.contrib import admin
from todo.models import Task,File,History,CustomUser
# Register your models here.
admin.site.register(Task)
admin.site.register(File)
admin.site.register(History)
admin.site.register(CustomUser)

