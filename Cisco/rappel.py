import os
import time 
import datetime
from random import choice
import parole
import re
import nltk
from nltk.tokenize import word_tokenize

liste_rappel = ['Vous m\'aviez demandé de vous rappelez : ','Je devez vous rappeller : ','Vous aviez programmé le rappel : ']
chemin_vers_fichier_de_note = "rappel.txt"

def rappel():
  conteur_rappel = 1
  rappel   = chemin_vers_fichier_de_note
  while conteur_rappel == 1: 
    f = open(rappel,'r')
    lignes  = f.readlines()
    f.close()
    minute = (time.strftime("%H:%M")) 
    date = time.strftime('%D')

    for ligne in lignes:
      if date in ligne and minute in ligne:
        ligner = ligne.replace(date,'')
        ligner = ligner.replace(minute,'')
 
        reponse = (choice(liste_rappel) + ligner)
        print(reponse)        
        parole.dit(reponse)
        mon_fichier = open(rappel, "r")
        ancien_contenu = mon_fichier.read()
        mon_fichier.close        
        
        nouveau_contenu = ancien_contenu.replace(ligne,'')
        print(nouveau_contenu)
         
        mon_fichier = open(chemin_vers_fichier_de_note, "w") 
        mon_fichier.write(nouveau_contenu)
        mon_fichier.close()

def add_rappel(phrase):
 heuree = (time.strftime("%H"))
 minute =  (time.strftime("%M"))
 mois = time.strftime('%m')
 jour = time.strftime('%d')
 
 
 nombre_dans_phrase = re.findall('\d+', phrase)
 print(nombre_dans_phrase)
 for chiffre in nombre_dans_phrase:
  heurebizzare = chiffre + ("h")
  if heurebizzare in phrase:
    phrase = phrase.replace(chiffre+("h"),chiffre+" "+("heures "))
    print(phrase)  
 
 if ("une minutes"):
  phrase = phrase.replace("une minutes","1 minutes") 
 
 if ("une heures"):
  phrase = phrase.replace("une minutes","1 heures")

 content_french = [phrase]
 for i in content_french:
   phrase = (word_tokenize(i, language='french'))
 
 
 
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
 phrase = phrase.replace("rappel-moi","") 
 phrase = phrase.replace("rappelle-moi","") 
 phrase = phrase.replace("rappelle","") 
 phrase = phrase.replace("rappel","") 
 
 print(phrase)  
 
 if ("demain") in phrase and ("après-demain") not in phrase and ("après") not in phrase:
  if ("soir") not in phrase and ("matin") not in phrase and ("après-midi") not in phrase and ("minute") not in phrase and ("heure") not in phrase:
   print("voila lsource")
   phrase.replace(" demain ","")
   jour = int(jour)
   jour = jour + 1
   jour = str(jour)
   mon_fichier = open(chemin_vers_fichier_de_note, "a") 
   mon_fichier.write("\n" + heuree + (":") + minute + (" ") + mois + ("/") + (jour) + ("/")+(time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close()    
  elif ("soir") in phrase and ("matin") not in phrase and ("après-midi") not in phrase and ("minute") not in phrase and ("heure") not in phrase:
   phrase.replace(" demain ","" )
   jour = int(jour)
   jour = jour + 1
   jour = str(jour)
   mon_fichier = open(chemin_vers_fichier_de_note, "a") 
   mon_fichier.write("\n" + "19" + (":") + "00" + (" ") + mois + ("/") + (jour) +("/")+(time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close()
 
  elif ("soir") not in phrase and ("matin") in phrase and ("après-midi") not in phrase and ("minute") not in phrase and ("heure") not in phrase:
   phrase.replace(" demain ","")
   jour = int(jour)
   jour = jour + 1
   jour = str(jour)
   mon_fichier = open(chemin_vers_fichier_de_note, "a") 
   mon_fichier.write("\n" + "10" + (":") + "00" + (" ") + mois + ("/") + (jour) + ("/") + (time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close()
 
  elif ("soir") not in phrase and ("matin") not in phrase and ("après-midi") in phrase and ("minute") not in phrase and ("heure") not in phrase:
   phrase.replace(" demain ","")
   jour = int(jour)
   jour = jour + 1
   jour = str(jour)
   mon_fichier = open(chemin_vers_fichier_de_note, "a") 
   mon_fichier.write("\n" + "15" + (":") + "00" + (" ") + mois + ("/") + (jour) + ('/')+ (time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close() 
 
  elif ("heures") in phrase or ("minutes") in phrase:
   nombre_dans_phrase = re.findall('\d+', phrase)        
   print(nombre_dans_phrase)
   content_french = [phrase]
   for i in content_french:
    phrase = (word_tokenize(i, language='french'))  
   heure_rappel = heuree
   minute_rappel = minute
   
   try:  
    for chiffre in nombre_dans_phrase:   
     calcule_heure = phrase.index("heures") - phrase.index(chiffre)
     if calcule_heure == 1: 
       heure_rappel = chiffre
       print(heure_rappel)
   except:
    print("") 
   
   minute_rappel = ("00")
   try: 
    for chiffre in nombre_dans_phrase:   
     moncalcule = phrase.index('minutes') - phrase.index(chiffre)
     print(moncalcule)
     if moncalcule == 1: 
       minute_rappel = chiffre    
       print(minute_rappel)
   except:
     print("")
   
   try: 
    for chiffre in nombre_dans_phrase:   
     moncalcule = phrase.index(chiffre) - phrase.index("heures")
     print(moncalcule)
     if moncalcule == 1: 
       minute_rappel = chiffre    
       print(minute_rappel)
   except:
     print("")
   
   if int(mois) < 10 and "0" not in mois:
    mois = "0" + mois

   phrase = " ".join(str(x) for x in phrase)
   phrase = phrase.replace("dans","")
   phrase = phrase.replace("moi","")
   phrase = phrase.replace(heure_rappel,"")   
   phrase = phrase.replace(minute_rappel,"")
   phrase = phrase.replace("heures","")
   phrase = phrase.replace("heure","")
   phrase = phrase.replace("minutes","")
   phrase = phrase.replace("minute","")
   phrase = phrase.replace(" demain ","")
   jour = int(jour) 
   jour = jour + 1
   jour = str(jour)

   mon_fichier = open(chemin_vers_fichier_de_note, "a")
   mon_fichier.write("\n" + heure_rappel+":"+minute_rappel+ " " +mois + ("/") + (jour) + ("/") + (time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close()
 
 if ("demain") in phrase and ("après") in phrase or ("après-demain") in phrase:
  print("1er marche fonctionne")
  if ("soir") not in phrase and ("matin") not in phrase and ("après-midi") not in phrase and ("minute") not in phrase and ("heure") not in phrase:
   print("voila lsource")
   phrase.replace(" demain ","")
   jour = int(jour)
   jour = jour + 2
   jour = str(jour)
   mon_fichier = open(chemin_vers_fichier_de_note, "a") 
   mon_fichier.write("\n" + heuree + (":") + minute + (" ") + mois + ("/") + (jour) + ("/")+(time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close()    
   
  elif ("soir") in phrase and ("matin") not in phrase and ("après-midi") not in phrase and ("minute") not in phrase and ("heure") not in phrase:
   phrase.replace(" demain ","" )
   jour = int(jour)
   jour = jour + 2
   jour = str(jour)
   mon_fichier = open(chemin_vers_fichier_de_note, "a") 
   mon_fichier.write("\n" + "19" + (":") + "00" + (" ") + mois + ("/") + (jour) +("/")+(time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close()
 
  elif ("soir") not in phrase and ("matin") in phrase and ("après-midi") not in phrase and ("minute") not in phrase and ("heure") not in phrase:
   phrase.replace(" demain ","")
   jour = int(jour)
   jour = jour + 2
   jour = str(jour)
   mon_fichier = open(chemin_vers_fichier_de_note, "a") 
   mon_fichier.write("\n" + "10" + (":") + "00" + (" ") + mois + ("/") + (jour) + ("/") + (time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close()
 
  elif ("soir") not in phrase and ("matin") not in phrase and ("après-midi") in phrase and ("minute") not in phrase and ("heure") not in phrase:
   phrase.replace(" demain ","")
   jour = int(jour)
   jour = jour + 2
   jour = str(jour)
   mon_fichier = open(chemin_vers_fichier_de_note, "a") 
   mon_fichier.write("\n" + "15" + (":") + "00" + (" ") + mois + ("/") + (jour) + ('/')+ (time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close() 
 
  elif ("heures") in phrase or ("minutes") in phrase:
   nombre_dans_phrase = re.findall('\d+', phrase)        
   print(nombre_dans_phrase)
   content_french = [phrase]
   for i in content_french:
    phrase = (word_tokenize(i, language='french'))  
   heure_rappel = heuree
   minute_rappel = minute
   
   try:  
    for chiffre in nombre_dans_phrase:   
     print("tour")
     calcule_heure = phrase.index("heures") - phrase.index(chiffre)
     if calcule_heure == 1: 
       heure_rappel = chiffre
       print(heure_rappel)
   except:
    print("") 
   
   minute_rappel = ("00")
   try: 
    for chiffre in nombre_dans_phrase:   
     moncalcule = phrase.index('minutes') - phrase.index(chiffre)
     print(moncalcule)
     if moncalcule == 1: 
       minute_rappel = chiffre    
       print(minute_rappel)
   except:
     print("")
   
   try: 
    for chiffre in nombre_dans_phrase:   
     moncalcule = phrase.index(chiffre) - phrase.index("heures")
     print(moncalcule)
     if moncalcule == 1: 
       minute_rappel = chiffre    
       print(minute_rappel)
   except:
     print("")
   
   if int(mois) < 10 and "0" not in mois:
    mois = "0" + mois
   
   phrase = " ".join(str(x) for x in phrase)
   phrase = phrase.replace("dans","")
   phrase = phrase.replace("moi","")
   phrase = phrase.replace(heure_rappel,"")   
   phrase = phrase.replace(minute_rappel,"")
   phrase = phrase.replace("heures","")
   phrase = phrase.replace("heure","")
   phrase = phrase.replace("minutes","")
   phrase = phrase.replace("minute","")
   phrase = phrase.replace(" demain ","")
   jour = int(jour) 
   jour = jour + 2
   jour = str(jour)
   
   mon_fichier = open(chemin_vers_fichier_de_note, "a")
   mon_fichier.write("\n" + heure_rappel+":"+minute_rappel+ " " +mois + ("/") + (jour) + ("/") + (time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close()
   
 elif ("demain") not in phrase and ("après-demain")not in phrase:
  if ("dans") in phrase: 
   nombre_dans_phrase = re.findall('\d+', phrase)        
   print(nombre_dans_phrase)
   content_french = [phrase]
   for i in content_french:
    phrase = (word_tokenize(i, language='french')) 
   
   heure_rappel = heuree
   minute_rappel = minute
   
   try:
    for chiffre in nombre_dans_phrase:   
     cacule_heure = phrase.index("heures") - phrase.index(chiffre)
     if cacule_heure == 1: 
       heure_rappel = int(heure_rappel) + int(chiffre)
       print("heure rapel egaole "+ heure_rappel)
       heure_rappel = str(heure_rappel)
       adition1 = chiffre
   except:
     print("")

   try:
    for chiffre in nombre_dans_phrase:
     moncalcule = (phrase.index('minutes') - phrase.index(chiffre))
     print(moncalcule)
     if moncalcule == 1: 
      minute_rappel = int(minute_rappel) + int(chiffre)
      adition = chiffre
      if minute_rappel < 10 and "0" not in str(minute_rappel):
        minute_rappel = "0" + str(minute_rappel)
      minute_rappel = str(minute_rappel)
      print(minute_rappel)
   except:
    
    try: 
     for chiffre in nombre_dans_phrase:
      moncalcule = (phrase.index(chiffre) - phrase.index('heures'))
      print(moncalcule)
      if moncalcule == 1:
       minute_rappel = int(minute_rappel) + int(chiffre)
       adition = chiffre
       if minute_rappel < 10 and "0" not in str(minute_rappel):
        minute_rappel = "0" + str(minute_rappel)
       minute_rappel = str(minute_rappel)
       print(minute_rappel)
    except:
      print("")
   
   if int(minute_rappel) > 60:
    heure_rappel = int(heure_rappel)+1
    minute_rappel = int(minute_rappel) - 60
    if minute_rappel < 10 and "0" not in str(minute_rappel):
        minute_rappel = "0" + str(minute_rappel)
    heure_rappel = str(heure_rappel)
    minute_rappel = str(minute_rappel)  
   
   if int(heure_rappel) > 24:
    heure_rappel = int(heure_rappel) - 24  
    mois = int(mois) + 1
    mois = str(mois) 
    if heure_rappel < 10: 
     heure_rappel = "0"+str(heure_rappel) 
   
   if int(mois) < 10 and "0" not in mois:
    mois = "0" + mois

   heure_rappel = str(heure_rappel)
   
   phrase = " ".join(str(x) for x in phrase)
   try:
    phrase = phrase.replace(adition,"")
   except:
    True

   try:
    phrase = phrase.replace(adition1,"")
   except:
    True
   phrase = phrase.replace("moi","")
   phrase = phrase.replace("dans","")
   phrase = phrase.replace(heure_rappel,"")
   phrase = phrase.replace(minute_rappel,"")
   phrase = phrase.replace("heures","")
   phrase = phrase.replace("heure","")
   phrase = phrase.replace("minutes","")
   phrase = phrase.replace("minute","")
   
   print(minute_rappel)
   print(heure_rappel)

  
   mon_fichier = open(chemin_vers_fichier_de_note, "a")
   mon_fichier.write("\n" + heure_rappel+":"+minute_rappel+ " " +mois + ("/") + (jour) + ("/") + (time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close()        
  
  elif ("heures") in phrase or ("minutes") in phrase:
   nombre_dans_phrase = re.findall('\d+', phrase)        
   print(nombre_dans_phrase)
   content_french = [phrase]
   for i in content_french:
    phrase = (word_tokenize(i, language='french'))  
   heure_rappel = heuree
   minute_rappel = minute
   
   try:  
    for chiffre in nombre_dans_phrase:   
     print("tour")
     calcule_heure = phrase.index("heures") - phrase.index(chiffre)
     if calcule_heure == 1: 
       heure_rappel = chiffre
       print(heure_rappel)
   except:
    print("") 
   
   minute_rappel = ("00")
   try: 
    for chiffre in nombre_dans_phrase:   
     moncalcule = phrase.index('minutes') - phrase.index(chiffre)
     print(moncalcule)
     if moncalcule == 1: 
       minute_rappel = chiffre    
       print(minute_rappel)
   except:
     print("")
   
   try: 
    for chiffre in nombre_dans_phrase:   
     moncalcule = phrase.index(chiffre) - phrase.index("heures")
     print(moncalcule)
     if moncalcule == 1: 
       minute_rappel = chiffre    
       print(minute_rappel)
   except:
     print("")
   
   if int(mois) < 10 and "0" not in mois:
    mois = "0" + mois
   
   phrase = " ".join(str(x) for x in phrase)
   phrase = phrase.replace("dans","")
   phrase = phrase.replace("moi","")
   phrase = phrase.replace(heure_rappel,"")   
   phrase = phrase.replace(minute_rappel,"")
   phrase = phrase.replace("heures","")
   phrase = phrase.replace("heure","")
   phrase = phrase.replace("minutes","")
   phrase = phrase.replace("minute","")
   phrase = phrase.replace(" demain ","")
   
   mon_fichier = open(chemin_vers_fichier_de_note, "a")
   mon_fichier.write("\n" + heure_rappel+":"+minute_rappel+ " " +mois + ("/") + (jour) + ("/") + (time.strftime('%y')) + (" ") + phrase)
   mon_fichier.close()

  elif ("ce") in phrase and ("soir") in phrase or ("ce") in phrase and ("matin") in phrase or("cette") in phrase and ("après-midi") in phrase:
   phrase = " ".join(str(x) for x in phrase)
   if ("matin") in phrase and ("soir") not in phrase and ("après-midi"):
    phrase.replace("matin","")
    mon_fichier = open(chemin_vers_fichier_de_note, "a") 
    mon_fichier.write("\n" + "10" + (":") + "00" + (" ") + (time.strftime('%m')) + ("/") + (time.strftime('%d')) + (time.strftime('%y')) + (" ") + phrase)
    mon_fichier.close()      
   if ("après-midi") in phrase and ("matin") not in phrase and ("soir") not in phrase:
    phrase.replace("après-midi","")
    mon_fichier = open(chemin_vers_fichier_de_note, "a") 
    mon_fichier.write("\n" + "15" + (":") + "00" + (" ") + (time.strftime('%m')) + ("/") + (time.strftime('%d')) + (time.strftime('%y')) + (" ") + phrase)
    mon_fichier.close() 
   if ("soir") in phrase and ("matin") not in phrase and ("après-midi") not in phrase:
    phrase.replace("soir","")
    mon_fichier = open(chemin_vers_fichier_de_note, "a") 
    mon_fichier.write("\n" + "18" + (":") + "00" + (" ") + (time.strftime('%m')) + ("/") + (time.strftime('%d')) + (time.strftime('%y')) + (" ") + phrase)
    mon_fichier.close()
  
