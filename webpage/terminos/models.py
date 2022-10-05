from django.db import models
from django.db.models.fields import CharField, PositiveSmallIntegerField


class alternativas_tp (models.Model):
    #Identificador de pregunta-respuesta
    numero_respuesta_alt= PositiveSmallIntegerField(default=1)

    #Contiene las alternativas a mostrar dentro de las paginas
    parte_1a= CharField(max_length=100, blank=True) 
    parte_2a= CharField(max_length=100, blank=True)
    parte_3a= CharField(max_length=100, blank=True)

    respuesta_a= CharField(max_length=100, blank=True)

    #Contiene las alternativas a mostrar dentro de las paginas
    parte_1b= CharField(max_length=100, blank=True) 
    parte_2b= CharField(max_length=100, blank=True)
    parte_3b= CharField(max_length=100, blank=True)

    respuesta_b= CharField(max_length=100, blank=True)

    
    
