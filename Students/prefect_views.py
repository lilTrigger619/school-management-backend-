from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import Prefect_serializer
from .models import Prefect

class Prefect_view(APIView):
    def post(self, request):
        _data = request.data
        _ser = Prefect_serializer(data=_data)
        if(_ser.is_valid()):
            _ser.save()
            return Response(_ser.data, status=status.HTTP_200_OK)
        else:
            return Response(_ser.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        _prefects = get_list_or_404(Prefect)
        _ser = Prefect_serializer(_prefects)
        return Response(_ser.data, status=status.HTTP_200_OK)


class Prefect_detail_view(APIView):
    def get (self, request, pk):
        _prefect = get_object_or_404(Prefect)
        _ser = Prefect_serializer(_prefect)
        return Response(_ser.data, status=status.HTTP_200_OK)
    
    def put (self, request, pk):
        _data = request.data
        _prefect = get_object_or_404(Prefect, pk=pk)
        _ser = Prefect_serializer(_prefect, data=_data)
        if(_ser.is_valid()):
            _ser.save()
            return Response(_ser.data, status=status.HTTP_200_OK)
        else:
            return Response(_ser.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        def delete (self, request, pk):
            _prefect = get_object_or_404(Prefect, pk=pk)
            _prefect.delete()
            return Response("Deleted", status=status.HTTP_200_OK)
