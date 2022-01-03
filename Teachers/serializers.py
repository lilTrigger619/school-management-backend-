from rest_framework import serializers
from base_user_manager.models import C_user
from .models import Staff


class Staff_Serializer(serializers.Serializer):

    Gender = (('mal', 'Male'), ('fem', 'Female'))
    username = serializers.CharField(max_length=30, required=True)
    password = serializers.CharField(max_length=300,
                                     required=True,
                                     write_only=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=30, required=False)
    gender = serializers.CharField()
    position = serializers.CharField(
        max_length=40,
        required=False,
    )
    profile_image = serializers.ImageField(required=False)
    phone = serializers.CharField(max_length=30, required=False)
    location = serializers.CharField(max_length=30, required=False)
    disability = serializers.CharField(max_length=60, required=False)
    illness = serializers.CharField(max_length=130, required=False)

    def create(self, validated_data):
        try:
            username = validated_data['username']
        except KeyError:
            username = None

        try:
            password = validated_data['password']
        except KeyError:
            password = None

        try:
            first_name = validated_data['first_name']
        except KeyError:
            first_name = None

        try:
            last_name = validated_data['last_name']
        except KeyError:
            last_name = None

        try:
            email = validated_data['email']
        except KeyError:
            email = None

        try:
            profile_image = validated_data['profile_image']
        except KeyError:
            profile_image = None

        try:
            position = validated_data['position']
        except KeyError:
            position = None

        try:
            phone = validated_data['phone']
        except KeyError:
            phone = None

        try:
            location = validated_data['location']
        except KeyError:
            location = None

        try:
            disability = validated_data['disability']
        except KeyError:
            disability = None

        try:
            illness = validated_data['illness']
        except KeyError:
            illness = None

        try:
            gender = validated_data['gender']
        except KeyError:
            gender = None

        user = C_user.objects.create_staff_user(username=username,
                                                email=email,
                                                password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        staff = Staff.objects.create(user=user,
                                     profile_image=profile_image,
                                     position=position,
                                     phone=phone,
                                     location=location,
                                     disability=disability,
                                     illness=illness,
                                     gender=gender)
        return staff

    def update(self, instance, validated_data):
        print(instance)
        print(instance.user)
        print(instance.user.username)
        print(instance.user.first_name)
        print(instance.user.last_name)
        print(instance.user.email)
        print(dir(instance))
        instance.user.username = validated_data.get('username', instance.user.username)
        instance.user.password = validated_data.get('password', instance.user.password)
        instance.user.first_name = validated_data.get('first_name',
                                                 instance.user.first_name)
        instance.user.last_name = validated_data.get('last_name',
                                                instance.user.last_name)
        instance.user.email = validated_data.get('email', instance.user.email)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.illness = validated_data.get('illness', instance.illness)
        instance.disability = validated_data.get('disability',
                                                 instance.disability)
        instance.location = validated_data.get('location', instance.location)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.position = validated_data.get('position', instance.position)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.user.save()
        instance.save()
        return instance

class ViewStaff_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
