# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:41:50 2024

@author: erikas
"""

#Arbeidskrav 2 

#Oppg 1) Du skal her lage et programmet som skal regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive svaret til skjerm med passende tekst.

def beregn_alder(fodselsaar):
    return 2024 - fodselsaar

# Brukerinput
fodselsaar = int(input("Skriv inn fødselsår: "))  #Legge inn fødselsnummer
alder = beregn_alder(fodselsaar)    # Alder som brukes i def
print(f"Du blir {alder} år i løpet av 2024.")


#%%

#Oppg 2) Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. 
#Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe 5).
#Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
#Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?

import math  # For å bruke math.ceil, dette er for å rund opp til nærmeste heltall
def antall_pizza_total(antall_elever):
    antall_pizza_elev = 0.25 # Hver elev spiser 1/4 pizza
    antall_pizza_total = antall_elever * antall_pizza_elev 
    return math.ceil(antall_pizza_total)  # Rund opp til nærmeste heltall

# Brukerinput
antall_elever = int(input("Skriv antall elever: "))  # Antall elever som skal være med på festen og spise
antall_pizza = antall_pizza_total(antall_elever) # Regn ut total pizza
print(f"Det må handles inn {antall_pizza} pizzaer til festen.")

#%%

#Oppg 3) Lag et program med en funksjon som regner om fra grader til radianer.

import numpy as np
# Funksjon for å konvertere grader til radianer
def v_rad(v_grad):
    return v_grad * np.pi / 180

# Brukerinput
v_grad = float(input('Skriv inn gradtallet: '))  #Brukeren skriver inn vinkelen i grader
antall_radianer = v_rad(v_grad)  # Beregner radianer
print(f"{v_grad:.0f} grader er {antall_radianer:.2f} radianer.")  #Skriver ut med 2 desimaler

#%%

#Oppg 4)

#4.a Oppretter en dictionary med land, hovedstad og antall innbyggere i millioner

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }

#Brukerinput
land = input("Skriv et land: ")

#Sjekker om landet finnes i dictionary
if land in data:
   hovedstad, innbyggere = data[land]
   print(f"{hovedstad} er hovedstaden i {land}, og det bor {innbyggere} millioner innbyggere der.")
else:
   print(f"Beklager, informasjon om {land} finnes ikke i databasen.")
  
#%%    
#4.b # Oppretter en dictionary med eksisterende data og ledde et nytt land

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }

# Brukerinput for å legge til nytt land
nytt_land = input("Skriv inn et nytt land: ")

# Sjekker om landet allerede finnes i ordboken
if nytt_land in data:
    print(f"{nytt_land} finnes allerede i databasen.")
else:
    hovedstad = input(f"Skriv inn hovedstaden i {nytt_land}: ")
    innbyggere = float(input("Skriv inn antall innbyggere i hovedstaden (i millioner): "))
 
#Legger til det nye landet i dictionary
data[nytt_land] = [hovedstad, innbyggere]
print(f"{nytt_land} har blitt lagt til databasen!")

#Skriver ut den oppdaterte dictionaryen
print("\nOppdatert dictionary:")
for land, info in data.items():
 print(f"{land}: Hovedstad - {info[0]}, Innbyggere - {info[1]} millioner")
  
 
#%%

#Oppgave 5) Lag et program med en funksjon som tar a og b som argumenter og returner ut arelaet og ytre omkrets

import math 
def beregn_total_areal_omkrets(a, b):
    
   #beregn areal av trekanten
   areal_trekant = (a * b) / 2 #areal av trekanten er høyde * base delt i to
   
   #beregn hypotenusen (diameteren til halvsirkelen) og hypotenuse til trekanten
   hypotenuse = math.sqrt(a**2 + b**2)
   
   #beregn radius til halvsirkelen (halvparten av hypotenusen)
   radius= hypotenuse/2   
        
   #beregne areal av halvsirkel
   areal_sirkel = (math.pi* radius**2) / 2  # Areal av halvsirkel 
    
   #beregn total areal
   total_areal = areal_trekant + areal_sirkel
        
   #beregn omkretsen av halvsirkel
   omkrets_sirkel = math.pi * radius + hypotenuse
    
   #beregne omkretsen av trekanten
   omkrets_trekant = a + b + hypotenuse
    
   #beregne total omkrets
   total_omkrets = omkrets_sirkel + omkrets_trekant #Ytre omkrets (halvsirkel + trekant)
   return  total_areal , total_omkrets
   
#brukerinput
a = float(input("Legge inn verdi for a (lengde på en katet): "))
b = float(input("Legge inn verdi for b ( lengde på den andre kateten): "))  

#Kall funksjonen og hent resultatene
areal, omkrets = beregn_total_areal_omkrets(a, b)
    
print(f"Total arealet av trekanten er: {areal:.2f} kvadrat enheter")
print(f"Total omkretsen til figuren er: {omkrets:.2f} enheter")


#%%
#Oppgave 6 Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10]

import numpy as np
import matplotlib.pyplot as plt

# Definer funksjonen f(x) = -x^2 - 5
def f(x):
    return -x**2 - 5

# Definer x-verdier på intervallet [-10, 10]
x = np.linspace(-10, 10, 200)

# Beregn y-verdier ved å bruke funksjonen
y = f(x)

# Plot grafen
plt.plot(x, y, label=r'$f(x) = -x^2 - 5$', color='blue')

# Legg til tittel og etiketter
plt.title("Plot av funksjonen $f(x) = -x^2 - 5$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.grid(True)
plt.legend()

# Vis grafen
plt.show()

    
    
    
