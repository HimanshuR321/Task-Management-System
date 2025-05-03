from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Task

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class ProjectSerializer(serializers.ModelSerializer):
    tasks_count = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'created_at', 'updated_at', 'user', 'tasks_count')
        read_only_fields = ('user', 'tasks_count')

    def get_tasks_count(self, obj):
        return obj.tasks.count()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'due_date', 'status', 'created_at', 'updated_at', 'project', 'user')
        read_only_fields = ('user',) 