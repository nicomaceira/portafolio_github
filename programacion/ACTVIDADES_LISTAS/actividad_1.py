#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor
milista=[]
longitud=int(input("introduce el tamaño de la lista:"))
for x in range (0,longitud):
    caramelo=int(input("dame un caramelo:"))
    milista.append(caramelo)
milista.sort()
print(milista)
