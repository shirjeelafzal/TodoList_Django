from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(User):
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
    priority=models.CharField(max_length=15,choices=priority_choices,default="low")
    deadline=models.DateTimeField()
    start=models.DateTimeField()
    tag=models.CharField(max_length=15)
    creator= models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='task2task',default=None)
    assigner=models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='assigners',default=None)
    def __str__(self):
        return self.name
    
    
class File(models.Model):
    def nameFile(instance,filename):
        return '/'.join(['files',str(instance.task),filename])
    files=models.FileField(upload_to=nameFile,blank=True)
    task=models.ForeignKey(Task, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return (str(self.task))
    
class History(models.Model):
    Desciption_change=models.TextField()
    time=models.DateTimeField()
    
    task=models.ForeignKey(Task, on_delete=models.CASCADE,default=None,null=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=None,null=True)
    
    def __str__(self):
        return (str(self.task))
    
