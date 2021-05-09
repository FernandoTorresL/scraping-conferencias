# Wordcloud: Presidential conferences analysis (México)

With so many presidential conferences in México for about two years, have you ask what words are the most spoken? Who has been participated on them and what they said? Let´s go to analize them...

This proyect is based on the exercise from [Prof. Jorge Luis Novelo](https://github.com/PhinanceScientist) and his post on [LinkeId](https://www.linkedin.com/pulse/qu%C3%A9-es-lo-que-dice-el-discurso-presidencial-an%C3%A1lisis-de-luis-jorge/)

## Project stages:
- [x] Extract: Finish, main branch (some improvements on the way)
- [ ] Transform: WIP, develop and feature_* branch
- [ ] Load: To build

![Screenshot](https://s3-us-west-2.amazonaws.com/torresmxbucket/2021/02/Screen-Shot-2021-02-20-at-1.42.44.png)


### Setup

* Clone this repository

```bash
git clone git@github.com:FernandoTorresL/scraping-conferencias.git
```

* Prepare the environment

```bash
# Create and activate the environment
python3 -m venv venv
source venv/bin/activate

python3 -m pip install --upgrade pip

pip3 install wheel
pip3 install jupyter
pip3 install bs4 requests numpy
pip3 install pandas
pip3 install nltk wordcloud stop-words
```

or use the requirements.txt file:

```bash
# Create and activate the environment
python3 -m venv venv
source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

### Use the Jupyter Notebook

* Change to the notebook directory

```bash
cd notebook
```

* Execute Jupyter Notebook (with active environment)

```bash
./venv/bin/jupyter notebook
```

* Open *scraping-conferencias.ipynb*

### Use the Scrapy spider
```bash
cd project_live/extract/wordcloud_conferences
scrapy crawl get_transcriptions
```
* It create a data_{timestamp*}.json and .csv files on project_live/extract/data_extracted/

*UTC date and time, in ISO format


## Transform Stage:
### WIP (Work in Progress)

Future updates and automatization in progress (May 09, 2021)

---

### Follow me

### [fertorresmx.dev](https://www.fertorresmx.dev/)

#### :globe_with_meridians: Twitter, Instagram: [@fertorresmx](https://www.twitter/fertorresmx)




---
# Wordcloud: análisis de las conferencias presidenciales (México)

Con tantas conferencias presidenciales en México desde hace dos años, ¿te has preguntado qué palabras son las que más se mencionan en ellas? ¿Quiénes han participado y qué han dicho? Vamos a analizarlo...

Éste proyecto está inspirado por el [ejercicio del Prof. Jorge Luis Novelo](https://github.com/PhinanceScientist) y su post en [LinkeId](https://www.linkedin.com/pulse/qu%C3%A9-es-lo-que-dice-el-discurso-presidencial-an%C3%A1lisis-de-luis-jorge/)

## Etapas del proyecto:
- [x] Extract (Extracción): Finalizada, main branch (con algunas mejoras en progreso)
- [ ] Transform (Transformación): WIP, develop and feature_* branch
- [ ] Load (Carga): Pendiente

![Screenshot](https://s3-us-west-2.amazonaws.com/torresmxbucket/2021/02/Screen-Shot-2021-02-20-at-1.42.44.png)

### Setup

* Clonar el repositorio

```bash
git clone git@github.com:FernandoTorresL/scraping-conferencias.git
```

* Preparar el ambiente

```bash
# Crear y activar el ambiente
python3 -m venv venv
source venv/bin/activate

python3 -m pip install --upgrade pip

pip3 install wheel
pip3 install jupyter
pip3 install bs4 requests numpy
pip3 install pandas
pip3 install nltk wordcloud stop-words
pip3 install wheel scrapy autopep8
```

o utilicemos el archivo requirements.txt:

```bash
# Crear y activar el ambiente
python3 -m venv venv
source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

### Utilizar archivo Jupyter Notebook

* Cambia al directorio notebook

```bash
cd notebook
```

* Ejecuta Jupyter Notebook (dentro del ambiente)

```bash
./venv/bin/jupyter notebook
```

* Abre el notebook *scraping-conferencias.ipynb*

### Utilizar spider de Scrapy
```bash
cd project_live/extract/wordcloud_conferences
scrapy crawl get_transcriptions
```
* Se generará el archivo data_{timestamp*}.json y .csv en la carpeta project_live/extract/data_extracted/

* Con fecha y tiempo UTC, en formato ISO

## Etapa de Transformación de datos:
### WIP (Work in Progress)

Actualizaciones futuras y automatización en progreso (09-mayo-2021)

------

#### Follow me 
[fertorresmx.dev](https://fertorresmx.dev/)

#### :globe_with_meridians: [Twitter](https://twitter.com/FerTorresMx), [Instagram](https://www.instagram.com/fertorresmx/): @fertorresmx

#### :globe_with_meridians: Twitter, Instagram: [@fertorresmx](https://www.twitter/fertorresmx)
