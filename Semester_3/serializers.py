from rest_framework import serializers
from .models import Sem_3
from Course.serializers import Course_serializer

#A semester serializer for each classroom

class Sem_3_serializer(serializers.ModelSerializer):
    course = Course_serializer(many=True, required=False)
    class Meta:
        model = Sem_3
        fields = '__all__'

