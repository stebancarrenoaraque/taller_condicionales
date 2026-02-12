# programa para calcular costo de una llamada
# Input
print("------------------------------------")
print("---------costo llamada--------------")
print("------------------------------------")
min= int(input(" Digite la duracion de la llamada en minutos: "))

# processing
if (min <= 3):
    costo_llamada = 500
else:
    costo_llamada = 500 + (min - 3)*100

# output
print("------------------------------------")
print("-------------resultado--------------")
print("------------------------------------")
print("Duracion de la llamada: " + str(min) + "minutos")
print("costo de la llamada: " + str(costo_llamada))