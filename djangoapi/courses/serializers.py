"""Serializer Classes"""
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    """Course Serializer"""
    class Meta:
        """Meta Class"""
        model = Course
        fields = ['id', 'name', 'language', 'price']
