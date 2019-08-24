from django.urls import path

from . import views

app_name = 'randomTorneo'

urlpatterns = (
    path('generar', views.Generar.as_view(), name='Generar Torneo'),
    path('torneo', views.Torneo.as_view(), name='Torneo'),
    path('inscribir', views.Inscribir.as_view(), name='Inscribir Equipo'),
	path('sortear', views.Sortear.as_view(), name='Sortear'),
    path('verificar', views.Verificar.as_view(), name='Verificar'),
    path('grupos', views.Grupos.as_view(), name='Grupos')

)
