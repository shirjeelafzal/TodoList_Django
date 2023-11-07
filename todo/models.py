from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(User):
    # Add your custom fields here
    view = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
class Task(models.Model):
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
    name=models.CharField(max_length=15)
    description=models.TextField()
    status=models.CharField(max_length=15, choices=status_choices,default="to_do")
    prority=models.CharField(max_length=15,choices=priority_choices,default="low")  
    deadline=models.DateTimeField()
    start=models.DateTimeField()
    tag=models.CharField(max_length=15)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,related_name='task2task',default='1')
    assigner=models.ForeignKey(User, on_delete=models.CASCADE,related_name='assigners',default='1')
    def __str__(self):
        return self.name
    
    
class File(models.Model):
    files=models.FileField()
    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    def __str__(self):
        return self.task
    
class History(models.Model):
    Desciption_change=models.TextField()
    time=models.DateTimeField()
    
    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task
    
