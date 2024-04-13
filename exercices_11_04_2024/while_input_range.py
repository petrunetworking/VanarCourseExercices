#condition sa se  citeasca de la tastatura doua variabile start_n si end_n
start_n =int(input("introduceti numarul de inceput:"))
end_n=int(input("introduceti numarul de sfirsit:"))
#condition sa se modifice codul de mai sus in asa mod incat daca utilizatorul introduce prima valoare mai mica si cea de a doua mai mare (de ex: 5 si 10) ciclul sa afiseze toate valorile in ordine crescatoare de la 5 la 10
if start_n < end_n:
    while start_n <= end_n:
        print(start_n)
        start_n += 1
#condition daca valorile se introduc invers (de ex: 10 si 5) sa se afiseze toate numerele intregi in ordine descrescatoare din acest diapazon
elif start_n > end_n:
    while start_n>=end_n:
        print(start_n)
        start_n -=1