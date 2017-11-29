import speech_recognition as sr

 
def reconnaissance(): 
 r = sr.Recognizer()
 r.energy_threshold = 525
 with sr.Microphone() as source:  
  print("je vous écoutes")
  audio = r.listen(source)
  print("réfléxion")
  try: 
   detection = (r.recognize_google( audio, language='fr-FR', show_all=False))
   return detection
  except:
   None  