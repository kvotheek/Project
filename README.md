# Project
Actualizado al 12/09/2022

Este proyecto está realizado por Fernanda Catalán con la autorización del Doctor Juan Olivos Pérez con la motivación de colaborarle en su proyecto de crear una plataforma que permita a los alumnos de medicina poner en práctica su conocimientos respecto al área de radiología y permitir la realización de diagnósticos mediante observación de éstas imágenes.

Desarrollado en un ambiente virtual ocupando virtualenv (venv version 20.14.1) con interfaz Django (version 4.0.6) y principal lenguaje de programación Python en su versión 3.10.4
Se debe tener instalado Visual Studio Code y la extension de Python. Cada uno posee una licencia libre.

La fecha de expiración (EOL) de los programas utilizados son los siguientes: 
- Django 4.0: soporte extendido 04/2023 (https://www.djangoproject.com/download/) // actualizaciones:  https://docs.djangoproject.com/en/4.1/howto/upgrade-version/
- Python: 3.10: 04/10/2026 (https://endoflife.date/python)
- Virtualenv 20.14 solo va sacando nuevas actualizaciones, pero hasta ahora no tiene fecha de caducidad. 



La base de datos cuenta con 30 imágenes patológicas obtenidas de la página radiopaedia con su debido consentimiento, además de un banco de 30 preguntas con sus respectivas alternativas y respuestas correctas. Los datos actualmente se encuentran en SQLite3.

REQUISITOS:
Tener instalado los siguientes:
     - Github Desktop (Disponible en https://desktop.github.com/)
     - Visual Studio Code (Disponible en https://code.visualstudio.com/download)
     - Python version 3.10.4 (Disponible en: https://www.python.org/downloads/release/python-3104/)

NOTA: Todo lo escrito entre comillas dobles quiere decir que se puede copiar y pegar o se debe modificar para copiar y pegar en donde se indique.

Desde GITHUB DESKTOP:
I. Clonar el repositorio desde github desktop y almacenarlo en la carpeta que mas plasca. (por defecto la carpeta sera documentos/github/, pero se puede cambiar la ruta para guardar el proyecto en  el escritorio)

Pasos a seguir:
1. Instalar carpeta de ambiente virutal:
     - Abrir el cmd e ir a la ruta en donde se encuentra el proyecto hasta la carpeta "webpage"
     - Ejecutar el comando "python -m virtualenv venv" (Esto creará una carpeta llama "venv" dentro de la carpeta "webpage")

2. Habilitar la ejecución de Scripts.
    
     - Abrir el powershell de windows: en la barra de busqueda buscar "Windows Powershell" y ejecutar como administrador. 
     - Escribir o copiar y pegar lo siguiente: "Get-ExecutionPolicy"
     - Una vez dado el enter, debería aparecer un mensaje que dice Restricted. Se debe cambiar escribiendo o copiando y pegando lo siguiente: "Set-ExecutionPolicy Unrestricted"
     - Indicar que [S]Si. Se puede escribir "Si" o una "S".
     - Para corroborar volver a escribir "Get-ExecutionPolicy". La cual debería decir "Unrestricted"

Para poder correr el código se debe:
1. Abrir Visual Studio Code

2. Arrastrar la carpeta "webpage" y soltarla en la ventana de VSCode 

3. Abrir un nuevo terminal (atajo en windows: ctrl + shift + ñ) y activar el ambiente virtual colocando lo siguiente: 
     "& c:/Users/%username%/%ruta donde se encuentra el proyecto%/Project/webpage/venv/Scripts/Activate.ps1"  

Modificar lo que está entre porcentajes con el username y la ruta en donde está ubicado el proyecto que por defecto es .../Documents/Github/... . 
La ruta donde se encuentre el proyecto puede ser documentos, escritorio, etc. Luego dar a enter y aparecerá un "(venv)"  en la seccion izquierda de la terminal. Similar a esto:
     (venv) PS C:\Users\%username%\%ruta%\webpage

4. Instalar la librería de Pillow una vez activado el ambiente, con la siguiente línea: "pip install Pillow". Esto permitirá ver las imágenes.

4. Luego en la terminal escribir y darle a enter a cada una de las siguientes líneas de código en el orden en que están escritas: 
     "python manage.py makemigrations"
     "python manage.py migrate"
     Si ninguna de ellas da un error, entonces escribir:
     "python manage.py runserver" 

5. Esto ultimo desplegará un mensaje y se debe apretar la tecla CTRL y hacer click donde aparezca el siguiente enlace: http://127.0.0.1:8000/ 

6. Será redirigido a la página


v1.1 5/10/2022
Tiene actualizaciones en el layout sobre el cambio de color en background
se agrega la barra de navegación segmentadad dependiendo del usuario que ingresa
Cambios en visualizacion de botones