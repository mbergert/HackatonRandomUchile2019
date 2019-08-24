from randomTorneo.models import Torneos, Equipos

import time
import random
import string


#Generar torneos
for i in range(0,5):
	nombre = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])
	nEquipos= 10
	descripcion= ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
	fechaSorteo= time.time()
	torneo= Torneos(nombre = nombre, max_equipos = nEquipos, descripcion = descripcion, timestamp = fechaSorteo , id_pulso = -1)
	torneo.save()
#generar Equipos
	for j in range(0,10):
		nombre = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])
		equipo = Equipos(nombre= nombre,id_torneo= torneo.id, id_grupo=-1)
		equipo.save()	

