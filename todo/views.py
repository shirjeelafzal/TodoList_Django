from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import Task,CustomUser,File,History
from .serializers import TaskSerializer,CustomUserSerializer,FileSerializer,HistorySerializer
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#end point for showing all data
def todo_task(request):
    todo=Task.objects.all()
    serializer=TaskSerializer(todo,many=True)
    # jason_data=JSONRenderer().render(serializer.data)
    #HttpResponse(jason_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)
def todo_user(request):
    todo=CustomUser.objects.all()
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

# delete implementaion
@csrf_exempt
def todo_task_id(request,pk):
    if request.method=="GET":
        data=Task.objects.get(id=pk)
        serializer=TaskSerializer(data)
        # jason_data=JSONRenderer().render(serializer.data)
        # return HttpResponse(jason_data,content_type='application/json')
        return JsonResponse(serializer.data,safe=False)
    if request.method=="DELETE":
        if Task.objects.get(id=pk):
            data=Task.objects.get(id=pk)
            data.delete()
            return redirect("/api/task")
        else:
            return HttpResponse("No data to delete")
        
#for user
@csrf_exempt
def todo_user_id(request,pk):
    if request.method=="GET":
        data=CustomUser.objects.get(id=pk)
        serializer=CustomUserSerializer(data)
        # jason_data=JSONRenderer().render(serializer.data)
        # return HttpResponse(jason_data,content_type='application/json')
        return JsonResponse(serializer.data,safe=False)
    if request.method=="DELETE":
        if CustomUser.objects.get(id=pk):
            data=CustomUser.objects.get(id=pk)
            data.delete()
            return redirect("/api/user")
        else:
            return HttpResponse("No data to delete")
#for file
@csrf_exempt
def todo_file_id(request,pk):
    if request.method=="GET":
        data=File.objects.get(id=pk)
        serializer=FileSerializer(data)
        # jason_data=JSONRenderer().render(serializer.data)
        # return HttpResponse(jason_data,content_type='application/json')
        return JsonResponse(serializer.data,safe=False)
    if request.method=="DELETE":
        if File.objects.get(id=pk):
            data=File.objects.get(id=pk)
            data.delete()
            return redirect("/api/file")
        else:
            return HttpResponse("No data to delete")
#for history
@csrf_exempt
def todo_history_id(request,pk):
    if request.method=="GET":
        data=History.objects.get(id=pk)
        serializer=HistorySerializer(data)
        return JsonResponse(serializer.data,safe=False)
    if request.method=="DELETE":
        if History.objects.get(id=pk):
            data=History.objects.get(id=pk)
            data.delete()
            return redirect("/api/history")
        else:
            return HttpResponse("No data to delete")
        



# def todo_list_pk(request,pk):
#     todo=Task.objects.get(pk)
#     serializer=TaskSerializer(todo)
#     jason_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(jason_data,content_type='application/json')