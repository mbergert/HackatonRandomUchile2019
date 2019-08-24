from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from randomTorneo.serializers import UserSerializer, GroupSerializer
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import hashlib
import random
from randomTorneo.models import Torneos, Equipos

from rest_framework.views import APIView
from randomTorneo.models import Torneos, Equipos

class Generar(APIView):

    @staticmethod
    def get(request):
        # no hace nada
        return Response("Henloget", status=200)

    @staticmethod
    def post(request):
        nombre = request.data.get('nombre')
        nEquipos = request.data.get('nEquipos')
        descripcion = request.data.get('descripcion')
        fechaSorteo = request.data.get('fechaSorteo')

        if not None in [nombre, nEquipos, descripcion, fechaSorteo]:
            # generar torneo en la base de datos
            torneo = Torneos(nombre=nombre, max_equipos=nEquipos, descripcion=descripcion, timestamp=fechaSorteo,
                             id_pulso=-1)
            torneo.save()
            idSorteo = torneo.id
            return Response(idSorteo, status=200)
        return Response("Error en la data", status=400)
    
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

# API URL
beacon_url = "https://random.uchile.cl/beacon/2.0/pulse/time/"


def get_pulse(timestamp):
    beacon_url = "https://random.uchile.cl/beacon/2.0/pulse/time/" + timestamp
    content = requests.get(beacon_url)

    # JSON containing all the pulse data
    pulse = content.json()["pulse"]

    # Random string of 512 bits obtained from the pulse
    seed = pulse["outputValue"]

    # This index will be used by the observer to verify the process
    pulse_index = pulse["pulseIndex"]

    return pulse_index, seed


def run_lottery(timestamp, idsequipos):
    pulse_index, seed = get_pulse(timestamp)
    N = len(idsequipos)

    # Seed the PRNG
    random.seed(seed)

    # The list to be shared
    equipos = [-1 for i in range(N)]

    for i in range(N):
        number = random.choice(idsequipos)
        equipos[i] = number
        idsequipos.remove(number)


    return equipos

def run_lotteryid(pulse_index, idsequipos):
    beacon_url = "https://beacon.clcert.cl/beacon/2.0/chain/4/pulse/" + str(pulse_index)
    content = requests.get(beacon_url)

    # JSON containing all the pulse data
    pulse = content.json()["pulse"]

    # Random string of 512 bits obtained from the pulse
    seed = pulse["outputValue"]

    N = len(idsequipos)

    # Seed the PRNG
    random.seed(seed)

    # The list to be shared
    equipos = [-1 for i in range(N)]

    for i in range(N):
        number = random.choice(idsequipos)
        equipos[i] = number
        idsequipos.remove(number)


    return equipos

def ordenar(equipos):

    res = [[], [], [], []]
    for e in equipos:
        res[e.id_grupo].append([e.id, e.nombre])
    return res



class Sortear(APIView):
    @staticmethod
    def get(request):
        
        return Response("Henloget", status=200)

    @staticmethod
    def post(request):
        idtorneo = request.POST['id']
        torneo = Torneos.objects.get(id=idtorneo)
        timestamp = str(torneo.timestamp)
        id_pulso, seed = get_pulse(timestamp)
        torneo.id_pulso = id_pulso
        torneo.save()

        equipos = Equipos.objects.filter(id_torneo=idtorneo)
        idsequipos = []
        for e in equipos:
            idsequipos.append(e.id)

        grupos = run_lottery(timestamp, idsequipos)

        for i in range(len(grupos)):
            eq = Equipos.objects.get(id=grupos[i])
            eq.id_grupo = i%4
            eq.save()

        res = ordenar(grupos)


        return Response({"equipos" : res, "id_pulso" : id_pulso, "datos_iniciales" : idsequipos}, status=200)

class Verificar(APIView):
    @staticmethod
    def get(request):
        pulseid = request.GET['id_pulso']
        datos_iniciales=request.GET['datos_iniciales']
        idsequipos = []

        for key in datos_iniciales:
            idsequipos.append(datos_iniciales[key])

        equipos = run_lotteryid(pulseid, idsequipos)
        res = ordenar(equipos)


        return Response(res, status=200)

    @staticmethod
    def post(request):
        return Response("Henlopost", status=200)



def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None
