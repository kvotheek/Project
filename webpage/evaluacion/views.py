from django.shortcuts import render

from alternativas.models import secc_alternativa


def evaluacion(request):
    return render(request, 'evaluacion.html')

# Funcion de las preguntas. con filter se obtiene la información del moódulo específico. Devuelve la database y el .html correspondiente al numero de la pregunta.  
def uno_(request):
    primera= secc_alternativa.objects.filter(numero_respuesta_alt=1)  
    return render(request, 'ev1.html',{'primera':primera})  

def dos_(request):
    segunda= secc_alternativa.objects.filter(numero_respuesta_alt=2)  
    return render(request, 'ev2.html',{'segunda':segunda})

def tres_(request):
    tercera= secc_alternativa.objects.filter(numero_respuesta_alt=3)  
    return render(request, 'ev3.html',{'tercera':tercera}) 

def cuatro_(request):
    cuarto= secc_alternativa.objects.filter(numero_respuesta_alt=4)  
    return render(request, 'ev4.html',{'cuarto':cuarto})  

def cinco_(request):
    quinto= secc_alternativa.objects.filter(numero_respuesta_alt=5)  
    return render(request, 'ev5.html',{'quinto':quinto})

def seis_(request):
    sexto= secc_alternativa.objects.filter(numero_respuesta_alt=6)  
    return render(request, 'ev6.html',{'sexto':sexto}) 

def siete_(request):
    sept= secc_alternativa.objects.filter(numero_respuesta_alt=7)  
    return render(request, 'ev7.html',{'sept':sept})  

def ocho_(request):
    octavo= secc_alternativa.objects.filter(numero_respuesta_alt=8)  
    return render(request, 'ev8.html',{'octavo':octavo})

def nueve_(request):
    noveno= secc_alternativa.objects.filter(numero_respuesta_alt=9)  
    return render(request, 'ev9.html',{'noveno':noveno}) 

def diez_(request):
    decimo= secc_alternativa.objects.filter(numero_respuesta_alt=10)  
    return render(request, 'ev10.html',{'decimo':decimo})  

def once_(request):
    onceavo= secc_alternativa.objects.filter(numero_respuesta_alt=11)  
    return render(request, 'ev11.html',{'onceavo':onceavo})

def doce_(request):
    doceavo= secc_alternativa.objects.filter(numero_respuesta_alt=12)  
    return render(request, 'ev12.html',{'doceavo':doceavo}) 

def trece_(request):
    treceavo= secc_alternativa.objects.filter(numero_respuesta_alt=13)  
    return render(request, 'ev13.html',{'treceavo':treceavo})  

def catorce_(request):
    catorceavo= secc_alternativa.objects.filter(numero_respuesta_alt=14)  
    return render(request, 'ev14.html',{'catorceavo':catorceavo})

def quince_(request):
    quinceavo= secc_alternativa.objects.filter(numero_respuesta_alt=15)  
    return render(request, 'ev15.html',{'quinceavo':quinceavo}) 

def diesciseis_(request):
    diesciseis= secc_alternativa.objects.filter(numero_respuesta_alt=16)  
    return render(request, 'ev16.html',{'diesciseis':diesciseis})  

def diescisiete_(request):
    diescisiete= secc_alternativa.objects.filter(numero_respuesta_alt=17)  
    return render(request, 'ev17.html',{'diescisiete':diescisiete})

def diesciocho_(request):
    diesciocho= secc_alternativa.objects.filter(numero_respuesta_alt=18)  
    return render(request, 'ev18.html',{'diesciocho':diesciocho}) 

def diescinueve_(request):
    diescinueve= secc_alternativa.objects.filter(numero_respuesta_alt=19)  
    return render(request, 'ev19.html',{'diescinueve':diescinueve})  

def veinte_(request):
    veinte= secc_alternativa.objects.filter(numero_respuesta_alt=20)  
    return render(request, 'ev20.html',{'veinte':veinte})

def veintiuno_(request):
    veintiuno= secc_alternativa.objects.filter(numero_respuesta_alt=21)  
    return render(request, 'ev21.html',{'veintiuno':veintiuno}) 

def veintidos_(request):
    veintidos= secc_alternativa.objects.filter(numero_respuesta_alt=22)  
    return render(request, 'ev22.html',{'veintidos':veintidos})  

def veintitres_(request):
    veintitres= secc_alternativa.objects.filter(numero_respuesta_alt=23)  
    return render(request, 'ev23.html',{'veintitres':veintitres})

def veinticuatro_(request):
    veinticuatro= secc_alternativa.objects.filter(numero_respuesta_alt=24)  
    return render(request, 'ev24.html',{'veinticuatro':veinticuatro}) 

def veinticinco_(request):
    veinticinco= secc_alternativa.objects.filter(numero_respuesta_alt=25)  
    return render(request, 'ev25.html',{'veinticinco':veinticinco})  

def veintiseis_(request):
    veintiseis= secc_alternativa.objects.filter(numero_respuesta_alt=26)  
    return render(request, 'ev26.html',{'veintiseis':veintiseis})

def veintisiete_(request):
    veintisiete= secc_alternativa.objects.filter(numero_respuesta_alt=27)  
    return render(request, 'ev27.html',{'veintisiete':veintisiete}) 

def veintiocho_(request):
    veintiocho= secc_alternativa.objects.filter(numero_respuesta_alt=28)  
    return render(request, 'ev28.html',{'veintiocho':veintiocho})  

def veintinueve_(request):
    veintinueve= secc_alternativa.objects.filter(numero_respuesta_alt=29)  
    return render(request, 'ev29.html',{'veintinueve':veintinueve})

def treinta_(request):
    treinta= secc_alternativa.objects.filter(numero_respuesta_alt=30)  
    return render(request, 'ev30.html',{'treinta':treinta}) 
