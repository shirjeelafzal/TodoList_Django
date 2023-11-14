


import os
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from drf_yasg.utils import swagger_auto_schema

from .models import Task,CustomUser,File,History
from .serializers import TaskSerializer,CustomUserSerializer,FileSerializer,HistorySerializer#,HistorySerializer2
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import status, parsers, renderers
import json
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter


# Create your views here.

################### End point for showing all data and for creating new instances ############################
# @csrf_exempt
# def todo_task(request):
#     if request.method=='GET':
#         todo=Task.objects.all()
#         serializer=TaskSerializer(todo,many=True)
#         # jason_data=JSONRenderer().render(serializer.data)
#         #HttpResponse(jason_data,content_type='application/json')
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method=='POST':
#         jason_data=request.body
#         print(jason_data)
#         stream=io.BytesIO(jason_data)
#         python_data=JSONParser().parse(stream)
#         creator_instance=get_object_or_404(CustomUser,username=python_data['creator']).pk
#         assigner_instance=get_object_or_404(CustomUser,username=python_data['assigner']).pk
#         python_data['creator']=creator_instance
#         python_data['assigner']=assigner_instance
#         serializer=TaskSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse('Data has been saved')
#         else:
#             return JsonResponse(serializer.errors)
# @csrf_exempt
# def todo_user(request):
#     if request.method=="GET":
#         todo=CustomUser.objects.all()
#         serializer=CustomUserSerializer(todo,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method=='POST':
#         jason_data=request.body
#         stream=io.BytesIO(jason_data)
#         python_data=JSONParser().parse(stream)
#         serializer=CustomUserSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse('Data has been saved')
#         else:
#             return JsonResponse(serializer.errors)
# @csrf_exempt
# def todo_file(request):
#     if request.method=='GET':
#         todo=File.objects.all()
#         serializer=FileSerializer(todo,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method=='POST':
#         file=request.FILES.get('files')
#         task_name=request.POST['task']
#         # mu_var=task_name
#         try:
#             task_instance = get_object_or_404(Task, name=task_name)
#             pdf_file_instance = File.objects.create(files=file,task=task_instance)
#             return JsonResponse('Data has been stroed',safe=False)
#         except Exception as e:
#             return HttpResponseServerError(f"Error uploading the file: {str(e)}")
#
#
#
#
# @csrf_exempt
# def todo_history(request):
#     if request.method=='GET':
#         todo=History.objects.all()
#         serializer=HistorySerializer(todo,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method=="POST":
#         jason_data=request.body
#         stream=io.BytesIO(jason_data)
#         python_data=JSONParser().parse(stream)
#         task_instance=get_object_or_404(Task,name=python_data['task']).pk
#         user_instance=get_object_or_404(CustomUser,username=python_data['user']).pk
#         python_data['task']=task_instance
#         python_data['user']=user_instance
#         serializer=HistorySerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse('Data has been saved')
#         else:
#             return JsonResponse(serializer.errors)
#
# ################### delete implementaion+updting############################
#
# @csrf_exempt
# def todo_task_id(request,pk):
#     if request.method=="GET":
#         data=Task.objects.get(id=pk)
#         serializer=TaskSerializer(data)
#         # jason_data=JSONRenderer().render(serializer.data)
#         # return HttpResponse(jason_data,content_type='application/json')
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method=="DELETE":
#         if Task.objects.get(id=pk):
#             data=Task.objects.get(id=pk)
#             data.delete()
#             return redirect("/api/task")
#         else:
#             return HttpResponse("No data to delete")
#     elif request.method=="PATCH":
#         data=Task.objects.get(id=pk)
#         jason_data=request.body
#         stream=io.BytesIO(jason_data)
#         python_data=JSONParser().parse(stream)
#         if 'name' in python_data:
#             data.name = python_data['name']
#         if 'description' in python_data:
#             data.description = python_data['description']
#         if 'status' in python_data:
#             data.status = python_data['status']
#         if 'priority' in python_data:
#             data.priority = python_data['priority']
#         if 'deadline' in python_data:
#             data.deadline = python_data['deadline']
#         if 'start' in python_data:
#             data.start = python_data['start']
#         if 'tag' in python_data:
#             data.tag = python_data['tag']
#
#         if 'assigner' in python_data:
#             assigner_instance = get_object_or_404(CustomUser, username=python_data['assigner'])
#             data.assigner =assigner_instance
#         if 'creator' in python_data:
#             creator_instance = get_object_or_404(CustomUser, username=python_data['creator'])
#             data.creator = creator_instance
#         data.save()
#         return HttpResponse("Data has been updated")
#     elif request.method=="PUT":
#         data=Task.objects.get(id=pk)
#         jason_data=request.body
#         stream=io.BytesIO(jason_data)
#         python_data=JSONParser().parse(stream)
#
#         required_keys = ['name', 'description', 'status', 'priority', 'deadline', 'start', 'tag', 'creator', 'assigner']
#         for key in required_keys:
#             if key not in python_data:
#                 return HttpResponse('All fields are not provided')
#
#         data.name = python_data['name']
#         data.description = python_data['description']
#         data.status = python_data['status']
#         data.priority = python_data['priority']
#         data.deadline = python_data['deadline']
#         data.start = python_data['start']
#         data.tag = python_data['tag']
#         assigner_instance = get_object_or_404(CustomUser, username=python_data['assigner'])
#         data.assigner =assigner_instance
#         creator_instance = get_object_or_404(CustomUser, username=python_data['creator'])
#         data.creator = creator_instance
#         data.save()
#         return HttpResponse("Data has been updated")
#
# #for user
# @csrf_exempt
# def todo_user_id(request,pk):
#     if request.method=="GET":
#         data=CustomUser.objects.get(id=pk)
#         serializer=CustomUserSerializer(data)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method=="DELETE":
#         if CustomUser.objects.get(id=pk):
#             data=CustomUser.objects.get(id=pk)
#             data.delete()
#             return redirect("/api/user")
#         else:
#             return HttpResponse("No data to delete")
#     elif request.method=="PATCH":
#         data=CustomUser.objects.get(id=pk)
#         jason_data=request.body
#         stream=io.BytesIO(jason_data)
#         python_data=JSONParser().parse(stream)
#
#         if 'password' in python_data:
#             data.password=python_data['password']
#         if 'username' in python_data:
#             data.username=python_data['username']
#         if 'datejoined' in python_data:
#             data.Desciption_change = python_data['datejoined']
#         if 'view' in python_data:
#             data.view=python_data['view']
#         if 'edit' in python_data:
#             data.view=python_data['edit']
#         if 'is_staff' in python_data:
#             data.view=python_data['is_staff']
#         if 'is_active' in python_data:
#             data.view=python_data['is_active']
#         if 'is_superuser' in python_data:
#             data.view=python_data['is_superuser']
#         if 'first_name' in python_data:
#             data.first_name=python_data['first_name']
#         if 'last_name' in python_data:
#             data.first_name=python_data['last_name']
#         if 'email' in python_data:
#             data.first_name=python_data['email']
#
#         data.save()
#         return HttpResponse("Data has been updated")
#     elif request.method=="PUT":
#         data=CustomUser.objects.get(id=pk)
#         jason_data=request.body
#         stream=io.BytesIO(jason_data)
#         python_data=JSONParser().parse(stream)
#         print(python_data)
#         required_keys = ['first_name','last_name','email','password', 'username', 'datejoined', 'view', 'edit', 'is_staff', 'is_active', 'is_superuser']
#         for key in required_keys:
#             if key not in python_data:
#                 return HttpResponse('All fields are not provided')
#         data.password=python_data['password']
#         data.username=python_data['username']
#         data.Desciption_change = python_data['datejoined']
#         data.view=python_data['view']
#         data.view=python_data['edit']
#         data.view=python_data['is_staff']
#         data.view=python_data['is_active']
#         data.view=python_data['is_superuser']
#         data.first_name=python_data['first_name']
#         data.first_name=python_data['last_name']
#         data.first_name=python_data['email']
#         data.save()
#         return HttpResponse("Data has been updated")
# #for file
# @csrf_exempt
# def todo_file_id(request,pk):
#     if request.method=="GET":
#         data=File.objects.get(id=pk)
#         serializer=FileSerializer(data)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method=="DELETE":
#         if File.objects.get(id=pk):
#             data=File.objects.get(id=pk)
#             data.delete()
#             return redirect("/api/file")
#         else:
#             return HttpResponse("No data to delete")
#     elif request.method=='PATCH':
#         current_instance = File.objects.get(id=pk)
#         if request.content_type.startswith('multipart'):
#             task_name, files = request.parse_file_upload(request.META, request)
#             if len(task_name) == 0:
#                 request.FILES.update(files)
#                 file = request.FILES['files']
#                 current_instance.files = file
#                 current_instance.save()
#                 return JsonResponse('Data has been strored', safe=False)
#             elif len(files) == 0:
#                 taskname=task_name['task']
#                 task_instance = get_object_or_404(Task, name=taskname)
#                 current_instance.task = task_instance
#                 current_instance.save()
#                 return JsonResponse('Data has been strored', safe=False)
#             else:
#                 request.FILES.update(files)
#                 file = request.FILES['files']
#                 current_instance.files = file
#                 taskname = task_name['task']
#                 task_instance = get_object_or_404(Task, name=taskname)
#                 current_instance.task = task_instance
#                 current_instance.save()
#                 return JsonResponse('Data has been strored', safe=False)
#         else:
#             return JsonResponse('Data sent is incorrect', safe=False)
#     elif request.method=='PUT':
#         current_instance = File.objects.get(id=pk)
#         if request.content_type.startswith('multipart'):
#             task_name, files = request.parse_file_upload(request.META, request)
#             if len(task_name)==0 or len(files)==0:
#                 return JsonResponse('All fields are not entered', safe=False)
#             request.FILES.update(files)
#             file = request.FILES['files']
#             taskname = task_name['task']
#             task_instance = get_object_or_404(Task, name=taskname)
#             current_instance.files=file
#             current_instance.task=task_instance
#             current_instance.save()
#             return JsonResponse('Data has been strored', safe=False)
#         else:
#             return JsonResponse('Data sent is incorrect', safe=False)
#
#
# #for history
# @csrf_exempt
# def todo_history_id(request,pk):
#     if request.method=="GET":
#         data=History.objects.get(id=pk)
#         serializer=HistorySerializer(data)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method=="DELETE":
#         if History.objects.get(id=pk):
#             data=History.objects.get(id=pk)
#             data.delete()
#             return redirect("/api/history")
#         else:
#             return HttpResponse("No data to delete")
#     elif request.method=="PATCH":
#         data=History.objects.get(id=pk)
#         jason_data=request.body
#         stream=io.BytesIO(jason_data)
#         python_data=JSONParser().parse(stream)
#
#         if 'task' in python_data:
#             task_instance = get_object_or_404(Task, name=python_data['task'])
#             data.task = task_instance
#         if 'user' in python_data:
#             user_instance = get_object_or_404(CustomUser, username=python_data['user'])
#             data.user = user_instance
#         if 'Desciption_change' in python_data:
#             data.Desciption_change = python_data['Desciption_change']
#         if 'time' in python_data:
#             data.time = python_data['time']
#         data.save()
#         return HttpResponse("Data has been updated")
#     elif request.method=="PUT":
#         data=History.objects.get(id=pk)
#         jason_data=request.body
#         stream=io.BytesIO(jason_data)
#         python_data=JSONParser().parse(stream)
#         if 'task' not in python_data or 'user' not in python_data or 'Desciption_change' not in python_data or 'time' not in python_data:
#             return HttpResponse("All fields are not provided")
#
#
#         task_instance = get_object_or_404(Task, name=python_data['task'])
#         data.task = task_instance
#         user_instance = get_object_or_404(CustomUser, username=python_data['user'])
#         data.user = user_instance
#         data.Desciption_change = python_data['Desciption_change']
#         data.time = python_data['time']
#         data.save()
#         return HttpResponse("Data has been updated")
#

@extend_schema(responses=TaskSerializer)
class TaskViewSet(viewsets.ViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    def list(self,request):
        if Task.objects.all():
            queryset = Task.objects.all()
            serializer=TaskSerializer(self.queryset,many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "No data available"}, status=status.HTTP_404_NOT_FOUND)
    def retrieve(self,request,pk=None):
        viewset = Task.objects.get(id=pk)
        serializer=TaskSerializer(viewset)
        return Response(serializer.data)
    def destroy(self, request, pk=None):
        obj=Task.objects.get(id=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        item = get_object_or_404(Task.objects.all(), pk=pk)
        serializer = TaskSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        item=get_object_or_404(Task.objects.all(),pk=pk)
        serializer=TaskSerializer(item,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(responses=CustomUserSerializer)
class UserViewSet(viewsets.ViewSet):
    serializer_class = CustomUserSerializer()
    queryset = CustomUser.objects.all()
    def list(self,request):
        if CustomUser.objects.all():
            queryset = CustomUser.objects.all()
            serializer=CustomUserSerializer(self.queryset,many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "No data available"}, status=status.HTTP_404_NOT_FOUND)
    def retrieve(self,request,pk=None):
        viewset = CustomUser.objects.get(id=pk)
        serializer=CustomUserSerializer(viewset)
        return Response(serializer.data)
    def destroy(self, request, pk=None):
        obj=CustomUser.objects.get(id=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        item = get_object_or_404(CustomUser.objects.all(), pk=pk)
        serializer = CustomUserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        item=get_object_or_404(CustomUser.objects.all(),pk=pk)
        serializer=CustomUserSerializer(item,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(responses=HistorySerializer)
class HistoryViewSet(viewsets.ViewSet):
    serializer_class = HistorySerializer()
    queryset = History.objects.all()
    def list(self,request):
        if History.objects.all():
            queryset = History.objects.all()
            serializer=HistorySerializer(self.queryset,many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "No data available"}, status=status.HTTP_404_NOT_FOUND)
    def retrieve(self,request,pk=None):
        viewset = History.objects.get(id=pk)
        serializer=HistorySerializer(viewset)
        return Response(serializer.data)
    def destroy(self, request, pk=None):
        obj=History.objects.get(id=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        serializer = HistorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        item = get_object_or_404(History.objects.all(), pk=pk)
        serializer = HistorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        item=get_object_or_404(History.objects.all(),pk=pk)
        serializer=HistorySerializer(item,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@extend_schema(responses=FileSerializer)
class FileViewSet(viewsets.ViewSet):
    ##testing for file upload
    # throttle_classes = ()
    # permission_classes = ()
    # parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    # renderer_classes = (renderers.JSONRenderer,
    serializer_class = FileSerializer()
    queryset = File.objects.all()
    def list(self,request):
        if File.objects.all():
            queryset = File.objects.all()
            serializer=FileSerializer(self.queryset,many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "No data available"}, status=status.HTTP_404_NOT_FOUND)
    def retrieve(self,request,pk=None):
        viewset = File.objects.get(id=pk)
        serializer=FileSerializer(viewset)
        return Response(serializer.data)
    def destroy(self, request, pk=None):
        obj=File.objects.get(id=pk)
        obj.delete()
        return Response({"detail": "Data has been deleted"},status=status.HTTP_204_NO_CONTENT)

    #
    @swagger_auto_schema(
        request_body=None,  # Since it's a file upload, the body is not JSON
        manual_parameters=[{"name": "file","in": "formData","type": "file",
                            "description": "The file to upload",
                "required": True,}],
        responses={status.HTTP_200_OK: "Success response description"},
    )
    def create(self, request):
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        request_body=None,  # Since it's a file upload, the body is not JSON
        manual_parameters=[{"name": "file", "in": "formData", "type": "file",
                            "description": "The file to upload",
                            "required": True, }],
        responses={status.HTTP_200_OK: "Success response description"},
    )
    def update(self, request, pk=None):
        if 'task' not in request.POST or not request.POST['task']:
            return Response({"error": "Task field is required"}, status=status.HTTP_400_BAD_REQUEST)
        item = get_object_or_404(File.objects.all(), pk=pk)
        serializer = FileSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=None,  # Since it's a file upload, the body is not JSON
        manual_parameters=[{"name": "file", "in": "formData", "type": "file",
                            "description": "The file to upload",
                            "required": True, }],
        responses={status.HTTP_200_OK: "Success response description"},
    )
    def partial_update(self, request, pk=None):
        item=get_object_or_404(File.objects.all(),pk=pk)
        serializer=FileSerializer(item,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
