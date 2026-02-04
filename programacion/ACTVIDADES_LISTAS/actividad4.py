#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
lista = []
vocales = "aáàeéèiíìoóòuúù"
while True:
    letra = input("Introduce una letra (o 'fin' para terminar): ")
    if letra.lower() == "fin":
        break
    if len(letra) != 1 or not letra.isalpha():
        print("Introduce solo una letra.")
        continue
    if letra.lower() in vocales:
        if letra.lower() in "aáàäâ":
            letra = "a"
        elif letra.lower() in "eéèëê":
            letra = "e"
        elif letra.lower() in "iíìïî":
            letra = "i"
        elif letra.lower() in "oóòöô":
            letra = "o"
        elif letra.lower() in "uúùüû":
            letra = "u"
    if letra not in lista:
        lista.append(letra)
        print("Letra añadida.")
    else:
        print("Letra repetida.")
print("Lista final:", lista)