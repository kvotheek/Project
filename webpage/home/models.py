from django.db import models

from django.db.models.fields import CharField
# Create your models here.


class Registro(models.Model):
    # Se realiza el modelo estandar para el registro de un usuario
    nombre= CharField(max_length=100, blank=True) 
    apellido= CharField(max_length=100, blank=True) 
    mail=CharField(max_length=100, blank=True)  
    usuario= CharField(max_length=100, blank=True) 
    clave= CharField(max_length=100, blank=True) 



