from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, File,History,CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'
class TaskSerializer(serializers.ModelSerializer):
    # creator=CustomUserSerializer()
    # assigner=CustomUserSerializer()
    class Meta:
        model=Task
        fields='__all__'


class FileSerializer(serializers.ModelSerializer):
    # task=TaskSerializer()
    class Meta:
        model = File
        fields = '__all__' 
class HistorySerializer(serializers.ModelSerializer):
    # task=TaskSerializer()
    # user=CustomUserSerializer()
    class Meta:
        model = History
        fields = '__all__'