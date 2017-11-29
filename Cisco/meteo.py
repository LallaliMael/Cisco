# -*- coding: utf-8 -*-

import parole
import urllib.request
import json
import requests
import time 
import datetime

def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%X')
    return converted_time

def meteo(ville):
 try: 
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
   reponse = 'Il fait particulièrment froid, aujourdh\'ui'  + temp + ' la température maximal est de {}'.format(data["temp_max"]) + (" degré") + ' et la température minimale de {}'.format(data["temp_min"]) + (" degré")
  elif int('{}'.format(data["temp_max"])) >= 28:
   reponse = 'Il fait particulièrment chaud, aujourdh\'ui' + temp + ' la température maximal est de {}'.format(data["temp_max"]) + (" degré") + ' et la température minimale de {}'.format(data["temp_min"]) + (" degré")   
  else:
    reponse = 'A ' + ville +  temp + ' la bas, la température maximal est de {}'.format(data["temp_max"]) + (" degré") + ' et la température minimale de {}'.format(data["temp_min"]) + (" degré")
  parole.dit(reponse)
 except:
  parole.dit("Désolé, mais je suis incapable de trouver la ville que vous m'avez demandé")
