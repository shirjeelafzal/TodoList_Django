from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Task,CustomUser,File,History
from .serializers import TaskSerializer,CustomUserSerializer,FileSerializer,HistorySerializer
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
# Create your views here.

#end point for showing all data
def todo_task(request):
    todo=Task.objects.all()
    serializer=TaskSerializer(todo,many=True)
    # jason_data=JSONRenderer().render(serializer.data)
    #HttpResponse(jason_data,content_type='application/json')
    return JsonResponse(serializer.data)
def todo_user(request):
    todo=User.objects.all()
    serializer=CustomUserSerializer(todo,many=True)
    return JsonResponse(serializer.data,safe=False)

def todo_file(request):
    todo=File.objects.all()
    serializer=FileSerializer(todo,many=True)
    return JsonResponse(serializer.data,safe=False)

def todo_history(request):
    todo=History.objects.all()
    serializer=HistorySerializer(todo,many=True)
    return JsonResponse(serializer.data,safe=False)




def todo_list_pk(request,pk):
    todo=Task.objects.get(pk)
    serializer=TaskSerializer(todo)
    jason_data=JSONRenderer().render(serializer.data)
    return HttpResponse(jason_data,content_type='application/json')