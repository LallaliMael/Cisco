import parole
import webbrowser
import détéction_apareil
import note
import actualité
from random import choice
import threading
import définition
import musique

vérification = 1
hote = ''
port = 12800

#Pour lancer la reconnaissance du mot clé "cisco"
def snowboy():
  os.system("sudo xterm -e 'python " + chemin_vers_le_fichier_demo_snowboy + chemin_vers_le_fichier_snowboy_cisco +   "'")


def traitement():
 while vérification == 1:
 #conexion avec le fichier snowboy
  connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  connexion_principale.bind((hote, port))
  connexion_principale.listen(5)
  print("Le serveur écoute à présent sur le port {}".format(port))
  serveur_lance = True
  clients_connectes = []
  
  while serveur_lance:
   connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
   for connexion in connexions_demandees:
      connexion_avec_client, infos_connexion = connexion.accept()
      clients_connectes.append(connexion_avec_client)
   clients_a_lire = []
   try:
      clients_a_lire, wlist, xlist = select.select(clients_connectes,
              [], [], 0.05)
   except select.error:
       pass
   else:
    for client in clients_a_lire:
     msg_recu = client.recv(1024)
     requete = msg_recu.decode()
     print(requete)
     os.system("killall python")
#Si le mot clé "Cisco" est détécté
     if requete == 1:
     	phrase = reconnaissance_vocale.reconnaissance()
     	content_french = [phrase]
        for i in content_french:
         phd = (word_tokenize(i, language='french'))
         print(phd)
        if "close" in phrase:
        	exit()
        elif "heure" in phrase and "note" not in phrase or "heure" in phrase and "rappel" not in phrase or "heure" in phrase and "réveil" not in phrase:
            heure = (time.strftime("Il est %H heures %M monsieur."))
            parole.dit(heure)
            snowboy()
        elif "lance" in phrase and "internet" in phrase and "recherche" not in phrase or "ouvre" in phrase and "google" in phrase and "recherche" not in phrase:
            webbrowser.open("https://www.google.fr")
            parole.dit("C\'est fait !")
            snowboy()
        elif "raconte" in phrase and "histoire" in phrase and "rappel" not in phrase and "note" not in phrase:
            reponse = choice(['C\'est l\'histoire d\'un assistant virtuel trés intélligent','Et il vécurent heureux et eurent baucoup d\'enfants'])
            parole.dit(reponse)
            snowboy() 
        elif "je" in phrase and "t'aime" in phrase and "note" not in phrase and "rappel" not in phrase:
        	parole.dit("Merci !")
        	snowboy()
        elif "lance" in phrase and "youtubez" in phrase and "recherche" not in phrase or "ouvre" in phrase and "youtube" in phrase and "recherche" not in phrase:
            webbrowser.open("www.youtube.com")
            parole.dit("Tout de suite Monsieur")
            snowboy()
        elif "combien" in phrase and "apareil" in phrase and "conécté" in phrase and "note" not in phrase and "rappel":
        	parole.dit("je regarde sa")
        	nombre = détéction_apareil.combien_dapareil()
        	if liste_apareil = []:
        		parole.dit("Il n'ya aucun appareil conécté a votre réseau")
            else:
            	parole.dit("Il ya" + nomnbre + "conécté a votre réseau Monsieau" )
            snowboy()
        elif "prend" in phrase and "note" in phrase or "ajoute" in phrase and "note" in phrase:
        	phrase = phrase.replace("prend","")         
            phrase = phrase.replace("note","")
            phrase = phrase.replace("ajoute","")
            note = phrase
            note.add_note(note)
            snowboy()
        elif "combien" in phrase and "note" in phrase or "combien" in a and "note" in phrase:
        	nombre_de_note = note.combien()
        	snowboy()
        elif "éfface" in a and "tout" not in a or "supprime" in a and "tout" not in a:
            note.éfface(phrase)
            snowboy()
        elif "éfface" in phrase and "tout" in phrase and "note" in phrase:
        	note.remove_all()
            snowboy()
        elif "li" in phrase and "note" in phrase and "tout" not in phrase:
        	note.affichier_une_note(phrase)
        	snowboy()
        elif "li" in phrase and "note" in phrase and "tout" in phrase:
        	note.afficher_toutes_les_notes()
        	snowboy()
        elif "vérifie" in phrase and "mail" in phrase and "note" not in phrase and "rappel" not in phrase or "combien" in phrase and "non" in phrase and "mail" in phrase and "note" not in phrase and "rappel" not in phrase:
            notif = alerte_mail.notif()
            parole.dit("Vous avez " + notif + " mail non lue")
            snowboy()
        elif "présente" in phrase and "toi" in phrase and "note" not in phrase and rappel not in phrase:
        	reponse = ("bonjour, je m'apelle CISCO et je suis votre nouvelle assistant virtuel, je suis capable d'éxécuté des tache plus ou moins simple sur votre PC")
            parole.dit(reponse)
            snowboy()
        elif "tu" in phrase and "sert" in phrase and "quoi" in phrase and "note" not in phrase and rappel not in phrase:
            reponse = "Je suis capable d'éxécuter des tache plus ou moins simple sur votre pc, vos apareil domotique, je peut aussi répondre a beaucoup de vos question, vous rappéler ce que vous souhaiter vous réveiller tout les matin et de nombreuse autre chose"
            parole.dit(reponse)
            snowboy()
        elif "actualité" in phrase and "higt" nit in phrase and "numérique" not in phrase and "note" not in phrase and "rappel" not in phrase:
            threading.Thread(target=actualité.reconnaissance_actualité).start()
            actualité.actualite()
            snowboy()
        elif "musique" in phrase and "note" not in phrase and "rappel" not in phrase:
        	threading.Thread(target=musique.reconnaissance.musique).start()
            musique.lecture_musique()
            snowboy()
        elif "redémarre" in phrase and "note" not in phrase and "rappel" not in ta:
        	os.system("shutdown -r -t 00")
            parole.dit("Tout se suite !")
            snowboy()
              elif ("redéma") in phrase and ("recherche") not in phrase and ("dit") not in phrase and ("def") not in phrase and ("déf") not in phrase and ("exposé") not in phrase or ("redémarre") in phrase and ("recherche") not in phrase and ("dit") not in phrase and ("def") not in phrase and ("déf") not in phrase and ("exposé") not in a:
         os.system("shutdown -r -t 00")
         reponse = ("bien sur")
         parole.dit(reponse)
         snowboy()

      elif "j'ai" in phrase and "chaud" in ta:
        reponse = "Aller faire un petit plongeon !"
        parole.dit(reponse)              
        snowboy()

      elif "j'ai" in phrase and "froid" in ta:
        reponse = "Vous voulez un chocolat chaud ?"
        parole.dit(reponse)
        snowboy()

      elif "je" in phrase and "suis" in phrase and "énervé" in phrase or "je" in phrase and "suis" in phrase and "furieux" in phrase or "je" in phrase and "suis" in phrase and "en" in phrase and "colère" in ta:
         reponse = "La colère est une émotion idiote, en plus vous saviez qu'elle vous grille les neurone ? Bien que mes neurones soit artificielle phrase votre place je me calmerez"        
         parole.dit(reponse)      
         snowboy()

      elif "je" in phrase and "suis" in phrase and "content" in phrase or "je" in phrase and "suis" in phrase and "heureux" in ta:
        reponse = "Si vous étes heureux, je le suis aussi !"
        parole.dit(reponse) 
        snowboy()

      elif "tu" in phrase and "habite" in phrase and "ou" in ta:
        reponse = "j'habite sur un nuage"
        parole.dit(reponse)      
        snowboy()

      elif "je" in phrase and "suis" in phrase and "triste" in ta:
        reponse = "La tristesse n'est qu'un sentiment, rien de plus"
        parole.dit(reponse)      
        snowboy() 
      elif "j'ai" in phrase and "peur" in ta:
        reponse = "La peur n'est qu'un sentiment, rien de plus"
        parole.dit(reponse)      
        snowboy()
      elif "j'ai" in phrase and "faim" in ta:
        reponse = "Faite vous un sandwich !"
        parole.dit(reponse)      
        snowboy()
      elif "tu" in phrase and "as" in phrase and "quelle" in phrase and "age" in phrase or "t'as" in phrase and "quelle" in phrase and "age" in phrase or "ta" in phrase and "quelle" in phrase and "age" in ta:
        reponse = "je ne suis qu'un programme, le tempS ne m'atteint pas, je suis immortelle"
        parole.dit(reponse)        
        snowboy()
      elif "j'ai" in phrase and "soif" in ta:
        reponse = "Buvez un verre d'eau !"
        parole.dit(reponse)       
        snowboy()
      elif "j'ai" in phrase and "péter" in ta:
        reponse = "Alors je suis content de ne pas avoir de nez pour sentir sa"
        parole.dit(reponse)
        snowboy()
      elif "ferme" in phrase and "séssion" in phrase:
      	os.system("shutdown -l")
        parole.dit("Trés bien !")
        snowboy()
      elif "raconte" in phrase and "blague" in phrase and "note" note in phrase and "rappel" not in phrase:
      	 reponse = choice(['attention, c\'est une blague a deux balles ... Pan Pan','Dans quelle pays on ne bronze pas du nez ? Mais au népal bien sur','a votre avis quelle est la capital de tamalou ? Et bien c\'est J\'ai bobola ! '])
         parole.dit(reponse)
         snowboy()
      elif "éteint" in phrase and "note" not in phrase and "rappel" not in phrase:
      	 os.system("shutdown -p -t 0")
         snowboy()
      elif "météo" in phrase and "note" not in phrase and "rappel" not in phrase:
      	 phrase = phrase.replace("météo","")
         phrase = phrase.replace("donne-moi","")
         phrase = phrase.replace("donne-moi ","")
         phrase = phrase.replace("donne","")
         phrase = phrase.replace("moi","")
         phrase = phrase.replace("la","")
         phrase = phrase.replace("c\'est","")
         phrase = phrase.replace("quoi","")
         phrase = phrase.replace("à","")
         phrase = phrase.replace("de","")
         phrase = phrase.replace("du","")
         phrase = phrase.replace("en","")
         phrase = phrase.replace("au","")
         phrase = phrase.replace("aux","")
         phrase = phrase.replace("température","")
         phrase = phrase.replace(" demain ","")
         phrase = phrase.replace(" après ","")
         phrase = phrase.replace(" après-demain ","")
         meteo.meteo(phrase)
         snowboy()
      elif "rappel" in phrase:
      	 rappel.add_rappel(phrase)
      	 parole.dit("C'est fait, Monsieur")
      	 snowboy()
      elif "merci" in phrase and "note" not in phrase and "rappel" not in phrase:
      	 reponse = choice(['Mais de rien Monsieur !','Mais je suis là pour ça !','Vous m\'avez créé pour ça !'])
      	 parole.dit(reponse)
      elif "jour" in phrase and "rappel" not in phrase and "note" not in phrase:
      	 reponse = time.strftime('Nous somme le %A %d/%m/%Y monsieur')
         parole.dit(reponse)
         snowboy()
      elif "recherche" in phrase and "note" not in phrase and "rappel" not in phrase:
      	 phrase = phrase.replace("recherche","")
      	 url = "https://www.google.fr/?gws_rd=ssl#q="
         recherche = phrase
         webbrowser.open(url + recherche)
         parole.dit("La recherche est lancé Monsieur !")
         snowboy()
      elif "dis" in phrase and "note" not in phrase and "rappel" not in phrase or "répète" in phrase and "note" not in phrase and "rappel" note in phrase:
         phrase = phrase.replace("dis","")
         phrase = phrase.replace("répète","")
         parole.dit(phrase)
         snowboy()
      elif "c'est" in phrase and "quoi" in phrase and "note" not in phrase and "rappel" not in phrase or "c'est" in phrase and "qui" in phrase and "note" not in phrase and "rappel" not in phrase:
         parole.dit(définition.definition(phrase))
      else:
       for mot in ta:
         if mot in liste_insulte:
          parole.dit("J'ai toujours su que vous étiez trés mal élevé")
          snowboy()      
         else:
          parole.dit("Désolé Monsieur mais je n'ai pas compris")
          snowboy()