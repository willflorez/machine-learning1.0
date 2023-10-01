# PrimerProyectoIndividualHenry
<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

## Índice 
<!-- TABLA DE CONTENIDO -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>  
    <li><a href="#Introducción">Introducción</a></li>
    <li><a href="#Objetivo">Objetivo</a></li>
    <li><a href="#pila-de-tecnologías">Pila de Tecnologías</a></li>
    <li><a href="#ETL">ETL</a></li>
    <li><a href="#EDA">EDA</a></li>
    <li><a href="#funciones-api">Funciones API</a></li>
    <li><a href="#modelo-ml">Modelo ML</a></li>
    <li><a href="#Deployment">Deployment</a></li>
    <li><a href="#Video">Video</a></li>
  </ol>
</details>

## Introducción

El presente proyecto tiene que ver con la puesta en práctica de todo lo aprendido en la carrera de Data de Henry.
Busco personalmente la apropiación de los conocimientos de ETL, EDA y Machine Learning.
Es un desafío para mi enfrentarme a este Dataset y lograr realizar un modelo de Machine Learning funcional.
## Objetivo

Desarrollar mis aptitudes de análisis con el Dataset entregado y llevar a feliz término el proyecto cumpliendo con la entrega de un modelo de Machine Learning y las funciones solicitadas desplegadas en Render.

- **Transformación y Limpieza de Datos:** Optimizar el proceso de ETL con el fin de entender mejor los datos y tomar decisiones acertadas que me permitan conservar los datos de la mejor manera posible, en pro de cumplir con la creación de las funciones solicitadas y el modelo requerido.

- **Desarrollo de API:** Entregar una API que arroje resultados acordes al contenido de los diferentes Dataset.

- **Modelo ML:** Desarrollar un modelo que recomiende videojuegos con base en la similitud del coseno.

**Analisis Exploratorio de Datos** Se busca encontrar patrones entre los datos, su relación con cada uno de ellos, ver si hay algun patron interesante entre cada uno de ellos.

+ def **recomendacion_juego( *`id de producto`* )**:
    Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

## Pila de Tecnologías

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

## Proceso de ETL

Para ETL consideré cada conjunto de datos por aparte. Aplicando transformaciones donde el tipo de cada columna fuera el mismo. Estudié cada columna y sus relaciones para entender que tipo de información me iba a encontrar y fui de a poco diseñando en mi mente una posible solución con el propósito de crear las funciones que el proyecto propone. En cada uno de los tres conjuntos de datos use la función .json_normalize y procedí a eliminar nulos en el caso donde se aplicaba, a conservar los años en aquellas columnas donde la información era fechas y a desanidar columnas con datos anidados. De esa misma manera los registros duplicados fueron eliminados. Invito a revisar, para conocer los detalles, los tres archivos notebook creados para tal proceso.



## EDA

El proceso de EDA lo centré en el conocimiento de las variables y como se relacionan entre sí. Queriendo encontrar datos que me indicarán la información mas relavante a tener en cuenta. De esta manera se obtiene por ejemplo lo siguiente: 
1. De reviews casi el 62% de los datos reflejan sentimientos neutrales, cerca del 30% sentimientos positivos hacia el juego y menos del 9% fue negativo. 
2. Cantidad de usuarios únicos que opinaron: 21432.
3. Dias de pico de reviews

*Estos procesos se desarrollaron localmente en **Visual Studio Code (VSCODE)** utilizando **Jupyter Notebook** como entorno de trabajo. La combinación de herramientas tecnológicas empleada esta basada en **Python** como lenguaje de programación, junto con librerias  como **numpy y pandas** para la manipulación de datos. Además, se utilizo **matplotlib y seaborn** para la creación de visualizaciones gráficas.*

## Funciones API

En el archivo main.py se entrega el código de las funciones solicitadas, probadas en API, preparando el proyecto para su futuro despliegue con Render

## Modelo ML

El modelo de ML de recomendación de videojuegos item-item entrega 5 recomendaciones de videojuegos. 


# Deployment

Luego de completar la implementación de **main.py** y demás archivos que componen el modelo y las funciones, el despliegue de la API se realizó de manera exitosa a través de Render, con ayuda de un **Dockerfile**:

**1. Creación de Entorno Virtual:** Se utiliza venv, lo cual permitió gestionar y separar las dependencias específicas de la API.

**2. Configuración de Archivos Necesarios:** Se llevaron a cabo las configuraciones necesarias para el despliegue, asegurando que todos los archivos necesarios estuvieran presentes. Algunos archivos son los datasets en formato parquet, el archivo de requirements.txt y el archivo .gitignore. 

**3. Inicialización de Git:** Se inició un repositorio de Git para el proyecto **(https://github.com/willflorez/individualSteam.git)** donde se evidencia el desarrollo del proyecto.

**4. Despliegue en Render:** Con Render se despliega la API. [API en ejecución](https://individualsteam.onrender.com). **(Se suguiere agregar "/docs" al final del enlace para acceder a la documentación automática creada por Swagger. Esto brinda una interfaz interactiva y detallada que describe todos los endpoints, métodos y parámetros disponibles en la API de manera clara.)**

## Video

<div align="center">

link al repositorio
[https://github.com/willflorez/machine-learning1.0]


link al video explicativo
[https://www.loom.com/share/44560780b5a94f229ede5b18300114c3?sid=1441e474-2bbf-412b-953e-29e8e20d6608]


link de render
[https://proyecto-machine-learning-1-0.onrender.com/docs]

</div>