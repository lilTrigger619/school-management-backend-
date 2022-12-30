from rest_framework  import serializers
from base_user_manager.models import C_user as User_controller
#from Teachers.models  import Staff as Teacher_profile_controller
#from Students.models import Student as Student_profile_controller

class Account_type_serializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    is_admin = serializers.BooleanField(required=True)
    is_student = serializers.BooleanField(required=True)
    is_staff = serializers.BooleanField(required=True)

class Mini_user_serializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    #is_verified = serializers.BooleanField(required=True)


