import random

lista = [random.randint(1, 20) for _ in range(5)]
lista_nueva = []

for numero in lista:
    if numero > 10:
        lista_nueva.append(numero)

lista_nueva_mayores = [x for x in lista if x > 10]

print(lista)
print(lista_nueva)
print(lista_nueva_mayores)