#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no
lista1=[]
lista2=[]
pal_repetidas=[]
pal_norepetidas=[]
longitud1=int(input("introduce la cantidad de palabras de la lista1: "))
for x in range (0,longitud1):
    palabra1=input("introduce una palabra: ")
    if palabra1 not in lista1:
        lista1.append(palabra1)
    else:
        print("ya has introducido esta palabra")
longitud2=int(input("introduce la cantidad de palabras de la lista2: "))
for y in range (0, longitud2):
    palabra2=input("introduce una palabra: ")
    if palabra2 not in lista2:
        lista2.append(palabra2)
    else:
        print("ya has introducido esta palabra")
for palabra in lista1:
    if palabra in lista2:
         pal_repetidas.append(palabra)
    else: pal_norepetidas.append(palabra)
print("palbras repetidas: ", pal_repetidas)
print("palanras no repetidas: ",pal_norepetidas)