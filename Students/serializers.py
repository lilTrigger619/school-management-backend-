from base_user_manager.serializers import Student_account_serializer
from Students.models import Student, Prefect
from base_user_manager.models import C_user
from rest_framework import serializers


#minimalistic data for populating table and statisfying
# small data requests.
class Student_minimal_view_serializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=244, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    email = serializers.EmailField(required=False)
    username = serializers.CharField(max_length=255, required=False)
    gender = serializers.CharField(max_length=255, required=False)
    phone = serializers.CharField(max_length=255, required=False)
    nationality = serializers.CharField(max_length=70, required=False)
    is_rep = serializers.BooleanField(required=False)
    is_class_rep = serializers.BooleanField(required=False)
    level = serializers.CharField(max_length=255, required=False)
    is_active = serializers.BooleanField(required=False)


class Basic_student_serializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    current_level = serializers.CharField(max_length=245, required=False)




#Prefect serializer
class Prefect_serializer(serializers.ModelSerializer):
    student = Basic_student_serializer(many=True, required=False)

    class Meta:
        model = Prefect
        fields = '__all__'


#Creating a full student account and profile.
# Note on line number 95
class Create_student_profile_serializer(serializers.ModelSerializer):
    user = Student_account_serializer(required=False)
    prefect_set = Prefect_serializer(required=False, many=True)

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop(
            'user'
        )  #this will pop the user object from the validated_data into the user variable
        user = Student_account_serializer(data=user_data)
        if (user.is_valid()):
            x_user = user.save()
            profile = Student.objects.create(user=x_user, **validated_data)
            return profile

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.other_name = validated_data.get('other_name',
                                                    instance.last_name)
        instance.last_name = validated_data.get('last_name',
                                                instance.last_name)
        instance.date_of_birth = validated_data.get('date_of_birth',
                                                    instance.date_of_birth)
        instance.location = validated_data.get('location', instance.location)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.disability = validated_data.get('disability',
                                                 instance.disability)
        instance.illness = validated_data.get('illness', instance.illness)
        instance.allergies = validated_data.get('allergies',
                                                instance.allergies)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.profile_image = validated_data.get('profile_image',
                                                    instance.profile_image)
        instance.is_rep = validated_data.get('rep', instance.is_rep)
        instance.is_class_rep = validated_data.get('rep',
                                                   instance.is_class_rep)
        instance.parent_confirmation = validated_data.get(
            'parent_confirmation', instance.parent_confirmation)
        instance.level = validated_data.get('level', instance.level)
        #parent.
        instance.biological_parent = validated_data.get('biological_parent',instance.biological_parent)
        instance.mother_fullname = validated_data.get('mother_fullname',instance.mother_fullname)
        instance.father_fullname = validated_data.get('father_fullname',instance.father_fullname)
        instance.mother_date_of_birth = validated_data.get('mother_date_of_birth',instance.mother_date_of_birth)
        instance.father_date_of_birth = validated_data.get('father_date_of_birth',instance.father_date_of_birth)
        instance.mother_phone = validated_data.get('mother_phone',instance.mother_phone)
        instance.father_phone  = validated_data.get('father_phone',instance.father_phone)
        instance.mother_email = validated_data.get('mother_email',instance.mother_email)
        instance.father_email = validated_data.get('father_email',instance.father_email)
        instance.parent_marrital_status = validated_data.get('parent_marrital_status',instance.parent_marrital_status)
        instance.save()
        return instance

'''
    Notes
Create_student_profile_serializer:
    The profile serializer will take all the parameters for create 
    a new user profile and will pass the parameters to the account 
    serializer so that it will create the account for the student

    When it comes to updating, the view will only pass the profile data to the serializer and put the rest to the view.
    So this serializer is not handling the updaing of the user
    account.
'''
