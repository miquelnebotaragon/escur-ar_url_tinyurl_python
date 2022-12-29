<h1 align="center"><b>Escurçar URL amb el servei de TinyURL i Python</b></h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">
    <img alt="License: GPL--3+" src="https://img.shields.io/badge/License-GPL--3+-yellow.svg" />
  </a>
  <a href="https://twitter.com/miquelnebot" target="_blank">
    <img alt="Twitter: Miquel Nebot" src="https://img.shields.io/twitter/follow/miquelnebot.svg?style=social" />
  </a>
</p>
<div align="center"><img src="https://user-images.githubusercontent.com/57944755/209711233-15963b37-2a47-4d86-827d-fe5af86343b5.png"></div>

# 👁️‍🗨️ Introducció
De manera recurrent en la nostra tasca diària volem fer més curts els enllaços de les pàgines que visitam i volem compartir a dins documents, pàgines... Per això tenim a la nostra disposició gran quantitat de pàgines com TinyURL que ens faciliten la tasca. Però, t'interessa saber com fer-ho a través de Python. Revisa la informació que trobaràs a continuació per descobrir com, amb 5 línies de codi, som capaços de treure el resultat desitjat.

# 💻 Escenari
Linux Mint 21.1 Vera Ubuntu based 20.04

# 0️⃣ Abans de començar
1. Haurem de tenir instal·lat Python en el nostre ordinador. Verificarem si disposam d'ell i la seva versió mitjançant la comanda següent a dins el Terminal (Ctrl+Alt+T): 

```console
user@kubuntu-mnebot:~$ python3 -V
```
Si no el tenim instal·lat, el podem aconseguir fàcilment mitjançant la comanda:
```console
user@kubuntu-mnebot:~$ sudo apt install python3
```
2. Per a la importació del mòdul necessari (**pyshorteners**) és imprescindible disposar al nostre ordinador de l'administrador de paquets **PIP**, per això, i si no ho hem fet amb anterioritat, l'instal·larem a través de la terminal de la següent maner
```console
user@kubuntu-mnebot:~$ sudo apt install python3-pip
```
3. Instal·larem finalment el mòdul necessari responsable d'escurçar la URL proposada:
```console
user@kubunu-mnebot:~$ sudo pip install pyshorteners
```

# 👇 Descàrrega i execució
Copiarem el codi següent 👇 a un arxiu amb extensió **.py** al nostre ordinador (per exemple **escurcar_url_tinyurl_python.py**) per a la seva posterior execució: 
<p></p>📝 Descàrrega de l'arxiu .py des d'<a href="https://github.com/miquelnebotaragon/baixar_youtube_python/blob/main/baixar_youtube.py" target="_blank">aquí</a>.

# ➕ Informació
1️⃣ L'arxiu **.py** ha estat comentat al detall (#) per tal de possibilitar l'anàlisi del seu funcionament.<p></p>
2️⃣ Aquesta aplicació ha estat creada únicament amb finalitat d'estudi i divulgació. No em faig responsable dels possibles problemes ni prejudicis que pugui provocar el seu ús.<p></p>
