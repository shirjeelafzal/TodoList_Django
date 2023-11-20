from django.shortcuts import  get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import Task, CustomUser, File, History
from .serializers import TaskSerializer, CustomUserSerializer, FileSerializer, HistorySerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


@extend_schema(responses=TaskSerializer)
class TaskViewSet(viewsets.ViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def list(self, request):
        if Task.objects.all():
            queryset = Task.objects.all()
            serializer = TaskSerializer(self.queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No data available"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        try:
            viewset = Task.objects.get(id=pk)
            serializer = TaskSerializer(viewset)
            return Response(serializer.data)
        except:
            return Response({
                "message": "Data does not exist",
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):

        try:
            obj = Task.objects.get(id=pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "No data to delete"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        item = get_object_or_404(Task.objects.all(), pk=pk)
        serializer = TaskSerializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        item = get_object_or_404(Task.objects.all(), pk=pk)
        serializer = TaskSerializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(responses=CustomUserSerializer)
class UserViewSet(viewsets.ViewSet):
    serializer_class = CustomUserSerializer()
    queryset = CustomUser.objects.all()

    def list(self, request):
        if CustomUser.objects.all():
            queryset = CustomUser.objects.all()
            serializer = CustomUserSerializer(self.queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No data available"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        try:
            viewset = CustomUser.objects.get(id=pk)
            serializer = CustomUserSerializer(viewset)
            return Response(serializer.data)
        except:
            return Response({"message": "This user does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            obj = CustomUser.objects.get(id=pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "This user does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        item = get_object_or_404(CustomUser.objects.all(), pk=pk)
        serializer = CustomUserSerializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        item = get_object_or_404(CustomUser.objects.all(), pk=pk)
        serializer = CustomUserSerializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(responses=HistorySerializer)
class HistoryViewSet(viewsets.ViewSet):
    serializer_class = HistorySerializer()
    queryset = History.objects.all()

    def list(self, request):
        if History.objects.all():
            queryset = History.objects.all()
            serializer = HistorySerializer(self.queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No data available"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        try:
            viewset = History.objects.get(id=pk)
            serializer = HistorySerializer(viewset)
            return Response(serializer.data)
        except:
            return Response({"message": "This data does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            obj = History.objects.get(id=pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "This data does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = HistorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        item = get_object_or_404(History.objects.all(), pk=pk)
        serializer = HistorySerializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        item = get_object_or_404(History.objects.all(), pk=pk)
        serializer = HistorySerializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(responses=FileSerializer)
class FileViewSet(viewsets.ViewSet):
    serializer_class = FileSerializer()
    queryset = File.objects.all()

    def list(self, request):
        if File.objects.all():
            queryset = File.objects.all()
            serializer = FileSerializer(self.queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No data available"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        try:
            viewset = File.objects.get(id=pk)
            serializer = FileSerializer(viewset)
            return Response(serializer.data)
        except:
            return Response({"message": "This data does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            obj = File.objects.get(id=pk)
            obj.delete()
            return Response({"Detail": "Data has been deleted"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "This data does not exist"}, status=status.HTTP_404_NOT_FOUND)

    #
    @swagger_auto_schema(
        request_body=None,  # Since it's a file upload, the body is not JSON
        manual_parameters=[{"name": "file", "in": "formData", "type": "file",
                            "description": "The file to upload",
                            "required": True, }],
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
    def partial_update(self, request, pk=None):
        item = get_object_or_404(File.objects.all(), pk=pk)
        serializer = FileSerializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
