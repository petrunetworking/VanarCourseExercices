PARKING_PLACES = 7
FREE_PLACE = 3

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES + 1):
    if place_index == FREE_PLACE:
        print("|  |", end="")
    else:
        print("| X |", end="")

print("\n","#"*PARKING_PLACES*5, sep="")
#intrebare ce reprezinta parametrul sep in functia print() si de ce a fost nevoie de acesta?
#raspuns
"""
Separatorul dintre argumentele funcției print() din Python este în mod implicit un spațiu (caracteristica softspace), care poate fi modificat și poate fi transformat în orice caracter, număr întreg sau șir de caractere,
la alegerea noastră. Parametrul "sep" este utilizat pentru a realiza același lucru, acesta se găsește doar în python 3.x sau mai târziu. 
Acesta este, de asemenea, utilizat pentru formatarea șirurilor de ieșire.
sursa info https://www.geeksforgeeks.org/python-sep-parameter-print/

"""
