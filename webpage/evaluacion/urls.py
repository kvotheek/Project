from django.urls import path

from .views import *

urlpatterns= [
 # pagina inicial evaluacion
 path ('', evaluacion, name='evaluacion'), 

 # ruta de las preguntas
 path('1/', uno_, name='uno_'), # se visualiza la respuesta en la ruta uno/ y redirecciona al archivo respuesta_1.html
 path('2/', dos_, name='dos_'),
 path('3/', tres_, name='tres_'),
 path('4/', cuatro_, name='cuatro_'),
 path('5/', cinco_, name='cinco_'),
 path('6/', seis_, name='seis_'),
 path('7/', siete_, name='siete_'),
 path('8/', ocho_, name='ocho_'),
 path('9/', nueve_, name='nueve_'),
 path('10/', diez_, name='diez_'),
 path('11/', once_, name='once_'), 
 path('12/', doce_, name='doce_'),
 path('13/', trece_, name='trece_'),
 path('14/', catorce_, name='catorce_'),
 path('15/', quince_, name='quince_'),
 path('16/', diesciseis_, name='diesciseis_'),
 path('17/', diescisiete_, name='diescisiete_'),
 path('18/', diesciocho_, name='diesciocho_'),
 path('19/', diescinueve_, name='diescinueve_'),
 path('20/', veinte_, name='veinte_'),
 path('21/', veintiuno_, name='veintiuno_'), 
 path('22/', veintidos_, name='veintidos_'),
 path('23/', veintitres_, name='veintitres_'),
 path('24/', veinticuatro_, name='veinticuatro_'),
 path('25/', veinticinco_, name='veinticinco_'),
 path('26/', veintiseis_, name='veintiseis_'),
 path('27/', veintisiete_, name='veintisiete_'),
 path('28/', veintiocho_, name='veintiocho_'),
 path('29/', veintinueve_, name='veintinueve_'),
 path('30/', treinta_, name='treinta_'),


]