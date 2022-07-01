from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_304_NOT_MODIFIED
from rest_framework.response import Response
from .serializers import Course_serializer as _Cs, Detailed_course_serializer as _Dcs
from .models import Course
from Teachers.models import Staff


# Create your views here.
class Course_view(APIView):
    """
    {
        name:"somthing",
        staff:{
            present: [],
            add: [],
            remove: [],
        },
    }
    """

    def post(self, request):
        _data = request.data
        _staff_data = _data.pop('staff')
        _ser = _Dcs(data=_data)
        if (_ser.is_valid()):
            _course = _ser.save()
            #add staff to the course creation
            if (_staff_data['add']):
                for pk in _staff_data['add']:
                    _staff = get_object_or_404(Staff, pk=pk)
                    _course.staff.add(_staff)
            _ser_course = _Dcs(_course)
            return Response(_ser_course.data, status=HTTP_201_CREATED)
        else:
            return Response(_ser.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        _course = get_list_or_404(Course)
        _ser = _Dcs(_course, many=True)
        return Response(_ser.data, status=HTTP_200_OK)


class Detailed_course_view(APIView):

    def get(self, request, pk):
        _course = get_object_or_404(Course, pk=pk)
        _ser = _Dcs(_course)
        return Response(_ser.data, status=HTTP_200_OK)

    def put(self, request, pk):
        """
            the data should come in this format
            {
                name : "somthing",
                staff : {
                    add : [], 
                    remove: [],
                },
            }
        """
        _course = get_object_or_404(Course, pk=pk)
        _data = request.data
        _staff = _data.pop("staff")
        if (_staff['add']):
            # making sure the primary_keys in the array exist
            _add_staff = _staff['add']
            for data in _add_staff:
                _staff_obj = get_object_or_404(Staff, pk=data)
                _course.staff.add(_staff_obj)
        if (_staff['remove']):
            _remove_staff = _staff['remove']
            for data in _remove_staff:
                _staff_obj = get_object_or_404(Staff, pk=data)
                _course.staff.remove(_staff_obj)

        _ser = _Dcs(_course, data=_data)
        if (_ser.is_valid()):
            _ser.save()
            return Response(_ser.data, status=HTTP_200_OK)
        else:
            return Response(_ser.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        _course = get_object_or_404(Course, pk=pk)
        _course.delete()
        return Response({"detail": "Course Deleted!"}, status=HTTP_200_OK)
