from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from .serializers import Staff_Serializer, Basic_staff_serializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from base_user_manager.models import C_user
from base_user_manager.serializers import Staff_account_serializer
from .models import Staff
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.
class Detail_Staff_View(APIView):
    """
    permission_classes = [
        IsAuthenticated,
    ]
    """

    def get(self, request, pk):
        _profile = get_object_or_404(Staff, pk=pk)
        _ser = Staff_Serializer(_profile)
        return Response(_ser.data, status=HTTP_200_OK)

    def put(self, request, pk):
        Err = {
            'account_error': '',
            'profile_error': '',
        }
        """
        {
            user: {},
            ....
        }
        the data should contain the user_credentials and user data
        """
        _profile = get_object_or_404(Staff, pk=pk)
        _data = request.data

        #updating the user account of the profile
        _account_cred = _data.pop('user')
        _account = _profile.user
        _ser_account = Staff_account_serializer(_account, data=_account_cred)
        if (_ser_account.is_valid()):
            _ser_account.save()
            Err['account_error'] = ''
        else:
            Err['account_error'] = _ser_account.errors

        #updating the user profile
        _ser_profile = Staff_Serializer(_profile, data=_data)
        if (_ser_profile.is_valid()):
            _ser_profile.save()
            Err['profile_error'] = ''
        else:
            Err['profile_error'] = _ser_profile.errors

        if (Err['profile_error'] or Err['account_error']):
            return Response(Err, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(_ser_profile.data, status=HTTP_200_OK)

    def delete(self, request, pk):
        obj = get_object_or_404(Staff, pk=pk)
        obj.user.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class All_Staff_View(APIView):
    """
    permission_classes = [
        IsAuthenticated,
    ]
    """

    def get(self, request):
        data = get_list_or_404(Staff)
        serialized_data = Staff_Serializer(data, many=True)
        return Response(serialized_data.data, status=HTTP_200_OK)


class Register_Staff_View(APIView):
    # Admin staff registration
    """
    permission_classes = [
        IsAuthenticated,
    ]
    parser_classes = [
        MultiPartParser,
        FormParser,
    ]
    """

    def post(self, request, format=None):
        data = request.data
        serialized_data = Staff_Serializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors,
                            status=HTTP_500_INTERNAL_SERVER_ERROR)


class Basic_staff_view(APIView):

    def get(self, request):
        _staff = request.user
        _ser_staff = Basic_staff_serializer(request.user.staff)
        _basic_list = get_list_or_404(Staff)
        _ser_list = Basic_staff_serializer(_basic_list, many=True)
        return Response({
            "user":_ser_staff.data, 
            "data":_ser_list.data,
            }, status=HTTP_200_OK)

class Detailed_basic_staff_view(APIView):

    def get(self, request, pk):
        _basic_user = get_object_or_404(Staff, pk=pk)
        _ser_basic_user = Basic_staff_serializer(_basic_user)
        return Response(_ser_basic_user.data, status=HTTP_200_OK)
