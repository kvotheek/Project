# Project
Actualizado al 10/08/2022

Este proyecto está realizado por Fernanda Catalán con la autorización del Doctor Juan Olivos Pérez con la motivación de colaborarle en su proyecto de crear una plataforma que permita a los alumnos de medicina poner en práctica sus conocimientos de imageneología. 

Desarrollado en un ambiente virtual ocupando virtualenv (venv) con interfaz Django y principal lenguaje de programación Python en su versión 3.10.4
Se debe tener instalado Visual Studio Code y las extensiones de Python y Pylance instaladas en el. 

REQUISITOS:
Tener instalado los siguientes programas:
     - Github Desktop (Disponible en https://desktop.github.com/)
     - Visual Studio Code (Disponible en https://code.visualstudio.com/download)
     - Python version 3.10.4 (Disponible en: https://www.python.org/downloads/release/python-3104/)

NOTA: Todo lo escrito entre comillas dobles quiere decir que se puede copiar y pegar o se debe modificar para copiar y pegar en donde se indique.

Desde GITHUB DESKTOP:
I. Clonar el repositorio desde github desktop y almacenarlo en la carpeta que mas plasca. (por default la carpeta sera documentos/github/, pero se puede cambiar la ruta para guardar el proyecto en  el escritorio)

Pasos previos:
1. Descomprimir el archivo venv.rar en la misma carpeta, es decir, hacer click en "Descomprimir aquí"
2. Habilitar la ejecución de Scripts.
    
    - Abrir el powershell de windows: en la barra de busqueda buscar "Windows Powershell" y ejecutar como administrador. 
   
     - Escribir o copiar y pegar lo siguiente: "Get-ExecutionPolicy"
     
     -  Una vez dado el enter, debería aparecer un mensaje que dice Restricted. Se debe cambiar escribiendo o copiando y pegando lo siguiente: "Set-ExecutionPolicy Unrestricted"

     - Indicar que [S]Si. Se puede escribir "Si" o una "S".

     - Para corroborar volver a escribir "Get-ExecutionPolicy"


Para poder correr el código se debe:
1. Abrir Visual Studio Code

2. Arrastrar la carpeta "webpage" y soltarla en la ventana de VSCode 

3. Abrir un nuevo terminal (atajo en windows: ctrl + shift + ñ) y activar el ambiente virtual colocando lo siguiente: 
     "& c:/Users/%username%/%ruta donde se encuentra el proyecto%/Project/webpage/venv/Scripts/Activate.ps1"  

Modificar lo que está entre porcentajes con lo que se indica. 
La ruta donde se encuentre el proyecto puede ser documentos, escritorio, etc. Luego dar a enter y aparecerá un "(venv)"  en la seccion izquierda de la terminal. Similar a esto:
     (venv) PS C:\Users\%username%\%ruta%\webpage

4. Luego en la terminal escribir y darle a enter a cada una de las siguientes líneas de código en el orden en que están escritas: 
     "python manage.py makemigrations"
     "python manage.py migrate"
     Si ninguna de ellas da un error, entonces escribir:
     "python manage.py runserver" 

5. Esto ultimo desplegará un mensaje y se debe apretar la tecla CTRL y hacer click donde aparezca el siguiente: http://127.0.0.1:8000/ 

6. Será redirigido a la página