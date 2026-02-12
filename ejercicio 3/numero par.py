# programa para verificar si un numero es par

# Input
print("------------------------------------")
print("---------Numero par/impar-----------")
print("------------------------------------")
x = int(input("digite un numero: "))

# processing
mod = x%2
if (mod == 0):
    rta = "PAR"
else:
    rta = "IMPAR"


# output
print("------------------------------------")
print("-------------resultado--------------")
print("------------------------------------")
print("El numero " + str(x) + " es " + rta)