#!/usr/bin/env python3
############################################################################
# Soubor:  main.py
# Datum:   15.11.2021 
# Autor:   Večeřa Vojtěch 
############################################################################
from random import randint, choice

############################################################################


from random import randint, choice

samohlasky = 'aeiyou'
souhlasky = 'qwrtzpsdfghjklyxcvbnm'

def slovo (maxchars = 10):
    vysledek = ''
    zacatek = randint(0, 1)
    for i in range(randint(1,maxchars) ):
        if i % 2 == zacatek :
            vysledek += choice(samohlasky)
        else:
            vysledek += choice(souhlasky)    
    return vysledek

print(slovo())
