from rest_framework import serializers
from .models import Course
from Teachers.serializers import Basic_staff_serializer


class Course_serializer(serializers.ModelSerializer):
    #getting all courses with only course title
    class Meta:
        model = Course
        fields = 'name'


class Detailed_course_serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False, label='ID')
    name = serializers.CharField(max_length=225)
    staff = Basic_staff_serializer(many=True, required=False)

    def create(self, validated_data):
        name = validated_data['name']
        _course = Course.objects.create(name=name)
        return _course

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    """
        
    """
