from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Staff_Serializer, C_user_serializer
from rest_framework.response import Response
from rest_framework import status
from base_user_manager.models import C_user
from knox.models import AuthToken
from .models import Staff
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.
class Detail_Staff_View(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, pk):
        data = Staff.objects.get(pk=pk)
        usr = data.user
        serialized_data = C_user_serializer(usr)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        acc = Staff.objects.get(pk=pk)
        data = request.data
        serialized_data = Staff_Serializer(acc, data=data)

        if serialized_data.is_valid():
            user = serialized_data.save()
            user.user.first_name = serialized_data.validated_data['first_name']
            user.user.last_name = serialized_data.validated_data['last_name']
            user.user.email = serialized_data.validated_data['email']
            user.user.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized_data.errors,
                            status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, pk):
        obj = Staff.objects.get(pk=pk)
        obj.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class All_Staff_View(APIView):
    permission_classes = [
            IsAuthenticated,
            ]

    def get(self, request):
        data = C_user.objects.all()
        usr = request.user
        serialized_data = C_user_serializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)





class Register_Staff_View(APIView):
# Admin staff registration    
    permission_classes = [
        IsAuthenticated,
    ]
    parser_classes = [
        MultiPartParser,
        FormParser,
    ]

    def post(self, request, format=None):
        data = request.data
        serialized_data = Staff_Serializer(data=data)
        if serialized_data.is_valid():
            staff = serialized_data.save()
            view = ViewStaff_Serializer(staff)
            return Response(view.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Get_User_View(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        usr = request.user
        serialized_data = C_user_serializer(request.user)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
