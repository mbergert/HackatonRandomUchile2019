from django.db import models

class Torneos(models.Model):
    nombre = models.CharField(max_length=50)
    max_equipos = models.IntegerField()
    descripcion = models.CharField(max_length=300)
    timestamp = models.BigIntegerField()
    id_pulso = models.BigIntegerField()
    listo = models.BooleanField(default=False)

    def getEquipos(self):
    	return Equipos.objects.get(id_torneo=self.id)

    def getGrupo(self, idgrupo):
    	grupo = Equipos.objects.get(id_torneo=self.id, id_grupo=idgrupo)
    	return grupo

    def countInscritos(self):
    	return Equipos.objects.get(id_torneo=self.id).count()


class Equipos(models.Model):
	nombre = models.CharField(max_length=50)
	id_torneo = models.ForeignKey(Torneos, on_delete=models.CASCADE)
	id_grupo = models.IntegerField()


    



