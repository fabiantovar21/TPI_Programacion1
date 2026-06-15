# TPI\_Programacion1

**Tecnicatura Universitaria en Programación - Universidad Tecnológica Nacional.**

**Programación 1.**



**Descripción del Proyecto**

Este proyecto es una aplicación de consola desarrollada en Python 3.x. 

El sistema permite gestionar un dataset de países almacenado en un archivo CSV, 

ofreciendo herramientas de búsqueda, filtrado por rangos, ordenamiento y generación de estadísticas e indicadores clave.



**Estructura del Proyecto**

De acuerdo con los requerimientos de modularización, el código se organiza de la siguiente manera:

* **main.py:** Punto de entrada del programa y manejo del menú principal.
* **archivos.py:** Persistencia de datos (lectura y escritura del archivo paises.csv).
* **gestion.py:** Funciones para agregar, actualizar y buscar países.
* **procesamiento.py:** Lógica para el filtrado por continente/rangos y algoritmos de ordenamiento.
* **estadisticas.py:** Cálculos de promedios, valores máximos y mínimos de población/superficie.
* **validaciones.py:** Funciones auxiliares para asegurar que no existan campos vacíos ni errores de formato.
* **paises.csv:** Dataset base con la información de los países



**Instrucciones de Uso**

Sigue estos pasos para ejecutar y utilizar el Sistema de Gestión de Países:

&#x09;**1. Requisitos Previos**

&#x09;Asegurarse de que todos los archivos del proyecto (main.py, archivos.py, gestion.py, procesamiento.py, estadisticas.py, validaciones.py) 

y el dataset base (paises.csv) se encuentren en la misma carpeta raíz.



&#x09;**2. Ejecución del Sistema**

&#x09;Abre una terminal o consola de comandos en la carpeta del proyecto y ejecuta el archivo principal:

python main.py



&#x09;**3. Navegación del Menú Principal**

&#x09;Al iniciar, el sistema cargará automáticamente los datos desde paises.csv

Podrás interactuar con las siguientes opciones mediante el teclado:

* **Opción 1:** Agregar País: Ingresa el nombre, población, superficie y continente. El sistema validará que no dejes campos vacíos
* **Opción 2:** Actualizar Datos: Permite modificar exclusivamente la población y superficie de un país ya existente
* **Opción 3:** Búsqueda: Ingresa un nombre o parte de él. El sistema admite coincidencias parciales o exactas
* **Opción 4:** Filtrado Avanzado: Podrás listar países por continente o definir rangos numéricos (mínimo y máximo) para población y superficie
* **Opción 5:** Ordenamiento: Organiza la lista por nombre, población o superficie de manera ascendente o descendente
* **Opción 6:** Estadísticas: Genera automáticamente indicadores sobre el país con mayor/menor población, promedios y cantidad de países por continente



**Ejemplos de Entrada y Salida**

* **Búsqueda:** Al ingresar "Arg" en la opción de búsqueda parcial, el sistema devuelve los datos completos de "Argentina".
* **Estadísticas:** El sistema calcula automáticamente el promedio de población basándose en los registros actuales del CSV
* **Filtros:** Se pueden listar países filtrando, por ejemplo, aquellos con una superficie mayor a 1,000,000 km²



**Integrantes**

*Fabian Tovar*

*Darwing Lohn*



**Profesores**

*Ariel Enferrel*

*Martín A. García*

*Cinthia Rigoni*

**Tutores**

*Flor Camila Gubiotti - Comisión 20*

*Neyen Bianchi - Comisión 21*



**Links:**

[**Acceso al repositorio de GitHub**](https://github.com/fabiantovar21/TPI_Programacion1)

