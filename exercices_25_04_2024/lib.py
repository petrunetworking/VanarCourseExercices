#HomeWork add Cooordonates and add psobilities to add plants gather plants and count plants
import data
from os import system
def render(garden):
    # system('cls')# for windows  use cls and for linux use clear
    for ri in range(len(garden)):
        for ci in range(len(garden[0])):
            print(garden[ri][ci],end=" ")
        print(ri)#afisam coordonatele pe rind
    for ci in range(len(garden[0])):
            print(ci, end=" ") #afisam coordonatele pe coloana
    print()
        
print()
def add_plant(garden, input_row, input_col):
    if 0 <= input_row < len(garden) and 0 <= input_col < len(garden[0]):
            if garden[input_row][input_col] ==".":
                garden[input_row][input_col] = "P"
            else:
                print("este deja  planta")
    else:
            print("Coordonate nevalide. introdu coordonatele afisate pe ecran.")
    print()
def gather_plant(garden, input_row, input_col):
    if 0 <= input_row < len(garden) and 0 <= input_col < len(garden[0]):
        if garden[input_row][input_col] =="P":
            garden[input_row][input_col] = "."
        else:
            print("nu este planta")
    else:
        print("Coordonate nevalide. introdu coordonatele afisate pe ecran.")
    print()
def count_plants(garden):
    count =0
    for ri in range(len(garden)):
          for pi in range(len(garden[0])):
            if garden[ri][pi] =="P":
                count +=1
    plants =count * 100 / len(garden[ri]*len(garden))#len =18 6x3 list
    print(f"plants: {plants:3.0f}%")
def menu():
     print("MENU")
     print("1. Plant")
     print("2. Gather")
     print("3. Water")
     print("4. Count")
     print("0. Exit")
     option=int(input("> "))
     return option

    
