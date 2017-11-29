import alerte_mail
import traitement_de_la_demande
import rappel
import réveil
import hello

import threading


threading.Thread(target=hello.bonjour()).start()
threading.Thread(target=alerte_mail.alerte()).start()
threading.Thread(target=rappel.rappel()).start()
threading.Thread(target=réveil.reveil()).start()
threading.Thread(target=traitement_de_la_demande.traitement()).start()


