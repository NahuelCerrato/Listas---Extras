
lista = [ 2 , 4 , 5 , -3 , 6, -3]
suma_positivos = 0
suma_negativos = 0
suma_total = 0

for i in lista:
    suma_total += i
    if i > 0:
        suma_positivos += i
    else:
        suma_negativos += i

print(f"La suma de los numeros positivos de la lista es: {suma_positivos}")
print(f"La suma de los numeros negativos de la lista es: {suma_negativos}")
print(f"La suma de todos los numeros de la lista es: {suma_total}")
