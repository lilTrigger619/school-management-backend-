from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from .serializers import Student_account_serializer, Staff_account_serializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED
from .models import C_user


# Create your views here.
class Student_account_view(APIView):

    def post(self, req):
        data = req.data
        ser_data = Student_account_serializer(data=data)
        if ser_data.is_valid():
            user = ser_data.save()
            return Response(ser_data.data, status=HTTP_201_CREATED)
        else:
            return Response(ser_data.errors,
                            status=HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, req):
        users = get_list_or_404(C_user, is_student=True)
        ser_data = Student_account_serializer(users, many=True)
        return Response(ser_data.data, status=HTTP_200_OK)


class Detailed_student_account_view(APIView):

    def get(self, req, pk):
        the_user = get_object_or_404(C_user, pk=pk, is_student=True)
        ser_data = Student_account_serializer(the_user)
        return Response(ser_data.data, status=HTTP_200_OK)

    def put(self, req, pk):
        _data = req.data
        the_user = get_object_or_404(C_user, pk=pk, is_student=True)
        ser_data = Student_account_serializer(the_user, data=_data)
        if (ser_data.is_valid()):
            ser_data.save()
            return Response(ser_data.data, status=HTTP_200_OK)
        else:
            #Debug
            print('#we got here')
            return Response(ser_data.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)


class Staff_account_view(APIView):

    def get(self, request):
        _list = get_list_or_404(C_user, is_staff=True)
        _ser_data = Staff_account_serializer(_list, many=True)
        return Response(_ser_data.data, status=HTTP_200_OK)

    def post(self, request):
        _data = request.data
        _ser_data = Staff_account_serializer(data=_data)
        if (_ser_data.is_valid()):
            _ser_data.save()
            return Response(_ser_data.data, status=HTTP_201_CREATED)
        else:
            return Response(_ser_data.errors,
                            status=HTTP_500_INTERNAL_SERVER_ERROR)


class Detailed_staff_account_view(APIView):

    def get(self, request, pk):
        _account = get_object_or_404(C_user, pk=pk, is_staff=True)
        _ser = Staff_account_serializer(_account)
        return Response(_ser.data, status=HTTP_200_OK)

    def put(self, request, pk):
        _account = get_object_or_404(C_user, pk=pk)
        _data = request.data
        _ser = Staff_account_serializer(_account, data=_data)
        if (_ser.is_valid()):
            _ser.save()
            return Response(_ser.data, status=HTTP_200_OK)
        else:
            return Response(_ser.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)


class Activate_user_account(APIView):

    def get(self, request, pk):
        user = get_object_or_404(C_user, pk=pk)
        user.is_active = True
        user.save()
        return Response(
            {'message': 'User activated {0}'.format(user.is_active)},
            status=HTTP_200_OK)


class Deactivate_user_account(APIView):

    def get(self, request, pk):
        user = get_object_or_404(C_user, pk=pk)
        print({'user': user})
        user.is_active = False
        user.save()
        return Response(
            {'message': 'User deactivated {0}'.format(user.is_active)},
            status=HTTP_200_OK)
