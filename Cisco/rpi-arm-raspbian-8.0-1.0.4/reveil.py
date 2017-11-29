# -*- coding: utf-8 -*-

import parole
import urllib.request
import json
import requests
import time 
import datetime
import os


chemin_vers_fichier_de_note = "C:/Users/lallali mael/Desktop/Cisco version modulaire/Nouveau dossier/reveil.txt"

ville = "indiquez le nom de votre ville"

def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%X')
    return converted_time

def meteo_reveil(ville):
  print("http://api.openweathermap.org/data/2.5/weather?q=" + ville + "&units=metric&appid=eec7b314c20283986153a77fcc6d49cc")
  url = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + ville + "&units=metric&appid=eec7b314c20283986153a77fcc6d49cc")
  output = url.read().decode('utf-8')
  raw_api_dict = json.loads(output)
  url.close()
  data = dict(
  city=raw_api_dict.get('name'),
  country=raw_api_dict.get('sys').get('country'),
  temp=raw_api_dict.get('main').get('temp'),
  temp_max=raw_api_dict.get('main').get('temp_max'),
  temp_min=raw_api_dict.get('main').get('temp_min'),
  humidity=raw_api_dict.get('main').get('humidity'),
  pressure=raw_api_dict.get('main').get('pressure'),
  sky=raw_api_dict['weather'][0]['description'],
  sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
  sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
  wind=raw_api_dict.get('wind').get('speed'),
  wind_deg=raw_api_dict.get('deg'),
  dt=time_converter(raw_api_dict.get('dt')),
  cloudiness=raw_api_dict.get('clouds').get('all')
   )
  m_symbol = '\xb0' + 'C'
  m_symbol = '\xb0' + 'C'
  cielle =  data["sky"]
  if cielle == ("Clear"):
   ciel = ("claire")
   temp = " ,Le temps est " + ciel
  elif cielle == ("Clouds") or cielle == ("broken clouds"):
   ciel = ("nuageux")
   temp = " ,Le temps est " + ciel
  elif cielle == ("Sunny"):
   temp = " ,Le temps est " + ciel
   ciel = ("ensolleilé")
   temp = " ,Le temps est " + ciel
  elif cielle == ("clear sky"):
   ciel = ("dégagé")
   temp = " ,Le temps est " + ciel
  elif cielle == ("overcasts clouds"):
   ciel = ("éxtrémement nuageux")
   temp = " ,Le temps est " + ciel
  elif cielle == ("scattered clouds"):
   ciel = ("nuageux") 
   temp = " ,Le temps est " + ciel
  else:
   temp = ""
  
  if int('{}'.format(data["temp_min"])) <= 0:
   reponse = 'Il est temps de vous levez, monsieur ,Il fait particulièrment froid, aujourdh\'ui'  + temp + ' la température maximal est de {}'.format(data["temp_max"]) + (" degré") + ' et la température minimale de {}'.format(data["temp_min"]) + (" degré")
  elif int('{}'.format(data["temp_max"])) >= 28:
   reponse = 'Il est temps de vous levez, monsieur ,Il fait particulièrment chaud, aujourdh\'ui' + temp + ' la température maximal est de {}'.format(data["temp_max"]) + (" degré") + ' et la température minimale de {}'.format(data["temp_min"]) + (" degré")   
  else:
    reponse =  "Il est temps de vous levez, monsieur ,la température maximal est de {}'.format(data["temp_max"]) + (" degré") + ' et la température minimale de {}'.format(data["temp_min"]) + (" degré")"
  parole.dit(reponse)






def reveil():
 conteur_reveil = 1
 reveil   = chemin_vers_fichier_de_note
 while conteur_reveil == 1: 
  f = open(reveil,'r')
  lignes  = f.readlines()
  f.close()
  minute = (time.strftime("%H:%M")) 
  date = time.strftime('%D')
  for ligne in lignes:
    if date in ligne and minute in ligne:
      
      ligner = ligne.replace(date,'')
      ligner = ligner.replace(minute,'') 
      
      meteo_reveil()

      mon_fichier = open(reveil, "r")
      ancien_contenu = mon_fichier.read()
      mon_fichier.close          
      nouveau_contenu = ancien_contenu.replace(ligne,'')
      print(nouveau_contenu)         
      mon_fichier = open(chemin_vers_fichier_de_note, "w") 
      mon_fichier.write(nouveau_contenu)
      mon_fichier.close()