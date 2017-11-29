import wikipedia


def definition(phrase): 
 try: 
  phrase.remove('c\'est')
 except:
  print("")
 try:
  phrase.remove("qui")
 except:
  print("")
 try:
  phrase.remove("est")
 except:
  print(" ") 
 try:
  phrase.remove("quoi")
 except:
  print("")
 try: 
  phrase.remove('un')
 except:
  print("")
 try: 
  phrase.remove('une')
 except:
  print("")
 try: 
  phrase.remove('le')
 except:
  print("")
 try: 
  phrase.remove('la')
 except:
  print("") 
 try:
 phrase = " ".join(str(x) for x in phrase)
 definition = wikipedia.summary(phrase, sentences = 1)
 return definition
 except:
 return "désolé monsieur, mais je ne connais pas de définition qui coresponde a votre demande"
