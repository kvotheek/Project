from django.shortcuts import render

from .models import secc_alternativa

#para seccion intento cambio ruta
from django.shortcuts import get_object_or_404


def inicio_alternativas(request):
    #alternativas= secc_alternativa.objects.all()   por ahora se traen todos los objetos del modelo
    return render(request, 'home.html') #devuelve alternativas que contiene lo guardado en la base de datos 

# idea intento de cambio de ruta
def p_detail(request, p_id):
    p=get_object_or_404(secc_alternativa, pk=p_id)
    return render (request, 'p.html', {"p":p})

# Funcion de las preguntas. con filter se obtiene la información del moódulo específico. Devuelve la database y el .html correspondiente al numero de la pregunta.  
def uno(request):
    primera= secc_alternativa.objects.filter(numero_respuesta_alt=1)  
    return render(request, '1.html',{'primera':primera})  

def dos(request):
    segunda= secc_alternativa.objects.filter(numero_respuesta_alt=2)  
    return render(request, '2.html',{'segunda':segunda})

def tres(request):
    tercera= secc_alternativa.objects.filter(numero_respuesta_alt=3)  
    return render(request, '3.html',{'tercera':tercera}) 

def cuatro(request):
    cuarto= secc_alternativa.objects.filter(numero_respuesta_alt=4)  
    return render(request, '4.html',{'cuarto':cuarto})  

def cinco(request):
    quinto= secc_alternativa.objects.filter(numero_respuesta_alt=5)  
    return render(request, '5.html',{'quinto':quinto})

def seis(request):
    sexto= secc_alternativa.objects.filter(numero_respuesta_alt=6)  
    return render(request, '6.html',{'sexto':sexto}) 

def siete(request):
    sept= secc_alternativa.objects.filter(numero_respuesta_alt=7)  
    return render(request, '7.html',{'sept':sept})  

def ocho(request):
    octavo= secc_alternativa.objects.filter(numero_respuesta_alt=8)  
    return render(request, '8.html',{'octavo':octavo})

def nueve(request):
    noveno= secc_alternativa.objects.filter(numero_respuesta_alt=9)  
    return render(request, '9.html',{'noveno':noveno}) 

def diez(request):
    decimo= secc_alternativa.objects.filter(numero_respuesta_alt=10)  
    return render(request, '10.html',{'decimo':decimo})  

def once(request):
    onceavo= secc_alternativa.objects.filter(numero_respuesta_alt=11)  
    return render(request, '11.html',{'onceavo':onceavo})

def doce(request):
    doceavo= secc_alternativa.objects.filter(numero_respuesta_alt=12)  
    return render(request, '12.html',{'doceavo':doceavo}) 

def trece(request):
    treceavo= secc_alternativa.objects.filter(numero_respuesta_alt=13)  
    return render(request, '13.html',{'treceavo':treceavo})  

def catorce(request):
    catorceavo= secc_alternativa.objects.filter(numero_respuesta_alt=14)  
    return render(request, '14.html',{'catorceavo':catorceavo})

def quince(request):
    quinceavo= secc_alternativa.objects.filter(numero_respuesta_alt=15)  
    return render(request, '15.html',{'quinceavo':quinceavo}) 

def diesciseis(request):
    diesciseis= secc_alternativa.objects.filter(numero_respuesta_alt=16)  
    return render(request, '16.html',{'diesciseis':diesciseis})  

def diescisiete(request):
    diescisiete= secc_alternativa.objects.filter(numero_respuesta_alt=17)  
    return render(request, '17.html',{'diescisiete':diescisiete})

def diesciocho(request):
    diesciocho= secc_alternativa.objects.filter(numero_respuesta_alt=18)  
    return render(request, '18.html',{'diesciocho':diesciocho}) 

def diescinueve(request):
    diescinueve= secc_alternativa.objects.filter(numero_respuesta_alt=19)  
    return render(request, '19.html',{'diescinueve':diescinueve})  

def veinte(request):
    veinte= secc_alternativa.objects.filter(numero_respuesta_alt=20)  
    return render(request, '20.html',{'veinte':veinte})

def veintiuno(request):
    veintiuno= secc_alternativa.objects.filter(numero_respuesta_alt=21)  
    return render(request, '21.html',{'veintiuno':veintiuno}) 

def veintidos(request):
    veintidos= secc_alternativa.objects.filter(numero_respuesta_alt=22)  
    return render(request, '22.html',{'veintidos':veintidos})  

def veintitres(request):
    veintitres= secc_alternativa.objects.filter(numero_respuesta_alt=23)  
    return render(request, '23.html',{'veintitres':veintitres})

def veinticuatro(request):
    veinticuatro= secc_alternativa.objects.filter(numero_respuesta_alt=24)  
    return render(request, '24.html',{'veinticuatro':veinticuatro}) 

def veinticinco(request):
    veinticinco= secc_alternativa.objects.filter(numero_respuesta_alt=25)  
    return render(request, '25.html',{'veinticinco':veinticinco})  

def veintiseis(request):
    veintiseis= secc_alternativa.objects.filter(numero_respuesta_alt=26)  
    return render(request, '26.html',{'veintiseis':veintiseis})

def veintisiete(request):
    veintisiete= secc_alternativa.objects.filter(numero_respuesta_alt=27)  
    return render(request, '27.html',{'veintisiete':veintisiete}) 

def veintiocho(request):
    veintiocho= secc_alternativa.objects.filter(numero_respuesta_alt=28)  
    return render(request, '28.html',{'veintiocho':veintiocho})  

def veintinueve(request):
    veintinueve= secc_alternativa.objects.filter(numero_respuesta_alt=29)  
    return render(request, '29.html',{'veintinueve':veintinueve})

def treinta(request):
    treinta= secc_alternativa.objects.filter(numero_respuesta_alt=30)  
    return render(request, '30.html',{'treinta':treinta}) 

# Funcion de las respuestas. Con filter se obtiene la información del moódulo específico. Devuelve la variable con la database y el .html correspondiente al numero de la respuesta. 
# Se mantiene la variable que almacena la data, solo se cambia el .html para luego poder llamarlo en href de las preguntas.

def uno_r(request):
    primera= secc_alternativa.objects.filter(numero_respuesta_alt=1)  
    return render(request, 'res_1.html',{'primera':primera})  

def dos_r(request):
    segunda= secc_alternativa.objects.filter(numero_respuesta_alt=2)  
    return render(request, 'res_2.html',{'segunda':segunda})

def tres_r(request):
    tercera= secc_alternativa.objects.filter(numero_respuesta_alt=3)  
    return render(request, 'res_3.html',{'tercera':tercera}) 

def cuatro_r(request):
    cuarto= secc_alternativa.objects.filter(numero_respuesta_alt=4)  
    return render(request, 'res_4.html',{'cuarto':cuarto})  

def cinco_r(request):
    quinto= secc_alternativa.objects.filter(numero_respuesta_alt=5)  
    return render(request, 'res_5.html',{'quinto':quinto})

def seis_r(request):
    sexto= secc_alternativa.objects.filter(numero_respuesta_alt=6)  
    return render(request, 'res_6.html',{'sexto':sexto}) 

def siete_r(request):
    sept= secc_alternativa.objects.filter(numero_respuesta_alt=7)  
    return render(request, 'res_7.html',{'sept':sept})  

def ocho_r(request):
    octavo= secc_alternativa.objects.filter(numero_respuesta_alt=8)  
    return render(request, 'res_8.html',{'octavo':octavo})

def nueve_r(request):
    noveno= secc_alternativa.objects.filter(numero_respuesta_alt=9)  
    return render(request, 'res_9.html',{'noveno':noveno}) 

def diez_r(request):
    decimo= secc_alternativa.objects.filter(numero_respuesta_alt=10)  
    return render(request, 'res_10.html',{'decimo':decimo})  

def once_r(request):
    onceavo= secc_alternativa.objects.filter(numero_respuesta_alt=11)  
    return render(request, 'res_11.html',{'onceavo':onceavo})

def doce_r(request):
    doceavo= secc_alternativa.objects.filter(numero_respuesta_alt=12)  
    return render(request, 'res_12.html',{'doceavo':doceavo}) 

def trece_r(request):
    treceavo= secc_alternativa.objects.filter(numero_respuesta_alt=13)  
    return render(request, 'res_13.html',{'treceavo':treceavo})  

def catorce_r(request):
    catorceavo= secc_alternativa.objects.filter(numero_respuesta_alt=14)  
    return render(request, 'res_14.html',{'catorceavo':catorceavo})

def quince_r(request):
    quinceavo= secc_alternativa.objects.filter(numero_respuesta_alt=15)  
    return render(request, 'res_15.html',{'quinceavo':quinceavo}) 

def diesciseis_r(request):
    diesciseis= secc_alternativa.objects.filter(numero_respuesta_alt=16)  
    return render(request, 'res_16.html',{'diesciseis':diesciseis})  

def diescisiete_r(request):
    diescisiete= secc_alternativa.objects.filter(numero_respuesta_alt=17)  
    return render(request, 'res_17.html',{'diescisiete':diescisiete})

def diesciocho_r(request):
    diesciocho= secc_alternativa.objects.filter(numero_respuesta_alt=18)  
    return render(request, 'res_18.html',{'diesciocho':diesciocho}) 

def diescinueve_r(request):
    diescinueve= secc_alternativa.objects.filter(numero_respuesta_alt=19)  
    return render(request, 'res_19.html',{'diescinueve':diescinueve})  

def veinte_r(request):
    veinte= secc_alternativa.objects.filter(numero_respuesta_alt=20)  
    return render(request, 'res_20.html',{'veinte':veinte})

def veintiuno_r(request):
    veintiuno= secc_alternativa.objects.filter(numero_respuesta_alt=21)  
    return render(request, 'res_21.html',{'veintiuno':veintiuno}) 

def veintidos_r(request):
    veintidos= secc_alternativa.objects.filter(numero_respuesta_alt=22)  
    return render(request, 'res_22.html',{'veintidos':veintidos})  

def veintitres_r(request):
    veintitres= secc_alternativa.objects.filter(numero_respuesta_alt=23)  
    return render(request, 'res_23.html',{'veintitres':veintitres})

def veinticuatro_r(request):
    veinticuatro= secc_alternativa.objects.filter(numero_respuesta_alt=24)  
    return render(request, 'res_24.html',{'veinticuatro':veinticuatro}) 

def veinticinco_r(request):
    veinticinco= secc_alternativa.objects.filter(numero_respuesta_alt=25)  
    return render(request, 'res_25.html',{'veinticinco':veinticinco})  

def veintiseis_r(request):
    veintiseis= secc_alternativa.objects.filter(numero_respuesta_alt=26)  
    return render(request, 'res_26.html',{'veintiseis':veintiseis})

def veintisiete_r(request):
    veintisiete= secc_alternativa.objects.filter(numero_respuesta_alt=27)  
    return render(request, 'res_27.html',{'veintisiete':veintisiete}) 

def veintiocho_r(request):
    veintiocho= secc_alternativa.objects.filter(numero_respuesta_alt=28)  
    return render(request, 'res_28.html',{'veintiocho':veintiocho})  

def veintinueve_r(request):
    veintinueve= secc_alternativa.objects.filter(numero_respuesta_alt=29)  
    return render(request, 'res_29.html',{'veintinueve':veintinueve})

def treinta_r(request):
    treinta= secc_alternativa.objects.filter(numero_respuesta_alt=30)  
    return render(request, 'res_30.html',{'treinta':treinta}) 