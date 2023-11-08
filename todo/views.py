from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import JsonResponse
from .models import Task,CustomUser,File,History
from .serializers import TaskSerializer,CustomUserSerializer,FileSerializer,HistorySerializer#,HistorySerializer2
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.

################### End point for showing all data and for creating new instances ############################
@csrf_exempt
def todo_task(request):
    if request.method=='GET':
        todo=Task.objects.all()
        serializer=TaskSerializer(todo,many=True)
        # jason_data=JSONRenderer().render(serializer.data)
        #HttpResponse(jason_data,content_type='application/json')
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        jason_data=request.body
        print(jason_data)
        stream=io.BytesIO(jason_data)
        python_data=JSONParser().parse(stream)
        creator_instance=get_object_or_404(CustomUser,username=python_data['creator']).pk
        assigner_instance=get_object_or_404(CustomUser,username=python_data['assigner']).pk
        python_data['creator']=creator_instance
        python_data['assigner']=assigner_instance
        serializer=TaskSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Data has been saved')
        else:
            return JsonResponse(serializer.errors)
@csrf_exempt
def todo_user(request):
    if request.method=="GET":
        todo=CustomUser.objects.all()
        serializer=CustomUserSerializer(todo,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        jason_data=request.body
        stream=io.BytesIO(jason_data)
        python_data=JSONParser().parse(stream)
        serializer=CustomUserSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Data has been saved')
        else:
            return JsonResponse(serializer.errors)
@csrf_exempt
def todo_file(request):
    if request.method=='GET':
        todo=File.objects.all()
        serializer=FileSerializer(todo,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        jason_data=request.body
        print(type(jason_data))
        # with open('fcc.json', 'r') as fcc_file:
        stream=io.BytesIO(jason_data)
        python_data=JSONParser().parse(request)
        task_instace=get_object_or_404(Task,name=python_data['task']).pk
        python_data['task']=task_instace
        print(python_data)
        serializer=FileSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Data has been saved')
        else:
            return JsonResponse(serializer.errors)

@csrf_exempt
def todo_history(request):
    if request.method=='GET':
        todo=History.objects.all()
        serializer=HistorySerializer(todo,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="POST":
        jason_data=request.body
        stream=io.BytesIO(jason_data)
        python_data=JSONParser().parse(stream)
        task_instance=get_object_or_404(Task,name=python_data['task']).pk
        user_instance=get_object_or_404(CustomUser,username=python_data['user']).pk
        python_data['task']=task_instance
        python_data['user']=user_instance
        serializer=HistorySerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Data has been saved')
        else:
            return JsonResponse(serializer.errors)
        
################### delete implementaion############################

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