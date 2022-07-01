from rest_framework import serializers
from .models import C_user


#create_staff_account_serializer
class Staff_account_serializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {'password': {'write_only': True,}}
        fields = '__all__'
        model = C_user

    def create(self, validated_data):
        username = validated_data['username']
        try:
            email = validated_data['email']
        except KeyError:
            email = ''
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        stf_user = C_user.objects.create_staff_user(username=username,
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)
        stf_user.set_password(password)
        stf_user.save()
        return stf_user

    def update(self, instance, validated_data):
        username = validated_data.get('username', instance.username)
        email = validated_data.get('email', instance.email)
        first_name = validated_data.get('first_name', instance.first_name)
        last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.get('password', instance.password)
        instance.first_name = first_name
        instance.last_name = last_name
        instance.email = email
        instance.username = username
        instance.set_password(password)
        instance.save()
        return instance


#create_student_account_serializer
class Student_account_serializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {'password': {'write_only': True}}
        fields = '__all__'
        model = C_user

    def create(self, validated_data):
        username = validated_data['username']
        try:
            email = validated_data['email']
        except KeyError:
            email = ''
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        std_user = C_user.objects.create_student_user(username=username,
                                                      email=email,
                                                      first_name=first_name,
                                                      last_name=last_name)
        std_user.set_password(password)
        std_user.save()
        return std_user

    def update(self, instance, validated_data):
        username = validated_data.get('username', instance.username)
        email = validated_data.get('email', instance.email)
        first_name = validated_data.get('first_name', instance.first_name)
        last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.get('password', instance.password)
        instance.first_name = first_name
        instance.last_name = last_name
        instance.email = email
        instance.username = username
        instance.set_password(password)
        instance.save()
        return instance


'''
class Change_password_serializer(serializers.ModelSerializer):
    class Meta:
        model = C_user
        fields = ['password']
        extra_kwargs = {'password':{'write_only':True}}
        
    def update(self, instance, validated_data):
        password = validated_data.get('password', instance.password)
        instance.set_password(password)
        instance.save()
        return instance
'''
