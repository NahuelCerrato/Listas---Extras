
lista = [ 2 , 4 , 5 , -3 , 6, -3, -4, -6, 10, 2]
suma_positivos = 0
suma_negativos = 0
suma_total = 0
mayores_que_tres = 0
menores_que_tres = 0

for i in lista:
    suma_total += i
    if i > 0:
        suma_positivos += i
    if i > 3:
        mayores_que_tres += i
    if i < 3:
        menores_que_tres += i
    if i < 0:
        suma_negativos += i

print(f"La suma de los numeros positivos de la lista es: {suma_positivos}")
print(f"La suma de los numeros negativos de la lista es: {suma_negativos}")
print(f"La suma de todos los numeros de la lista es: {suma_total}")
print(f"La suma de los numeros mayores que 3 de la lista es: {mayores_que_tres}")
print(f"La suma de los numeros menores que 3 de la lista es: {menores_que_tres}")
