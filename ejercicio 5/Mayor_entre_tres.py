# Programa para verificar si los dos ultimos digitos de un numero son iguales

# Input
print("------------------------------------")
print("------------------------------------")
print("------------------------------------")
n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))
n3 = int(input("Ingresa el tercer numero: "))

# processing
if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3




# output
print("------------------------------------")
print("-------------resultado--------------")
print("------------------------------------")
print("El numero mayor es: ", mayor)