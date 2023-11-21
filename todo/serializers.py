from rest_framework import serializers
from .models import Task, File, History, User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ["id",'email','name','view','edit','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError("Password and confirm password does not match")
        return attrs
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password']

class ProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','name']


