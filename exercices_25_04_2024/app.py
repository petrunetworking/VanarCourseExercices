#HomeWork add Cooordonates and add psobilities to add plants gather plants and count plants
from data import garden
from lib import render,menu,add_plant,count_plants,gather_plant

while True:
    render(garden)
    select_option =menu()
    if select_option == 1:
        row_input=int(input("introdu coordonatele rind: "))
        col_input=int(input("introdu coordonatele coloana: "))
        add_plant(garden,row_input,col_input)
    if select_option == 2:
        row_input=int(input("introdu coordonatele rind: "))
        col_input=int(input("introdu coordonatele coloana: "))
        gather_plant(garden,row_input,col_input)
    if select_option == 3:
        print("Water")#functia nu este implementata pina ce 
    if select_option == 4:
        count_plants(garden)
    if select_option == 0:
        break
    