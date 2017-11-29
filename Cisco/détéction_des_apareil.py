import os

def combien_dapareil():
  subcmd=os.popen('nmap -sP 192.168.1.*','r')  
  a = (subcmd.read()) 
  nombre = a.count('scan report for') 
  return nombre

def nom_apareil():
  subcmd=os.popen('nmap -sP 192.168.1.*','r')  
  a = (subcmd.read()) 
  a = a.split(" ")
  liste_apareil = []
  for mot in a:
   if ".home" in mot:
    liste_apareil.append(" , " + mot.replace(".home",""))      
  return liste_apareilz 
  