from rest_framework import serializers
from .models import Level
from Semester_1.serializers import Sem_1_serializer
from Semester_2.serializers import Sem_2_serializer
from Semester_3.serializers import Sem_3_serializer
from Teachers.serializers import Basic_staff_serializer


class Level_serializer(serializers.ModelSerializer):
    sem_1 = Sem_1_serializer(required=False)
    sem_2 = Sem_2_serializer(required=False)
    sem_3 = Sem_3_serializer(required=False)
    staff = Basic_staff_serializer(many=True, required=False)

    class Meta:
        model = Level
        fields = '__all__'
        extra_kwargs = {'name': {'unique': True}}

    def create(self, validated_data):
        name = validated_data['name']
        lvl = Level.objects.create(name=name)
        lvl = lvl.save()
        return lvl

    def update(self, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class Basic_level_serializer(serializers.Serializer):
    name = serializers.CharField(required=True)
