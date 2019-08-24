from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from randomTorneo.serializers import UserSerializer, GroupSerializer
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
#import requests
import hashlib

from rest_framework.views import APIView


class Generar(APIView):
    # obtener listado de puertas
    @staticmethod
    def get(request):
        
        return Response("Henloget", status=200)

    # Abrir una puerta
    @staticmethod
    def post(request):
    	nombre = request.data.get('nombre')
    	nEquipos= request.data.get('nEquipos')
    	descripcion= request.data.get('descripcion')
    	fechaSorteo= request.data.get('fechaSorteo')
    	if not None in [nombre, nEquipos, descripcion, fechaSorteo]:
    		idSorteo= "id"
    		return Response(idSorteo, status=200)
    	return Response("Error en la data", status=400)

class Torneo(APIView):
    # obtener listado de puertas
    @staticmethod
    def get(request):
        
        return Response("Henloget", status=200)

    # Abrir una puerta
    @staticmethod
    def post(request):
        return Response("Henlopost", status=200)        



class Inscribir(APIView):
    # obtener listado de puertas
    @staticmethod
    def get(request):
        
        return Response("Henloget", status=200)

    # Abrir una puerta
    @staticmethod
    def post(request):
        return Response("Henlopost", status=200)  


class Sortear(APIView):
    # obtener listado de puertas
    @staticmethod
    def get(request):
        
        return Response("Henloget", status=200)

    # Abrir una puerta
    @staticmethod
    def post(request):
        return Response("Henlopost", status=200)              