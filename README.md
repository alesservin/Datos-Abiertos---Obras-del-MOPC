# Datos Abiertos - Obras del MOPC

_Con este proyecto se puede obtener los datos en formato csv acerca de las obras realizadas por el Ministerio de Obras Públicas y Comunicaciones. Las obras son publicadas por la institución mencionada y se encuentran en formato de mapa interactivo en el siguiente [enlace](https://www.mopc.gov.py/mopcweb/index.php/unidades-y-comisiones/direcciones-y-unidades/banco-mundial/namopora-nanderape/mapa-interactivo-de-obras)_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local y te permitirá saber cómo ejecutarlo_

### Pre-requisitos 📋

_Para poder utilizar este script debes tener instalado Python (recomendado Python 3.8), el framework scrapy y el IDE PyCharm, aunque puedes usar cualquier IDE de tu preferencia._

En los siguientes enlaces podrás cononcer cómo descargar e instalar lo mencionado:
- Python: https://wiki.python.org/moin/BeginnersGuide/Download
- Scrapy: https://docs.scrapy.org/en/latest/intro/install.html
- PyCharm: https://www.jetbrains.com/es-es/pycharm/download/

### Instalación 🔧

Con git
1. Crea una carpeta en el directorio de archivos de tu usuario. Ejemplo: C:\Users\Acer
2. Abre el Git Bash en la carpeta creada.
3. Ejecuta la siguiente línea para obtener una copia del repositorio
```
git clone https://github.com/alesservin/Datos-Abiertos---Obras-del-MOPC
```


Sin git
1. Dirígete al repositorio de este proyecto y descarga los archivos del proyecto haciendo click "Clone or Download" y ["Download Zip"](https://github.com/alesservin/Datos-Abiertos---Obras-del-MOPC/archive/master.zip)

2. Descomprime el archivo Zip descargado y ubica la carpeta resultante en el directorio de archivos de tu usuario. Ejemplo: C:\Users\Acer


## Ejecutando el scrip ⚙️

1. Inicia la aplicación PyCharm

2. Abre el proyecto de la siguiente manera: En el PyCharm, haz click en File -> Open... y selecciona la carpeta que contiene el proyecto. Finalmente haz click en Ok y espera a que la carga finalice.

_**IMPORTANTE:** si el archivo mapa_obras.csv ya existe en la carpeta del proyecto, se recomienda eliminarlo antes de realizar el siguiente paso_

3. En la terminal del PyCharm ejecuta el siguiente comando:

```
scrapy crawl mapa -o mapa_obras.csv
```

_Una vez finalice la ejecución, podrás observar que en la carpeta del proyecto se generó un archivo llamado mapa_obras.csv, este es el archivo que contiene los datos acerca de las obras realizadas por el MOPC._
 
## Entendiendo el csv
_Para comprender los campos del archivo csv, se debe leer el [Diccionario de datos](Diccionario_de_datos.xlsx)_

## Autor ✒️

**Alejandro Servín** - *Estudiante de la carrera de Ing. en Business Informatics en la Universidad Paraguayo Alemana*.

## Licencia 📄

Este proyecto está bajo la licencia CC0 1.0 Universal - mira el archivo [LICENSE.md](LICENSE.md) para más detalles
