# Programa para verificar si los dos ultimos digitos de un numero son iguales

# Input
print("------------------------------------")
print("-----------ultimos digitos iguales--")
print("------------------------------------")
x = int(input("digite un numero: "))

# processing
ultimo_digito = x % 10
penultimo_digito = 0
if (ultimo_digito == penultimo_digito):
    rta = "IGUALES"
else:
    rta = "DIFERENTES"


# output
print("------------------------------------")
print("-------------resultado--------------")
print("------------------------------------")
print("El numero ingresado fue: " + str(x))
print("ultimo digito es: " + str(ultimo_digito))
print("su penltimo es: " + str(penultimo_digito))
