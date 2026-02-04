num1=int(input("introduce el primer valor, ambos valores deben ser numeros enteros: "))
num2=int(input("introduce el segundo valor:" ))
incremento=int(input("introduce el incremento: "))
for i in range(num1,num2,incremento):
    print(i,"*")