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

Poner en práctica los conceptos aprendidos durante la carrera de Data Scienst y sobreponerme a los errores de código y dificutades propias del desarrollo del proyecto. Adquirir las habilidades necesarias que me permitan desempeñarme satisfactoriamente en el mundo laboral.

- **Transformación y Limpieza de Datos:** Optimizar el proceso de ETL con el fin de entender mejor los datos y tomar decisiones acertadas que me permitan conservar los datos de la mejor manera posible, en pro de cumplir con la creación de las funciones solicitadas y el modelo requerido.

- **Modelo ML:** Desarrollar un modelo que recomiende videojuegos con base en la similitud del coseno.

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
Durante el desarrollo del proceso de EDA mis esfuerzos se orientaron hacia la consecución de la información justa y necesaria para la realización de las funciones y el modelo de recomendación. Por favor revisar el archivo Notebook donde se adelantó este proceso.


## Modelo ML

El modelo de ML recibe como parámetro un valor de item_id y entrega una recomendación de 5 video juegos. Se utilizó la similitud del coseno para llevar a feliz término el modelo. Se usan los tres conjuntos de datos y se crea un dataframe nuevo con las columnas title y genres para proceder a la creación de los vectores y aplicar la similitud del coseno, al final se lleva a cabo la función de recomendacion. Para el despliegue en Render se crea un dataframe con item_id y recommended para poder adelantar el despliegue. 



**Git:** Creé un repositorio de Git para el proyecto **(https://github.com/willflorez/machine-learning1.0)** .

**Despliegue en Render:** Con Render se despliega la API. [API en ejecución](https://proyecto-machine-learning-1-0.onrender.com/docs). En la web se puede hacer el uso de las funciones y del modelo de recomendación.

## Video

<div align="center">

link al video explicativo
[https://www.loom.com/share/44560780b5a94f229ede5b18300114c3?sid=1441e474-2bbf-412b-953e-29e8e20d6608]

</div>