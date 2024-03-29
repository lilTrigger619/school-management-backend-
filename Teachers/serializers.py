from base_user_manager.serializers import Staff_account_serializer
from base_user_manager.models import C_user
from rest_framework import serializers
from .models import Staff


class Staff_Serializer(serializers.ModelSerializer):
    user = Staff_account_serializer(required=False)

    class Meta:
        model = Staff
        fields = '__all__'

    """
    Gender = (('mal', 'Male'), ('fem', 'Female'))
    id = serializers.IntegerField(label='ID', read_only=True, required=False)
    username =  serializers.CharField(required=False, max_length=50)
    date_of_birth= serializers.DateField(required=False)
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
    photo  = serializers.ImageField(required=False)
    phone = serializers.CharField(max_length=30, required=False)
    location = serializers.CharField(max_length=30, required=False)
    disability = serializers.CharField(max_length=60, required=False)
    illness = serializers.CharField(max_length=130, required=False)
    """

    def create(self, validated_data):
        try:
            first_name = validated_data['first_name']
        except KeyError:
            first_name = ''

        try:
            last_name = validated_data['last_name']
        except KeyError:
            last_name = ''

        try:
            email = validated_data['email']
        except KeyError:
            email = ''

        try:
            photo = validated_data['photo']
        except KeyError:
            photo = ''

        try:
            position = validated_data['position']
        except KeyError:
            position = ''

        try:
            phone = validated_data['phone']
        except KeyError:
            phone = ''

        try:
            location = validated_data['location']
        except KeyError:
            location = ''

        try:
            disability = validated_data['disability']
        except KeyError:
            disability = ''

        try:
            illness = validated_data['illness']
        except KeyError:
            illness = ''

        try:
            date_of_birth = validated_data['date_of_birth']
        except KeyError:
            date_of_birth = None
        try:
            gender = validated_data['gender']
        except KeyError:
            gender = ''

        try:
            username = validated_data['username']
        except KeyError:
            username = ''

        _account_cred = validated_data.pop('user')

        _account = Staff_account_serializer(data=_account_cred)
        if (_account.is_valid()):
            user = _account.save()
            staff = Staff.objects.create(user=user,
                                         first_name=first_name,
                                         last_name=last_name,
                                         email=email,
                                         profile_image=photo,
                                         position=position,
                                         phone=phone,
                                         location=location,
                                         disability=disability,
                                         illness=illness,
                                         date_of_birth=date_of_birth,
                                         gender=gender)
            return staff

    def update(self, instance, validated_data):
        #updating the user instance of the instance
        instance.user.username = validated_data.get('username',
                                                    instance.user.username)
        instance.user.first_name = validated_data.get('first_name',
                                                      instance.user.first_name)
        instance.user.last_name = validated_data.get('last_name',
                                                     instance.user.last_name)
        instance.user.email = validated_data.get('email', instance.user.email)

        #updating the instance values
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.last_name = validated_data.get('last_name',
                                                instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.illness = validated_data.get('illness', instance.illness)
        instance.disability = validated_data.get('disability',
                                                 instance.disability)
        instance.location = validated_data.get('location', instance.location)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.position = validated_data.get('position', instance.position)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.profile_image = validated_data.get('photo',
                                                    instance.profile_image)
        instance.save()
        return instance

#gettings the level name
class Basic_level_serializer(serializers.Serializer):
    name = serializers.CharField(required=True)

#gettings the staff course set
class Basic_staff_course_serializer(serializers.Serializer):
   short_name = serializers.CharField(required=True) 

#gettings the staff active status
class Active_staff_serializer(serializers.Serializer):
    is_active = serializers.BooleanField(required=False)

class Basic_staff_serializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
    uuid = serializers.CharField(max_length=4000)
    position = serializers.CharField(max_length=40)
    phone = serializers.CharField(max_length=40)
    gender = serializers.CharField(max_length=3)
    level_set = Basic_level_serializer(many=True, required=False)
    course_set = Basic_staff_course_serializer(many=True, required=False)
    #this is just used to get the is active status of the teacher.
    user = Active_staff_serializer(required=False)
