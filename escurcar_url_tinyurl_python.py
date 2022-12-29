#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mòduls a importar:
import pyshorteners

# Variables
url_llarga = input("Escriu la URL a escurçar: ") # Sol·licita a l'usuari URL a escurçar.
escurça = pyshorteners.Shortener() # Variable generada pel propi mòdul.

# Execució amb el servei de TinyURL:
resultat = escurça.tinyurl.short(url_llarga) # URL escurçada.

# Impressió en pantalla del resultat:
# "\033[92m" Es el codi de color necessari per treure el resultat en pantalla de color verd.

print("L\'adreça curta generada per TinyURL és: " "\033[92m" +resultat) # Impressió en pantalla del resultat.
