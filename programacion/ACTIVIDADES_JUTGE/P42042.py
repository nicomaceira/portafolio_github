
letra= input()
if letra.isupper():
    letra = "majuscula"
elif letra.islower():
    letra = "minuscula"
vocals = "aeiouAEIOU"
if letra in vocals:
    tipo = "consonant"
elif letra.isalpha():
    tipo = "vocal"
print(letra)
print(tipo)
