


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
