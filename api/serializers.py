from rest_framework import serializers
from .models import ClassEntity

class ClassSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    responsavel = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return ClassEntity(**validated_data)
