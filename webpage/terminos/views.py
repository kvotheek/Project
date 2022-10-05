from django.shortcuts import render

from .models import alternativas_tp
from alternativas.models import secc_alternativa # se importa el modelo creado en la seccion de alternativas para poder obtener información de imagen, pregunta, respuesta

# VIEWS QUE CONTIENE LAS FUNCIONES DE LOS TÉRMINOS PAREADOS.
# Aqui se llama a la base de datos para devolver una página que contiene las preguntas, 
"""
PODRIA EXISTIR UN BOTON PARA CONTINUAR A LA SIGUIENTE PREGUNTA Y UN BOTON PARA VER LA RESPUESTA DIRECTAMENTE. 
"""
def terminos(request):
    return render(request, 'terminospareados.html')

# Cada funcion contiene dos extracciones de objetos, uno que corresponde a la database de la pregunta/imagen/respuesta y otro
# que contiene solo las respuestas de los términos pareados.
# Con filter se obtiene la información del moódulo específico. Devuelve la database y el .html correspondiente al numero de la pregunta.  

def uno_t(request):
    primero= secc_alternativa.objects.filter(numero_respuesta_alt=1)  
    tp1= alternativas_tp.objects.filter(numero_respuesta_alt=1)
    return render(request, 'terminos1.html',{'primero':primero,'tp1':tp1})  

def dos_t(request):
    segundo= secc_alternativa.objects.filter(numero_respuesta_alt=2)  
    tp2= alternativas_tp.objects.filter(numero_respuesta_alt=2)
    return render(request, 'terminos2.html',{'segundo':segundo,'tp2':tp2})

def tres_t(request):
    tercero= secc_alternativa.objects.filter(numero_respuesta_alt=3)  
    tp3= alternativas_tp.objects.filter(numero_respuesta_alt=3)
    return render(request, 'terminos3.html',{'tercero':tercero,'tp3':tp3}) 

def cuatro_t(request):
    cuarto= secc_alternativa.objects.filter(numero_respuesta_alt=4)  
    tp4= alternativas_tp.objects.filter(numero_respuesta_alt=4)
    return render(request, 'terminos4.html',{'cuarto':cuarto,'tp4':tp4})  

def cinco_t(request):
    quinto= secc_alternativa.objects.filter(numero_respuesta_alt=5)  
    tp5= alternativas_tp.objects.filter(numero_respuesta_alt=5)
    return render(request, 'terminos5.html',{'quinto':quinto,'tp5':tp5})


def seis_t(request):
    sexto= secc_alternativa.objects.filter(numero_respuesta_alt=6)
    tp6= alternativas_tp.objects.filter(numero_respuesta_alt=6)
    return render(request, 'terminos6.html',{'sexto':sexto,'tp6':tp6}) 

def siete_t(request):
    sept= secc_alternativa.objects.filter(numero_respuesta_alt=7)  
    tp7= alternativas_tp.objects.filter(numero_respuesta_alt=7)
    return render(request, 'terminos7.html',{'sept':sept,'tp7':tp7})  

def ocho_t(request):
    octavo= secc_alternativa.objects.filter(numero_respuesta_alt=8)  
    tp8= alternativas_tp.objects.filter(numero_respuesta_alt=8)
    return render(request, 'terminos8.html',{'octavo':octavo,'tp8':tp8})

def nueve_t(request):
    noveno= secc_alternativa.objects.filter(numero_respuesta_alt=9)  
    tp9= alternativas_tp.objects.filter(numero_respuesta_alt=9)
    return render(request, 'terminos9.html',{'noveno':noveno,'tp9':tp9}) 

def diez_t(request):
    decimo= secc_alternativa.objects.filter(numero_respuesta_alt=10)  
    tp10= alternativas_tp.objects.filter(numero_respuesta_alt=10)
    return render(request, 'terminos10.html',{'decimo':decimo,'tp10':tp10})  

def once_t(request):
    onceavo= secc_alternativa.objects.filter(numero_respuesta_alt=11) 
    tp11= alternativas_tp.objects.filter(numero_respuesta_alt=11) 
    return render(request, 'terminos11.html',{'onceavo':onceavo,'tp11':tp11})

def doce_t(request):
    doceavo= secc_alternativa.objects.filter(numero_respuesta_alt=12) 
    tp12= alternativas_tp.objects.filter(numero_respuesta_alt=12) 
    return render(request, 'terminos12.html',{'doceavo':doceavo,'tp12':tp12}) 

def trece_t(request):
    treceavo= secc_alternativa.objects.filter(numero_respuesta_alt=13) 
    tp13= alternativas_tp.objects.filter(numero_respuesta_alt=13) 
    return render(request, 'terminos13.html',{'treceavo':treceavo,'tp13':tp13})  

def catorce_t(request):
    catorceavo= secc_alternativa.objects.filter(numero_respuesta_alt=14)  
    tp14= alternativas_tp.objects.filter(numero_respuesta_alt=14)
    return render(request, 'terminos14.html',{'catorceavo':catorceavo,'tp14':tp14})

def quince_t(request):
    quinceavo= secc_alternativa.objects.filter(numero_respuesta_alt=15)  
    tp15= alternativas_tp.objects.filter(numero_respuesta_alt=15)
    return render(request, 'terminos15.html',{'quinceavo':quinceavo,'tp15':tp15}) 

def diesciseis_t(request):
    diesciseis= secc_alternativa.objects.filter(numero_respuesta_alt=16)  
    tp16= alternativas_tp.objects.filter(numero_respuesta_alt=16)
    return render(request, 'terminos16.html',{'diesciseis':diesciseis,'tp16':tp16})  

def diescisiete_t(request):
    diescisiete= secc_alternativa.objects.filter(numero_respuesta_alt=17)  
    tp17= alternativas_tp.objects.filter(numero_respuesta_alt=17)
    return render(request, 'terminos17.html',{'diescisiete':diescisiete,'tp17':tp17})

def diesciocho_t(request):
    diesciocho= secc_alternativa.objects.filter(numero_respuesta_alt=18)  
    tp18= alternativas_tp.objects.filter(numero_respuesta_alt=18)
    return render(request, 'terminos18.html',{'diesciocho':diesciocho,'tp18':tp18}) 

def diescinueve_t(request):
    diescinueve= secc_alternativa.objects.filter(numero_respuesta_alt=19)  
    tp19= alternativas_tp.objects.filter(numero_respuesta_alt=19)
    return render(request, 'terminos19.html',{'diescinueve':diescinueve,'tp19':tp19})  

def veinte_t(request):
    veinte= secc_alternativa.objects.filter(numero_respuesta_alt=20)  
    tp20= alternativas_tp.objects.filter(numero_respuesta_alt=20)
    return render(request, 'terminos20.html',{'veinte':veinte,'tp20':tp20})

def veintiuno_t(request):
    veintiuno= secc_alternativa.objects.filter(numero_respuesta_alt=21) 
    tp21= alternativas_tp.objects.filter(numero_respuesta_alt=21) 
    return render(request, 'terminos21.html',{'veintiuno':veintiuno,'tp21':tp21}) 

def veintidos_t(request):
    veintidos= secc_alternativa.objects.filter(numero_respuesta_alt=22)  
    tp22= alternativas_tp.objects.filter(numero_respuesta_alt=22)
    return render(request, 'terminos22.html',{'veintidos':veintidos,'tp22':tp22})  

def veintitres_t(request):
    veintitres= secc_alternativa.objects.filter(numero_respuesta_alt=23)  
    tp23= alternativas_tp.objects.filter(numero_respuesta_alt=23)
    return render(request, 'terminos23.html',{'veintitres':veintitres,'tp23':tp23})

def veinticuatro_t(request):
    veinticuatro= secc_alternativa.objects.filter(numero_respuesta_alt=24) 
    tp24= alternativas_tp.objects.filter(numero_respuesta_alt=24) 
    return render(request, 'terminos24.html',{'veinticuatro':veinticuatro,'tp24':tp24}) 

def veinticinco_t(request):
    veinticinco= secc_alternativa.objects.filter(numero_respuesta_alt=25)  
    tp25= alternativas_tp.objects.filter(numero_respuesta_alt=25)
    return render(request, 'terminos25.html',{'veinticinco':veinticinco,'tp25':tp25})  

def veintiseis_t(request):
    veintiseis= secc_alternativa.objects.filter(numero_respuesta_alt=26)  
    tp26= alternativas_tp.objects.filter(numero_respuesta_alt=26)
    return render(request, 'terminos26.html',{'veintiseis':veintiseis,'tp26':tp26})

def veintisiete_t(request):
    veintisiete= secc_alternativa.objects.filter(numero_respuesta_alt=27)  
    tp27= alternativas_tp.objects.filter(numero_respuesta_alt=27)
    return render(request, 'terminos27.html',{'veintisiete':veintisiete,'tp27':tp27}) 

def veintiocho_t(request):
    veintiocho= secc_alternativa.objects.filter(numero_respuesta_alt=28)  
    tp28= alternativas_tp.objects.filter(numero_respuesta_alt=28)
    return render(request, 'terminos28.html',{'veintiocho':veintiocho,'tp28':tp28})  

def veintinueve_t(request):
    veintinueve= secc_alternativa.objects.filter(numero_respuesta_alt=29)  
    tp29= alternativas_tp.objects.filter(numero_respuesta_alt=29)
    return render(request, 'terminos29.html',{'veintinueve':veintinueve,'tp29':tp29})

def treinta_t(request):
    treinta= secc_alternativa.objects.filter(numero_respuesta_alt=30)  
    tp30= alternativas_tp.objects.filter(numero_respuesta_alt=30)
    return render(request, 'terminos30.html',{'treinta':treinta,'tp30':tp30}) 

