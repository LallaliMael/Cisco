# -*- coding: utf-8 -*-

import parole
import urllib.request
import json
import requests
import time 
import datetime
import os


chemin_vers_fichier_de_note = "chemin_vers_votre_fichier_teste_de_reveil"
ville = "Indiquez le nom de votre ville"

mode_reveil = 1
global mode_reveil

def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%X')
    return converted_time

def meteo_reveil():
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
    reponse =  'Il est temps de vous levez, monsieur ,la température maximal est de {}'.format(data["temp_max"]) + (" degré") + ' et la température minimale de {}'.format(data["temp_min"]) + (" degré")
  parole.dit(reponse)


def reveil():
 conteur_reveil = 1
 reveil   = chemin_vers_fichier_de_note
 while 1: 
  if mode_reveil == 1: 
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
  else:
   jour = time.strftime('%A')
   heure = time.strftime('%H:%M')   
   if date == ("Monday") and (heure) == ("07:05") or jour == ("Tuesday") and (heure) == ("07:05") or jour == ("Wednesday") and (heure) == ("07:05") or jour == ("Thursday") and (heure) == ("07:05") or jour == ("Friday") and (heure) == ("07:05") or jour = "Saturday" and heure = "09:05" or jour = "Sunday" and heure = "09:05"
    meteo_reveil()


def add_reveil(phrase):
 heuree = (time.strftime("%H"))
 minute =  (time.strftime("%M"))
 mois = time.strftime('%m')
 jour = time.strftime('%d')
 jour_reveil = jour
 phrase = " ".join(str(x) for x in phrase)
 
 nombre_dans_phrase = re.findall('\d+', phrase)        
 print((nombre_dans_phrase))
 
 for chiffre in nombre_dans_phrase:
  heure_h = chiffre + ("h")
  if heure_h in phrase:
    phrase = phrase.replace(chiffre+("h"),chiffre+" "+("heures "))
    print(phrase)  
 heure_reveil = heuree 
 content_french = [phrase]
 for i in content_french:
  phrase = (word_tokenize(i, language='french')) 
  print(phrase)        
 
 if ("heures") in phrase and ("une") in phrase:
  try:
   calculde = phrase.index("heures") - phrase.index("une")
   if calculde == 1:
    phrase = " ".join(str(x) for x in phrase)
    phrase.replace("une","1")
  except:
    print("")
        
  content_french = [phrase]
  for i in content_french:
   phrase = (word_tokenize(i, language='french')) 
   print(phrase)        
 
 if ("heures") in phrase and ("demi") in phrase:
  try:
   calculde = phrase.index("heures") - phrase.index("demi")
   if calculde == 1:
    phrase = " ".join(str(x) for x in phrase)
    phrase.replace("demi heures","30 minutes")
  except:
    print("")

 phrase = " ".join(str(x) for x in phrase)        
 
 if ("midi") in phrase:
  phrase.replace("midi","12 heures")

 content_french = [phrase]
 for i in content_french:
   phrase = (word_tokenize(i, language='french')) 
   print(phrase)  

 if ("minutes") in phrase and ("une") in phrase:
  try:
   calculde = phrase.index("minutes") - phrase.index("une")
   if calculde == 1:
    phrase = " ".join(str(x) for x in phrase)
    phrase.replace("une","1")
  except:
    print("")
 
 phrase = " ".join(str(x) for x in phrase)
 phrase = phrase.replace("moi","")
 phrase = phrase.replace("reveil-","")
 phrase = phrase.replace("réveil-","")
 phrase = phrase.replace("réveil","")
 phrase = phrase.replace("tu","")
 phrase = phrase.replace("peut","")
 phrase = phrase.replace("me","")
 phrase = phrase.replace("réveiller","") 
 
 print(phrase)  
 
 if ("aprés") not in phrase and ("demain") in phrase and ("après-demain")not in phrase:
  minute_rev = ("00")
  if ("heures") in phrase or ("minutes") in phrase:
   nombre_dans_phrase = re.findall('\d+', phrase)        
   print(nombre_dans_phrase)
   content_french = [phrase]
   for i in content_french:
    phrase = (word_tokenize(i, language='french'))  
   heure_rev = heuree
   heure_reveil = heure_rev + (":") + minute_rev
   
   try:  
    for chiffre in nombre_dans_phrase:   
     calcule_heure = phrase.index("heures") - phrase.index(chiffre)
     if calcule_heure == 1: 
       heure_rev = chiffre
       print(heure_rev)
   except:
    print("") 
   
   
   try: 
    for chiffre in nombre_dans_phrase:   
     moncalcule =  phrase.index(chiffre) - phrase.index("heures")
     print(moncalcule)
     if moncalcule == 1: 
       minute_rev = chiffre    
       print(minute_rev)
   except:
     print("")
   
   heure_reveil = heure_rev + (":") + minute_rev
   jour_reveil2 = int(time.strftime('%d')) + 1

   jour_reveil = str(jour_reveil2) + ("/") +  time.strftime('%m')
 
 elif ("demain") not in phrase:
  if ("dans") in phrase: 
   nombre_dans_phrase = re.findall('\d+', phrase)        
   print(nombre_dans_phrase)
   content_french = [phrase]
   for i in content_french:
    phrase = (word_tokenize(i, language='french')) 
   
   heure_reveil = heuree
   minute_reveil = minute
   
   try:
    for chiffre in nombre_dans_phrase:   
     cacule_heure = phrase.index("heures") - phrase.index(chiffre)
     if cacule_heure == 1: 
       heure_reveil = int(heure_reveil) + int(chiffre)
       print("heure rapel egale "+ heure_reveil)
       heure_reveil = str(heure_reveil)
   except:
     print("")

   try:
    for chiffre in nombre_dans_phrase:
     moncalcule = (phrase.index('minutes') - phrase.index(chiffre))
     print(moncalcule)
     if moncalcule == 1: 
      minute_reveil = int(minute_reveil) + int(chiffre)
      if minute_reveil < 10 and "0" not in str(minute_reveil):
        minute_reveil = "0" + str(minute_reveil)
      minute_reveil = str(minute_reveil)
      print(minute_reveil)
   except:
    
    try: 
     for chiffre in nombre_dans_phrase:
      moncalcule = (phrase.index(chiffre) - phrase.index('heures'))
      print(moncalcule)
      if moncalcule == 1:
       minute_reveil = int(minute_reveil) + int(chiffre)
       if minute_reveil < 10 and "0" not in str(minute_reveil):
        minute_reveil = "0" + str(minute_reveil)
       minute_reveil = str(minute_reveil)
       print(minute_reveil)
    except:
      print("")
   
   if int(minute_reveil) > 60:
    heure_reveil = int(heure_reveil)+1
    minute_reveil = int(minute_reveil) - 60
    if minute_reveil < 10 and "0" not in str(minute_reveil):
        minute_reveil = "0" + str(minute_reveil)
    heure_reveil = str(heure_reveil)
    minute_reveil = str(minute_reveil)  
   
   if int(heure_reveil) > 24:
    heure_reveil = int(heure_reveil) - 24  
    mois = int(mois) + 1
    mois = str(mois) 
    if heure_reveil < 10: 
     heure_reveil = "0"+str(heure_reveil) 
   
   if int(mois) < 10 and "0" not in mois:
    mois = "0" + mois

   heure_reveil = str(heure_reveil)
   
   phrase = " ".join(str(x) for x in phrase)
   phrase.replace("moi","")
   phrase.replace("dans","")
   phrase.replace(heure_reveil,"")
   phrase.replace(minute_reveil,"")
   phrase.replace("heure","")
   phrase.replace("minute","")
   phrase.replace("heures","")
   phrase.replace("minutes","")
   print(minute_reveil)
   heure_reveil = heure_reveil+":"+minute_reveil
   jour_reveil = jour+"/"+mois
   print(heure_reveil)
   print(jour_reveil)        
 
 mode_reveil = 2
 print(mode_reveil)
 if heure reveil != None and jour_reveil != None:
  mon_fichier = open(chemin_vers_fichier_de_note, "a") 
  mon_fichier.write(jour +" " + heure_reveil)
  mon_fichier.close()
