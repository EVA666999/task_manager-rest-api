from rest_framework import serializers
import base64
from django.core.files.base import ContentFile
from .models import Task, Project

class TaskSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    image = serializers.CharField(required=False, allow_blank=True)
    

    class Meta:
        fields = "__all__"
        model = Task

    def create(self, validated_data):
        image_data = validated_data.pop('image', None)
        if image_data:
            format, imgstr = image_data.split(';base64,') 
            ext = format.split('/')[-1]
            validated_data['image'] = ContentFile(base64.b64decode(imgstr), name=f'temp.{ext}')
        return super().create(validated_data)
    
class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    description = serializers.CharField(required=True, allow_blank=False)
    tasks = serializers.SerializerMethodField()
    
    class Meta:
        fields = "__all__"
        model = Project
    
    def get_tasks(self, obj):
        tasks = Task.objects.filter(project=obj)
        return TaskSerializer(tasks, many=True).data