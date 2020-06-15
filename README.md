# Datos Abiertos - Obras del MOPC

_Con este proyecto se puede obtener los datos en formato csv acerca de las obras realizadas por el Ministerio de Obras Públicas y Comunicaciones._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local._

### Pre-requisitos 📋

_Para poder utilizar este script debes tener instalado Python (recomendado Python 3.8), el framework scrapy y el IDE PyCharm, aunque puedes usar cualquier IDE de tu preferencia._

En los siguientes enlaces podrás cononcer cómo descargar e instalar lo mencionado:
- Python: https://wiki.python.org/moin/BeginnersGuide/Download
- Scrapy: https://docs.scrapy.org/en/latest/intro/install.html
- PyCharm: https://www.jetbrains.com/es-es/pycharm/download/

### Instalación 🔧

1. Dirígete al repositorio de este proyecto y haz click en "Clone or Download" y ["Download as Zip"](https://github.com/alesservin/Datos-Abiertos---Obras-del-MOPC/archive/master.zip)

2. Descomprime el archivo Zip y ubica la carpeta en el directorio de archivos de tu usuario. Ejemplo: C:\Users\Acer


## Ejecutando el scrip ⚙️

1. Inicia la aplicación PyCharm

2. Abre el proyecto de la siguiente manera: En el PyCharm, haz click en File -> Open... y selecciona la carpeta que contiene el proyecto, el que ubicaste en el directorio de archivos de tu usuario. Finalmente haz click en Ok y espera a que carga finalice.

3. En la terminal del PyCharm ejecuta el siguiente comando:

```
scrapy crawl mapa -o mapa_obras.csv
```

_Una vez finalizada la ejecución, podrás observar que en la carpeta del proyecto se generó un archivo llamado mapa_obras.csv (si es que no existía antes), este es el archivo que contiene los datos acerca de las obras realizadas por el MOPC._

## Entiendiendo el csv
_Para 

## Autor ✒️

**Alejandro Servín** - *Estudiante de la carrera de Ing. en Business Informatics en la Universidad Paraguayo Alemana*.

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles