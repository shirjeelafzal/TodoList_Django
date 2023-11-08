from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, File,History,CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'


class FileSerializer(serializers.ModelSerializer):
    # task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

    class Meta:
        model = File
        fields = '__all__' 
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'