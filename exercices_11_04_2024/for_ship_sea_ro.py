#condition Sa se schimbe codul astfel incat coordonata vaporului sa poata fi data de la tastatura
big_ship  = int(input("please enter coordonat:"))
for x in range(1,11):
    if x == big_ship:
        #Sa se schimbe codul if/else astfel incat daca big_ship = 5 - rezultatul sa arate asa ~~~wWw~~~~
        if big_ship ==5:
            print("wWw",end="")
        else:
            print( "W", end="")
    else:
      print( "~", end="")