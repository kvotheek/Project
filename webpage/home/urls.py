from django.urls import path

from .views import * #Se importan todas las funciones de la seccion vistas

# path (url visible, funcion en .views, name= nombre del archivo.html )
urlpatterns= [
    
 path('', inicio, name='inicio'), # se visualiza la pagina estudio.html al llegar al home de la app estudio, lo que sería el home de las alternativas

# url del registro, login y logout de la página.
path("signup/", Signup, name="signup"),
path("login/", Login, name="login"),
path("logout/", Logout, name="logout"),
]