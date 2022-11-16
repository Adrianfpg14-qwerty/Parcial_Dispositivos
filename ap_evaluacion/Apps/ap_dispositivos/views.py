from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from Apps.ap_dispositivos.models import AP_Dispositivos
from Apps.ap_dispositivos.serializers import ApDispositivosSerializer

# Create your views here.


class ApDispositivosList(APIView):
    """
    Lista de AP_Dispositivos
    """

    def get(self, request, format=None):
        ap_dispositivos = AP_Dispositivos.objects.all()
        serializer = ApDispositivosSerializer(ap_dispositivos, many=True)
        return Response({"ap_dispositivos":serializer.data})

    def post(self, request, format=None):
        serializer = ApDispositivosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApDispositivosDetail(APIView):
    """
    Retrieve, update or delete de los ap_dispositivos por pk
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return AP_Dispositivos.objects.get(pk=pk)
        except AP_Dispositivos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ap_dispositivo = self.get_object(pk)
        serializer = ApDispositivosSerializer(ap_dispositivo)
        return Response({"ap_dispositivo":serializer.data})

    def put(self, request, pk, format=None):
        ap_dispositivo = self.get_object(pk)
        serializer = ApDispositivosSerializer(ap_dispositivo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        ap_dispositivo = self.get_object(pk)
        serializer = ApDispositivosSerializer(ap_dispositivo,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        ap_dispositivo = self.get_object(pk)
        ap_dispositivo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
