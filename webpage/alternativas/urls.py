from django.urls import path
#preguntas
from .views import *

# path (url visible, funcion en .views, name= nombre del archivo.html )
urlpatterns= [
 path('', inicio_alternativas, name='inicio_alternativas'),  # se visualiza la pagina home.html ('') al llegar al home de la app alternativas, lo que sería el home de las alternativas
 
 #Cambio de la ruta manual o automatico
 #path('<int:p_id>', p_detail),
 #path('<p_id:int>',p_detail),
 
 # ruta de las preguntas
 path('1/', uno, name='uno'), # se visualiza la respuesta en la ruta uno/ y redirecciona al archivo respuesta_1.html
 path('2/', dos, name='dos'),
 path('3/', tres, name='tres'),
 path('4/', cuatro, name='cuatro'),
 path('5/', cinco, name='cinco'),
 path('6/', seis, name='seis'),
 path('7/', siete, name='siete'),
 path('8/', ocho, name='ocho'),
 path('9/', nueve, name='nueve'),
 path('10/', diez, name='diez'),
 path('11/', once, name='once'), 
 path('12/', doce, name='doce'),
 path('13/', trece, name='trece'),
 path('14/', catorce, name='catorce'),
 path('15/', quince, name='quince'),
 path('16/', diesciseis, name='diesciseis'),
 path('17/', diescisiete, name='diescisiete'),
 path('18/', diesciocho, name='diesciocho'),
 path('19/', diescinueve, name='diescinueve'),
 path('20/', veinte, name='veinte'),
 path('21/', veintiuno, name='veintiuno'), 
 path('22/', veintidos, name='veintidos'),
 path('23/', veintitres, name='veintitres'),
 path('24/', veinticuatro, name='veinticuatro'),
 path('25/', veinticinco, name='veinticinco'),
 path('26/', veintiseis, name='veintiseis'),
 path('27/', veintisiete, name='veintisiete'),
 path('28/', veintiocho, name='veintiocho'),
 path('29/', veintinueve, name='veintinueve'),
 path('30/', treinta, name='treinta'),

 # ruta de las respuestas
 path('res1/', uno_r, name='uno_r'), 
 path('res2/', dos_r, name='dos_r'),
 path('res3/', tres_r, name='tres_r'),
 path('res4/', cuatro_r, name='cuatro_r'),
 path('res5/', cinco_r, name='cinco_r'),
 path('res6/', seis_r, name='seis_r'),
 path('res7/', siete_r, name='siete_r'),
 path('res8/', ocho_r, name='ocho_r'),
 path('res9/', nueve_r, name='nueve_r'),
 path('res10/', diez_r, name='diez_r'),
 path('res11/', once_r, name='once_r'), 
 path('res12/', doce_r, name='doce_r'),
 path('res13/', trece_r, name='trece_r'),
 path('res14/', catorce_r, name='catorce_r'),
 path('res15/', quince_r, name='quince_r'),
 path('res16/', diesciseis_r, name='diesciseis_r'),
 path('res17/', diescisiete_r, name='diescisiete_r'),
 path('res18/', diesciocho_r, name='diesciocho_r'),
 path('res19/', diescinueve_r, name='diescinueve_r'),
 path('res20/', veinte_r, name='veinte_r'),
 path('res21/', veintiuno_r, name='veintiuno_r'), 
 path('res22/', veintidos_r, name='veintidos_r'),
 path('res23/', veintitres_r, name='veintitres_r'),
 path('res24/', veinticuatro_r, name='veinticuatro_r'),
 path('res25/', veinticinco_r, name='veinticinco_r'),
 path('res26/', veintiseis_r, name='veintiseis_r'),
 path('res27/', veintisiete_r, name='veintisiete_r'),
 path('res28/', veintiocho_r, name='veintiocho_r'),
 path('res29/', veintinueve_r, name='veintinueve_r'),
 path('res30/', treinta_r, name='treinta_r'),

]

