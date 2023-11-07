from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('task',views.todo_task),
    path('user',views.todo_user),
    path('file',views.todo_file),
    path('history',views.todo_history),

    
    path('todo/<int:pk>',views.todo_list_pk,name='display'),
]
