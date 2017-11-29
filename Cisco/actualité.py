import urllib.request
import parole
import threading


def actualite():
 stop = 0
 global stop
 res = requests.get("https://news.google.com/news?cf=all&hl=fr&pz=2&ned=fr&topic=t&output=rss")
 doc = lxml.etree.fromstring(res.content)
 for item in doc.xpath('//item'):
   title = item.find('title').text
   threading.Thread(target=parole.dit(title)).start()
   if stop == 1:
   	break

def actualité_higtTech(): 
 stop = 0
 global stop
 res = requests.get("https://news.google.com/news?cf=all&hl=fr&pz=2&ned=fr&topic=t&output=rss")
 doc = lxml.etree.fromstring(res.content)
 for item in doc.xpath('//item'):
   title = item.find('title').text
   threading.Thread(target=parole.dit(title)).start()
   if stop == 1:
     break

def reconnaissance_actualité()
 r = sr.Recognizer()
 r.energy_threshold = 525
 with sr.Microphone() as source:  
  print("je vous écoutes")
  audio = r.listen(source)
  print("réfléxion")
  try: 
   detection = (r.recognize_google( audio, language='fr-FR', show_all=False))
   if "cisco" in detection and "stop" in detection:
    stop = 1  
  except:
   None  