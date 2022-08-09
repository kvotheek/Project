from django.db import models
from django.db.models.fields.files import ImageField
from django.db.models.fields import CharField, URLField, PositiveSmallIntegerField

# Create your models here.

class secc_alternativa(models.Model):
    #Identificador de pregunta-respuesta
    numero_respuesta_alt= PositiveSmallIntegerField(default=1)

    #Contiene las alternativas a mostrar dentro de las paginas
    alternativa_1= CharField(max_length=100, blank=True) 
    alternativa_2= CharField(max_length=100, blank=True)
    alternativa_3= CharField(max_length=100, blank=True)
    alternativa_4= CharField(max_length=100, blank=True)
    alternativa_5= CharField(max_length=100, blank=True)

    #Respuesta correcta mostrada en la pagina de respuesta
    alternativa_respuesta= CharField(max_length=100, blank=True)

    #Descripcion breve de la respuesta
    descripcion_breve = CharField(max_length=600, blank=True)

    #URL con mayor informacion de la respuesta, en ingles y en español
    url_info_esp= URLField(blank=True)
    url_info_ing= URLField(blank=True)
    

    #Imagen asociada a la patología
    imagen_con_patologia= ImageField(upload_to='estudio/images/')

    #Pregunta asociada a la patología 
    pregunta= CharField(max_length=500, blank=True)