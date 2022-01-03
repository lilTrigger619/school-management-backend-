from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Staff_Serializer, ViewStaff_Serializer
from rest_framework.response import Response
from rest_framework import status
from base_user_manager.models import C_user
from knox.models import AuthToken
from .models import Staff


#myecable.com
# Create your views here.
class Detail_Staff_View(APIView):

    def get(self, request, pk):
        data = Staff.objects.get(pk=pk)
        serialized_data = ViewStaff_Serializer(data)
        res_data = serialized_data.data.update({
            'username':
            data.user.username,
            'first name':
            data.user.first_name,
            'last name':
            data.user.last_name,
        })
        return Response(res_data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        acc = Staff.objects.get(pk=pk)
        data = request.data
        serialized_data = Staff_Serializer(acc, data=data)
        if serialized_data.is_valid():
            user = serialized_data.save()
        else:
            return Response(serialized_data.errors,
                            status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, pk):
        obj = Staff.objects.get(pk=pk)
        obj.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class All_Staff_View(APIView):

    def get(self, request):
        data = Staff.objects.all()
        serialized_data = ViewStaff_Serializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serialized_data = Staff_Serializer(data=data)
        if serialized_data.is_valid():
            staff = serialized_data.save()
            return Response(serialized_data.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Register_Staff_View(APIView):

    def post(self, request):
        data = request.data
        serialized_data = Staff_Serializer(data=data)
        if serialized_data.is_valid():
            staff = serialized_data.save()
            return Response(
                {
                    'username': serialized_data.validated_data['username'],
                    'email': serialized_data.validated_data['email'],
                },
                status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
