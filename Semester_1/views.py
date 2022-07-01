from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import Sem_1_serializer as _SSer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED
from .models import Sem_1

# Create your views here.


class Sem_1_view(APIView):

    def post(self, request):
        _data = request.data
        _ser = _SSer(data=_data)
        if (_ser.is_valid()):
            _ser.save()
            return Response(_ser.data, status=HTTP_201_CREATED)
        else:
            return Response(_ser.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)


    def get(self, request):
        _list = get_list_or_404(Sem_1)
        _ser = _SSer(_ser)
        return Response(_ser.data, status=HTTP_200_OK)


class Sem_1_detail_view(APIView):
    def get (self, request, pk):
        _sem = get_object_or_404(Sem_1, pk=pk)
        _ser = _DSer(_sem)
        return Response(_ser.data, status=HTTP_200_OK)

    def post (self, request, pk):
        _data = request.data
        _sem = get_object_or_404(Sem_1, pk=pk)

