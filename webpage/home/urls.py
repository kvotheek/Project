from django.urls import path

from .views import inicio ,registro, registro_exitoso #registro esta en .views y hace el post de la informacion de registro

# path (url visible, funcion en .views, name= nombre del archivo.html )
urlpatterns= [
    
 path('', inicio, name='inicio'), # se visualiza la pagina estudio.html al llegar al home de la app estudio, lo que sería el home de las alternativas
 path('registro', registro, name='registro'),
 path('registro_exitoso',registro_exitoso, name='registro_exitoso' ),
]