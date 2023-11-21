from django.contrib.auth import authenticate
from django.shortcuts import  get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Task, User, File, History
from .serializers import TaskSerializer, UserSerializer, FileSerializer, HistorySerializer,LoginSerializer,ProfileViewSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class LoginViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    def create(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'message':"Login Successful"},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'errors':{'non_field_errors':['Email or password is not correct']}}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

@extend_schema(responses=UserSerializer)
class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer()
    queryset = User.objects.all()

    def list(self, request):
        if User.objects.all():
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No data available"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        try:
            viewset = User.objects.get(id=pk)
            serializer = UserSerializer(viewset)
            return Response(serializer.data)
        except:
            return Response({"message": "This user does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            obj = User.objects.get(id=pk)
            obj.delete()
            return Response({"massage":"The user has been deleted successfully"},status=status.HTTP_200_OK)
        except:
            return Response({"message": "This user does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'messagge': 'User created'}, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            item = get_object_or_404(User.objects.all(), pk=pk)
            serializer = UserSerializer(item, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({"No user exists with this id"}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            item = get_object_or_404(User.objects.all(), pk=pk)
            serializer = UserSerializer(item, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({"No user exists with this id"}, status=status.HTTP_400_BAD_REQUEST)



@extend_schema(responses=TaskSerializer)
class TaskViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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
    parser_classes = [MultiPartParser]
    def list(self, request):
        if File.objects.all():
            queryset = File.objects.all()
            serializer = FileSerializer(queryset, many=True)
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
            return Response({"Detail": "Data has been deleted"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "This data does not exist"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=None,
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
        request_body=None,
        manual_parameters=[{"name": "file", "in": "formData", "type": "file",
                            "description": "The file to upload",
                            "required": True, }],
        responses={status.HTTP_200_OK: "Success response description"},
    )
    def update(self, request, pk=None):
        if len(request.data['task'])==0 or len(request.data['files'])==0:
            return Response({"error": "Enter all fields correctly"}, status=status.HTTP_400_BAD_REQUEST)
        item = get_object_or_404(File.objects.all(), pk=pk)
        serializer = FileSerializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        request_body=None,
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
class ProfileViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]
    def list(self,request):
        try:
            serializer=ProfileViewSerializer(request.user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({'error':"Could not verify user"}, status=status.HTTP_404_NOT_FOUND)