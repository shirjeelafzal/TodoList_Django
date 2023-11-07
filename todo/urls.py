from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('todo/add',views.todo_add,name='add'),
]
