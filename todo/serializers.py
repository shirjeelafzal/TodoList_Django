from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
class CustomUserSerializer(serializers.Serializer):
    # Add your custom fields here
    view = serializers.BooleanField(default=False)
    edit = serializers.BooleanField(default=False)
class TaskSerializer(serializers.Serializer):

    status_choices = [
        ("to_do", "to_do"),
        ("in_progress","in_progress"),
        ("done","done"),
    ]
    priority_choices = [
        ("low", "low"),
        ("medium","medium"),
        ("high","high"),
    ]
    name=serializers.CharField(max_length=15)
    description = serializers.CharField(allow_blank=True, allow_null=True)
    status=serializers.ChoiceField(choices=status_choices,default="to_do")
    prority=serializers.ChoiceField(choices=priority_choices,default="low")  
    deadline=serializers.DateTimeField()
    start=serializers.DateTimeField()
    tag=serializers.CharField(max_length=15)

    # creator= serializers.CharField()
    # assigner=serializers.CharField()    
    
    
    def __str__(self):
        return self.name

    # items=serializers.RelatedField(many=True)
    # class Meta:
    #     model=Task


class FileSerializer(serializers.Serializer):
    files=serializers.FileField()
    task=serializers.CharField()
    def __str__(self):
        return (str(self.task))
    
class HistorySerializer(serializers.Serializer):
    Desciption_change=serializers.CharField()
    time=serializers.DateTimeField()
    
    task=serializers.CharField()
    user=serializers.CharField()
    # category = serializers.RelatedField()
