#nombramos las variables
num_positivos=0
num_negativos=0
veces=6
#realizamos el bucle
for num in range(veces):
    num=int(input("introduce un numero: "))
#añadimos las condiciones
if num<0:
    num_negativos+1
if num>0:
    num_positivos+1
#mostramos por pantalla las soluciones
print(f"la suma de numeros positivos es:{num_positivos}")
print(f"la suma de numeros negativos es de:{num_negativos}")