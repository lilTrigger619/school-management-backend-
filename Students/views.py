from django.shortcuts import render, get_object_or_404, get_list_or_404
from .serializers import Create_student_profile_serializer, Student_account_serializer, C_user, Student_minimal_view_serializer, Prefect_serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Student


# Create a student account  (POST)
class Create_student_profile_view(APIView):
    #this view is just for creating students not for viewing.
    parser_classes=[FormParser, MultiPartParser]
    permission_classes=[IsAuthenticated]
    def post(self, request):
        _xdata = request.data
        _ser_data = Create_student_profile_serializer(data=_xdata)
        if (_ser_data.is_valid()):
            _ser_data.save()
            return Response(_ser_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(_ser_data.errors,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Detailed update view (PUT GET)
class Detail_update_student_profile_view(APIView):
    #This view is used to get a detail view on the student
    # and also update.
    permission_classes=[IsAuthenticated]
    parser_classes=[FormParser, MultiPartParser]
    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        std_account = student.user
        _xdata = request.data
        _x_user_data = _xdata.pop('user')
        _ser = Create_student_profile_serializer(student, data=_xdata)
        _acc_ser = Student_account_serializer(std_account, data=_x_user_data)
        if (_ser.is_valid() and _acc_ser.is_valid()):
            _ser.save()
            _acc_ser.save()
            return Response(_ser.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'profile_error': _ser.errors,
                    'account_error': _acc_ser.errors
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        _ser = Create_student_profile_serializer(student)
        return Response(_ser.data, status=status.HTTP_200_OK)


#Mini student view (GET)
class Student_minimal_view(APIView):
    #this view is only used to get the student mininal view
    # this will not accept any post request.
    def get(self, request):
        all_students = Student.objects.all()
        the_data = []
        print(all_students)
        for student in all_students:
            lvl = ''
            if (student.level):
                lvl = student.level.name
            else:
                lvl = ''
            the_data.append({
                'first_name': student.first_name,
                'last_name': student.last_name,
                'username': student.user.username,
                'email': student.user.email,
                'gender': student.gender,
                'phone': student.phone,
                'nationality': student.nationality,
                'level': lvl,
                'is_rep': student.is_rep,
                'is_class_rep': student.is_class_rep,
                'is_active': student.user.is_active,
            })

        _ser = Student_minimal_view_serializer(the_data, many=True)
        return Response(_ser.data, status=status.HTTP_200_OK)
'''
      Notes

Detail_update_student_profile_view
................................
this view will get and update the full student user profile.
The user account credentials will be taken to {Student_account_serializer}
which was import from base user manager with the instance of the user. 

        Data should come this form=
            {
             user:{}, // which will be taken to another serializer.
              first_name:"somthing",
              last_name: "something",
              emial;"something",

            }
'''
