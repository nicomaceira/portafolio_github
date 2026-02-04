#71.  Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.
lista_letras = []
while True:
    letra = input("Introduce una letra (o escribe 'fin' para terminar): ")
    if letra.lower() == "fin":
        break
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, introduce solo una letra.")
    if letra not in lista_letras:
        lista_letras.append(letra)
        print("Letra añadida.")
    else:
        print("Esa letra ya está en la lista, no se añadirá.")
print("Lista final de letras sin repetir:", lista_letras)
