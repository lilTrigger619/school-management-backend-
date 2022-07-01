from rest_framework import serializers
from Course.serializers import Course_serializer 
from .models import Sem_2

#A semester serializer for each classroom

class Sem_2_serializer(serializers.ModelSerializer):
    course = Course_serializer(many=True, required=False)
    class Meta:
        model = Sem_2
        fields = '__all__'

