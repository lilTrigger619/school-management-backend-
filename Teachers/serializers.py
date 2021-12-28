from rest_framework import serializers
from base_user_manager.models import C_user

class Staff_Serializer (serializers.Serializer):
    username = serializers.CharField(max_length=30, required=True)
    password = serializers.CharField(max_length=300, required=True, write_only=True)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name= serializers.CharField(max_length=30, required=False)
    

    def create (self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']

        staff = C_user.objects.create_staff_user(username=username, email=email, password=password)
        staff.first_name = first_name
        staff.last_name = last_name
        staff.save()
        return staff

    def update (self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

'''
class View_Staff_Serializer (serializers.ModelSerializer):
    class Meta:
        model = C_user
        fields = ['id',  'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password':{'write_only':True}}
'''
