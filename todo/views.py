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
        
################### delete implementaion+updting############################

@csrf_exempt
def todo_task_id(request,pk):
    if request.method=="GET":
        data=Task.objects.get(id=pk)
        serializer=TaskSerializer(data)
        # jason_data=JSONRenderer().render(serializer.data)
        # return HttpResponse(jason_data,content_type='application/json')
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="DELETE":
        if Task.objects.get(id=pk):
            data=Task.objects.get(id=pk)
            data.delete()
            return redirect("/api/task")
        else:
            return HttpResponse("No data to delete")
    elif request.method=="PATCH":
        data=Task.objects.get(id=pk)
        jason_data=request.body
        stream=io.BytesIO(jason_data)
        python_data=JSONParser().parse(stream)
        if 'name' in python_data:
            data.name = python_data['name']
        if 'description' in python_data:
            data.description = python_data['description']
        if 'status' in python_data:
            data.status = python_data['status']
        if 'priority' in python_data:
            data.priority = python_data['priority']
        if 'deadline' in python_data:
            data.deadline = python_data['deadline']
        if 'start' in python_data:
            data.start = python_data['start']
        if 'tag' in python_data:
            data.tag = python_data['tag']
        
        if 'assigner' in python_data:
            assigner_instance = get_object_or_404(CustomUser, username=python_data['assigner'])
            data.assigner =assigner_instance 
        if 'creator' in python_data:
            creator_instance = get_object_or_404(CustomUser, username=python_data['creator'])
            data.creator = creator_instance
        data.save()
        return HttpResponse("Data has been updated") 
    elif request.method=="PUT":
        data=Task.objects.get(id=pk)
        jason_data=request.body
        stream=io.BytesIO(jason_data)
        python_data=JSONParser().parse(stream)

        required_keys = ['name', 'description', 'status', 'priority', 'deadline', 'start', 'tag', 'creator', 'assigner']
        for key in required_keys:
            if key not in python_data:
                return HttpResponse('All fields are not provided')

        data.name = python_data['name']
        data.description = python_data['description']
        data.status = python_data['status']
        data.priority = python_data['priority']
        data.deadline = python_data['deadline']
        data.start = python_data['start']
        data.tag = python_data['tag']
        assigner_instance = get_object_or_404(CustomUser, username=python_data['assigner'])
        data.assigner =assigner_instance 
        creator_instance = get_object_or_404(CustomUser, username=python_data['creator'])
        data.creator = creator_instance
        data.save()
        return HttpResponse("Data has been updated") 
        
#for user
@csrf_exempt
def todo_user_id(request,pk):
    if request.method=="GET":
        data=CustomUser.objects.get(id=pk)
        serializer=CustomUserSerializer(data)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="DELETE":
        if CustomUser.objects.get(id=pk):
            data=CustomUser.objects.get(id=pk)
            data.delete()
            return redirect("/api/user")
        else:
            return HttpResponse("No data to delete")
    elif request.method=="PATCH":
        data=CustomUser.objects.get(id=pk)
        jason_data=request.body
        stream=io.BytesIO(jason_data)
        python_data=JSONParser().parse(stream)
        
        if 'password' in python_data:
            data.password=python_data['password']          
        if 'username' in python_data:
            data.username=python_data['username']
        if 'datejoined' in python_data:
            data.Desciption_change = python_data['datejoined']
        if 'view' in python_data:
            data.view=python_data['view']
        if 'edit' in python_data:
            data.view=python_data['edit']
        if 'is_staff' in python_data:
            data.view=python_data['is_staff']
        if 'is_active' in python_data:
            data.view=python_data['is_active']
        if 'is_superuser' in python_data:
            data.view=python_data['is_superuser']
        if 'first_name' in python_data:
            data.first_name=python_data['first_name']
        if 'last_name' in python_data:
            data.first_name=python_data['last_name']
        if 'email' in python_data:
            data.first_name=python_data['email']
        
        data.save()
        return HttpResponse("Data has been updated") 
    elif request.method=="PUT":
        data=CustomUser.objects.get(id=pk)
        jason_data=request.body
        stream=io.BytesIO(jason_data)
        python_data=JSONParser().parse(stream)
        print(python_data)
        required_keys = ['first_name','last_name','email','password', 'username', 'datejoined', 'view', 'edit', 'is_staff', 'is_active', 'is_superuser']
        for key in required_keys:
            if key not in python_data:
                return HttpResponse('All fields are not provided')
        data.password=python_data['password']          
        data.username=python_data['username']
        data.Desciption_change = python_data['datejoined']
        data.view=python_data['view']
        data.view=python_data['edit']
        data.view=python_data['is_staff']
        data.view=python_data['is_active']
        data.view=python_data['is_superuser']
        data.first_name=python_data['first_name']
        data.first_name=python_data['last_name']
        data.first_name=python_data['email']
        data.save()
        return HttpResponse("Data has been updated")
#for file
@csrf_exempt
def todo_file_id(request,pk):
    if request.method=="GET":
        data=File.objects.get(id=pk)
        serializer=FileSerializer(data)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="DELETE":
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
    elif request.method=="DELETE":
        if History.objects.get(id=pk):
            data=History.objects.get(id=pk)
            data.delete()
            return redirect("/api/history")
        else:
            return HttpResponse("No data to delete")
    elif request.method=="PATCH":
        data=History.objects.get(id=pk)
        jason_data=request.body
        stream=io.BytesIO(jason_data)
        python_data=JSONParser().parse(stream)
        
        if 'task' in python_data:
            task_instance = get_object_or_404(Task, name=python_data['task'])
            data.task = task_instance
        if 'user' in python_data:
            user_instance = get_object_or_404(CustomUser, username=python_data['user'])
            data.user = user_instance
        if 'Desciption_change' in python_data:
            data.Desciption_change = python_data['Desciption_change']
        if 'time' in python_data:
            data.time = python_data['time']
        data.save()
        return HttpResponse("Data has been updated") 
    elif request.method=="PUT":
        data=History.objects.get(id=pk)
        jason_data=request.body
        stream=io.BytesIO(jason_data)
        python_data=JSONParser().parse(stream)
        if 'task' not in python_data or 'user' not in python_data or 'Desciption_change' not in python_data or 'time' not in python_data:
            return HttpResponse("All fields are not provided")


        task_instance = get_object_or_404(Task, name=python_data['task'])
        data.task = task_instance
        user_instance = get_object_or_404(CustomUser, username=python_data['user'])
        data.user = user_instance
        data.Desciption_change = python_data['Desciption_change']
        data.time = python_data['time']
        data.save()
        return HttpResponse("Data has been updated") 

