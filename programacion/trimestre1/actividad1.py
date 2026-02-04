#nombramos las variables
var_min=int(input("introduce el principio: "))
var_max=int(input("introduce el final: "))
intervalo=int(input("introduce el intervalo: "))
#realizamos la sequencia
for i in range (var_min,var_max,intervalo):
    #mostramos por pantalla la sequencia
    print(i,end=",")