from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from Students.models import Student as Student_profile_controller
from Teachers.models import Staff as Teacher_profile_controller
from .profile_serializers import Account_type_serializer, Mini_user_serializer

class Account_type(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            _ser = Account_type_serializer(request.user)
            return Response(_ser.data, status=HTTP_200_OK)
        except:
            return Response({"message":"Failed to get user account"}, status=HTTP_401_NOT_FOUND)


class Mini_user(APIView):
    permission_classes= [IsAuthenticated]

    def get(self, request):
        try:
            _ser = Mini_user_serializer(request.user)
            return Response(_ser.data, status=HTTP_200_OK)
        except:
            raise Exception("Failed to get mini user")
        return Response({"message":"failed to get user data"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
