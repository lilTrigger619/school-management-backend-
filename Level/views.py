from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, HTTP_304_NOT_MODIFIED
from rest_framework.views import APIView
from .serializers import Level_serializer
from .models import Level
from Teachers.models import Staff


# Create your views here.
class Level_view(APIView):
    """
        {
            sem_1:{
                courses:[],
                add: [],
                remove: [],
            },
            sem_2:{
                courses:[],
                add: [],
                remove: [],
            },
            sem_3:{
                courses:[],
                add: [],
                remove: [],
            },
            name: 'something',
            staff: {
                add: [],
                remove: [],
                present: [],
            },
        }
    """

    def post(self, request):
        _data = request.data
        #creating all semesters
        sem1 = Sem_1.objects.create()
        sem1.save()
        sem2 = Sem_2.objects.create()
        sem2.save()
        sem3 = Sem_3.objects.create()
        sem3.save()
        #adding courses if they are available
        if (_data['sem_1']['add']):
            _sem1_courses = _data['sem_1']['add']
            for pk in _sem1_courses:
                _crs = get_object_or_404(Course, pk=pk)
                sem1.course.add(_crs)
        if (_data['sem_2']['add']):
            _sem2_courses = _data['sem_2']['add']
            for pk in _sem2_courses:
                _crs2 = get_object_or_404(Course, pk=pk)
                sem2.course.add(_crs)
        if (_data['sem_3']['add']):
            _sem3_courses = _data['sem_3']['add']
            for pk in _sem3_courses:
                _crs3 = get_object_or_404(Course, pk=pk)
                sem3.course.add(_crs)
        sem1.save()
        sem2.save()
        sem3.save()
        #all staff's to add
        _staff = _data['staff']
        #Creating the level
        _ser_level = Level_serializer(data=_data['level'])
        if (_ser_level.is_valid()):
            lvl = _ser_level.save()
            Err['level_errors'] = ''
            lvl.sem_1 = sem1
            lvl.sem_2 = sem2
            lvl.sem_3 = sem3

            if (_staff['add']):
                for pk in _staff['add']:
                    _stf = get_object_or_404(_staff, pk=pk)
                    lvl.staff.add(_stf)

            lvl.save()

            return Response(_ser.data, status=HTTP_201_CREATED)
        else:
            return Response(_ser.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        _list = get_list_or_404(Level)
        _ser = Level_serializer(_list, many=True)
        return Response(_ser.data, status=HTTP_200_OK)


class Detailed_level_view(APIView):

    def get(self, request, pk):
        _level = get_object_or_404(Level, pk=pk)
        _ser = Level_serializer(_level)
        return Response(_ser.data, status=HTTP_200_OK)

    def put(self, request, pk):
        _data = request.data
        _level = get_object_or_404(Level, pk=pk)
        """
            {
                sem_1:{
                    courses:[],
                    add: [],
                    remove: [],
                },
                sem_2:{
                    courses:[],
                    add: [],
                    remove: [],
                },
                sem_3:{
                    courses:[],
                    add: [],
                    remove: [],
                },
                name: 'something',
                staff: {
                    add: [],
                    remove: [],
                    present: [],
                },
            }
        """
        _staff = _data.pop('staff')
        _sem_1 = _data.pop('sem_1')
        _sem_2 = _data.pop('sem_2')
        _sem_3 = _data.pop('sem_3')
        #updating the staff
        if (_staff['add']):
            _staff_add = _staff['add']
            for pk in _staff_add:
                _staff_obj = get_object_or_404(Staff, pk=pk)
                _level.staff.add(_staff_obj)
        if (_staff['remove']):
            _staff_remove = _staff['remove']
            for pk in _staff_remove:
                _staff_obj = get_object_or_404(Staff, pk=pk)
                _level.staff.remove(_staff_obj)
        #updating all sem courses
        if (_sem_1['add']):
            for pk in _sem_1['add']:
                _crs = get_object_or_404(Course, pk=pk)
                _level.sem_1.course.add(_crs)
        if (_sem_1['remove']):
            for pk in _sem_1['remove']:
                _crs = get_object_or_404(Course, pk=pk)
                _level.sem_1.course.remove(_crs)
        if (_sem_2['add']):
            for pk in _sem_2['add']:
                _crs = get_object_or_404(Course, pk=pk)
                _level.sem_2.course.add(_crs)
        if (_sem_2['remove']):
            for pk in _sem_2['remove']:
                _crs = get_object_or_404(Course, pk=pk)
                _level.sem_2.course.remove(_crs)
        if (_sem_3['add']):
            for pk in _sem_3['add']:
                _crs = get_object_or_404(Course, pk=pk)
                _level.sem_3.course.add(_crs)
        if (_sem_3['remove']):
            for pk in _sem_3['remove']:
                _crs = get_object_or_404(Course, pk=pk)
                _level.sem_3.course.remove(_crs)
        #updating the name of the Level
        _ser = Level_serializer(_level, data=_data)
        if (_ser.is_valid()):
            _ser.save()
            return Response(_ser.data, status=HTTP_201_CREATED)
        else:
            return Response(_ser.errors, status=HTTP_304_NOT_MODIFIED)
