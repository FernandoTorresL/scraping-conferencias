# Wordcloud: análisis de las conferencias presidenciales (México)

Con tantas conferencias presidenciales en México desde hace dos años, ¿te has preguntado qué palabras son las que más se mencionan en ellas? ¿Quiénes han participado y qué han dicho? Vamos a analizarlo...

Éste proyecto está inspirado por el [ejercicio del Prof. Jorge Luis Novelo](https://github.com/PhinanceScientist) y su post en [LinkeId](https://www.linkedin.com/pulse/qu%C3%A9-es-lo-que-dice-el-discurso-presidencial-an%C3%A1lisis-de-luis-jorge/)

---
![Screenshot](https://s3-us-west-2.amazonaws.com/torresmxbucket/2021/02/Screen-Shot-2021-02-20-at-1.42.44.png)  

---
## Setup

* Clonar el repositorio
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
```

o utilicemos el archivo requeriments.txt:

```bash
# Crear y activar el ambiente
python3 -m venv venv
source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requeriments.txt
```

* Cambia al directorio notebook

```bash
cd notebook
```

* Ejecuta Jupyter Notebook

```bash
jupyter notebook
```

* Abre el notebook *scraping-conferencias.ipynb*

---

## WIP (Work in Progress)

Actualizaciones futuras y automatización en progreso (20-Feb-2021)

---

## Follow me

### [fertorresmx.dev](https://www.fertorresmx.dev/)

#### :globe_with_meridians: Twitter, Instagram: [@fertorresmx](https://www.twitter/fertorresmx)
