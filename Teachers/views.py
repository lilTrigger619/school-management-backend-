from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Staff_Serializer #View_Staff_Serializer
from rest_framework.response import Response
from rest_framework import status
from base_user_manager.models import C_user
from knox.models import AuthToken

#myecable.com
# Create your views here.
class Detail_Staff_View(APIView):
    def get(self, request, pk):
        data = C_user.objects.get(pk=pk)
        serialized_data = Staff_Serializer(data)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        acc = C_user.objects.get(pk=pk)
        data = request.data
        serialized_data = Staff_Serializer(acc, data=data)
        if serialized_data.is_valid():
            user = serialized_data.save()
            if not serialized_data.data['first_name']:
                pass
            else:
                user.first_name = serialized_data.data['first_name']
            if not serialized_data.data['last_name']:
                pass
            else:
                user.last_name = serialized_data.data['last_name']

            if not serialized_data.data['email']:
                pass
            else:
                user.email = serialized_data.data['email']
            
            user.save()
        else: 
            return Response(serialized_data.errors, status=status.HTTP_304_NOT_MODIFIED)

    def delete (self, request, pk):
        obj = C_user.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Register_Staff_View (APIView):
    def get(self, request):
        data = C_user.objects.all()
        serialized_data = Staff_Serializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def post (self, request):
        data = request.data
        serialized_data = Staff_Serializer(data=data)
        if serialized_data.is_valid():
            staff=serialized_data.save()
            '''
            if not serialized_data.data['first_name']:
                pass
            else:
                staff.first_name = serialized_data.data['first_name']
            if not serialized_data.data['last_name']:
                pass
            else:
                staff.last_name = serialized_data.data['last_name']

            if not serialized_data.data['email']:
                pass
            else:
                staff.email = serialized_data.data['email']

            staff.save()

            '''
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
