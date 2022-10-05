from django.urls import path
from .views import *


urlpatterns= [
 path('', terminos, name='terminos'),

 path('1/', uno_t, name='uno_t'), # se visualiza la respuesta en la ruta uno/ y redirecciona al archivo respuesta_1.html
 path('2/', dos_t, name='dos_t'),
 path('3/', tres_t, name='tres_t'),
 path('4/', cuatro_t, name='cuatro_t'),
 path('5/', cinco_t, name='cinco_t'),
 path('6/', seis_t, name='seis_t'),
 path('7/', siete_t, name='siete_t'),
 path('8/', ocho_t, name='ocho_t'),
 path('9/', nueve_t, name='nueve_t'),
 path('10/', diez_t, name='diez_t'),
 path('11/', once_t, name='once_t'), 
 path('12/', doce_t, name='doce_t'),
 path('13/', trece_t, name='trece_t'),
 path('14/', catorce_t, name='catorce_t'),
 path('15/', quince_t, name='quince_t'),
 path('16/', diesciseis_t, name='diesciseis_t'),
 path('17/', diescisiete_t, name='diescisiete_t'),
 path('18/', diesciocho_t, name='diesciocho_t'),
 path('19/', diescinueve_t, name='diescinueve_t'),
 path('20/', veinte_t, name='veinte_t'),
 path('21/', veintiuno_t, name='veintiuno_t'), 
 path('22/', veintidos_t, name='veintidos_t'),
 path('23/', veintitres_t, name='veintitres_t'),
 path('24/', veinticuatro_t, name='veinticuatro_t'),
 path('25/', veinticinco_t, name='veinticinco_t'),
 path('26/', veintiseis_t, name='veintiseis_t'),
 path('27/', veintisiete_t, name='veintisiete_t'),
 path('28/', veintiocho_t, name='veintiocho_t'),
 path('29/', veintinueve_t, name='veintinueve_t'),
 path('30/', treinta_t, name='treinta_t'),
]