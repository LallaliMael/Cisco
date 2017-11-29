from imaplib import ssl
import imaplib
import parole
import os

adresse_email = "Votre adresse email"
mot_de_passe_de_ladresse = "votre mot de passe"
notif = 0
u = 0
global notif

def alerte():
   def rafraichir():
     mail = imaplib.IMAP4_SSL('imap.outlook.com')
     mail.login(adresse_email, mot_de_passe_de_ladresse)
     mail.list()
     mail.select("inbox")
     result, data = mail.search(None, "ALL")
     ids = data[0]
     id_list = ids.split()
     latest_email_id = id_list[-1]
     result, data = mail.fetch(latest_email_id, "(RFC822)")
     raw_email = data[0][1]
     return raw_email
   dernierMail=rafraichir()
   while u == 0:
     mailApresRafraichissement=rafraichir()
     if dernierMail != mailApresRafraichissement :
         global notif
         notif += 1
         parole.dit("Vous avez reçu un nouveau mail, Monsieur")
         dernierMail=mailApresRafraichissement

def verif():
    return notif

