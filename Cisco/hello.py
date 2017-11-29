import time
import parole
from random import choice

liste_help = ['Vous avez besoin de mon aide ? ','Comment puis-je vous aider ? ','Je peux vous aider ? ','Que puis-je faire pour vous ? ','Comment puis-je vous être utile ? ']
liste_bonjour = ['bonjour Monsieur !','Heureux de vous revoir monsieur ','bonjour !','bonne journée']
bonjourm = ['bon matin, Monsieur !','Heureux de vous revoir Monsieur','bonne matinée']
bonjours = ['bonsoir Monsieur !','Heureux de vous revoir Monsieur','bonsoir !' ]

heure = (time.strftime("%H"))


def bonjour():
 vérifie_jour = time.strftime('%d/%m')
 if vérifie_jour == ('12/24') or vérifie_jour == ('12/25'):
  hello = ("Joyeux noël, Monsieur")
 else: 
  if (heure) <= ("11"):
   hello = choice(bonjourm)
  elif (heure) <= ("17") and (heure) > ("11"):
   hello = choice(liste_bonjour)
  elif (heure) <= ("24") and (heure) > ("17"):
   hello = choice(bonjours)
  help = choice(liste_help)
  parole.dit(hello + " " + help)