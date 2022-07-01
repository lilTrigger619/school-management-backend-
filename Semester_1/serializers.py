from rest_framework import serializers
from .models import Sem_1
from Course.serializers import Course_serializer 

#A semester serializer for each classroom

class Sem_1_serializer(serializers.ModelSerializer):
    course = Course_serializer(many=True, required=False)
    class Meta:
        model = Sem_1
        fields = '__all__'

