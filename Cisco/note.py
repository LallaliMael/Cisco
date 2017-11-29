import os
import parole

liste_note = []

chemin_vers_fichier_de_note = "chemin_vers_votre_fichier_texte_de_notes"

fichier_de_note = open(chemin_vers_fichier_de_note, "r") 
contenu = fichier_de_note.read()
fichier_de_note.close()

try:
 liste_note1 = contenu.split("zh;")
 for mot in liste_note1:
  liste_note.append(mot + " zh;")
except:
 None

for mot in liste_note:
  mot = mot.replace("zh;","")
  if mot = None or mot == " "
   chiffre_piston = liste_note.index(mot+"zh;")
   del liste_note[chiffre_piston]


def add_note(note):
  liste_note.append(note+" zh;")
  fichier_de_note = open(chemin_vers_fichier_de_note, "w") 
  note_pour_fichier = " ".join(str(x) for x in liste_note)
  fichier_de_note.write(note_pour_fichier)
  fichier_de_note.close()

def combien(): 
  nombre_de_note = len(liste_note)
  return nombre_de_note

def éfface(phrase):
 chiffre = re.findall('\d+', phrase)
 nombre_vérification = len(liste_note)
 conteur_de_nombre = 0
 nombre_de_note = len(liste_note)
 if nombre_de_note == 0:
   parole.dit("Il n\'ya aucun note enregistrer dans ma mémoire")
 else:
  for chifre in chiffre:
   chifre = int(chifre) - 1
   chifre = str(chifre)
   for note in liste_note:
    emplacement_note = liste_note.index(note)
    if int(chifre) - int(emplacement_note) == 0:
       del liste_note[int(chifre)]
       fichier_de_note = open(chemin_vers_fichier_de_note, "w")
       fichier_de_note.write( " ".join(str(x) for x in liste_note))
       fichier_de_note.close()
       parole.dit("La note est supprimé !")
    else:
       conteur_de_nombre = conteur_de_nombre + 1
       if conteur_de_nombre == nombre_vérification:
         parole.dit("La note que vous m'avez demandé d'éffacer n'éxiste pas, Monsieur")

def remove_all():
  liste_note = []
  fichier_de_note = open(chemin_vers_fichier_de_note, "w") 
  fichier_de_note.write("")
  fichier_de_note.close()
  parole.dit("J\'ai supprimé toutes les notes")

def affichier_une_note(phrase):
   if int(len(liste_note)) == 0:
     parole.dit("Il n\'y a aucune note enregistrer dans ma mémoire Monsieur") 
   else: 
    chiffre_dans_la_phrase = re.findall('\d+', phrase)
    nombre_de_note = len(liste_note)
    conteur_de_nombre = 0
    for chiffre in chiffre_dans_la_phrase:
     recup = chifre
     chiffre = int(chiffre) - 1
     chiffre = str(chiffre)
     for note in liste_note: 
      emplacement_note = liste_note.index(note)
      if int(chifre) - int(emplacement_note) == 0: 
       parole.dit("La note numéro " + recup + " est : " + note.replace("zh;",""))
      else:
         conteur_de_nombre = conteur_de_nombre + 1
      if conteur_de_nombre == nombre_de_note:
         parole.dit("La note que vous soubaité afficher n'éxiste pas") 


def afficher_toutes_les_notes():
  reponse = ""
  for note in liste_note:
   empl = liste_note.index(note)
   empl = int(empl) + 1
   empl = str(empl)
   reponse = reponse + " " + ",note " + str(empl) + (" : ") + note.replace("zh;","")
   parole.dit(reponse)

 