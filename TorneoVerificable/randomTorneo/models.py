from django.db import models

class Torneo(models.Model):
    nombre = models.CharField(max_length=50)
    max_equipos = models.IntegerField()
    descr = models.CharField(max_length=300)
    timestamp = models.BigIntegerField()
    id_pulso = models.BigIntegerField()
    listo = models.BooleanField()

    def getEquipos(self):
    	return Equipo.objects.get(id_torneo=self.id)

    def getGrupo(self, idgrupo):
    	grupo = Equipo.objects.get(id_torneo=self.id, id_grupo=idgrupo)
    	return grupo

    def countInscritos(self):
    	return Equipo.objects.get(id_torneo=self.id).count()


class Equipo(models.Model):
	nombre = models.CharField(max_length=50)
	id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
	id_grupo = models.IntegerField()


    



