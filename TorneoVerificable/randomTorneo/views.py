from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from randomTorneo.serializers import UserSerializer, GroupSerializer
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
#import requests
import hashlib

from rest_framework.views import APIView
from randomTorneo.models import Torneos, Equipos

class Generar(APIView):
    
    @staticmethod
    def get(request):
        #no hace nada
        return Response("Henloget", status=200)

    
    @staticmethod
    def post(request):
    	nombre = request.data.get('nombre')
    	nEquipos= request.data.get('nEquipos')
    	descripcion= request.data.get('descripcion')
    	fechaSorteo= request.data.get('fechaSorteo')

    	if not None in [nombre, nEquipos, descripcion, fechaSorteo]:
    		#generar torneo en la base de datos
    		torneo= Torneos(nombre = nombre, max_equipos = nEquipos, descripcion = descripcion, timestamp = fechaSorteo , id_pulso = -1)
    		torneo.save()
    		idSorteo= torneo.id
    		return Response(idSorteo, status=200)
    	return Response("Error en la data", status=400)

class Torneo(APIView):
    # obtener listado de puertas
    @staticmethod
    def get(request):
    	idTorneo = request.query_params.get('id')
    	print("id torneo es:" + idTorneo)
    	torneo= get_or_none(Torneos,id=idTorneo)
    	print("id torneo es:" + idTorneo)
    	response={"nombre": torneo.nombre, "max_equipos": torneo.max_equipos, "descripcion": torneo.descripcion, "timestamp": torneo.timestamp, "id_pulso":torneo.id_pulso}
    	if torneo is not None:
    		return Response(response, status=200)
    	else:
    		return Response("Equipo no existe uwu", 400)	

   
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


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None        