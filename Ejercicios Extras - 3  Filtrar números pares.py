#Ejercicio 3: Filtrar números pares

#Enunciado inicial:
#Escribe un programa que recorra una lista de números y genere una nueva lista con solo los
#números pares.
#Modificación 1:
#Cambia el programa para que filtre y muestre los números impares en lugar de los pares.
#Modificación 2:
#Ahora modifica el programa para que la nueva lista contenga solo los números que son múltiplos
#de 4.

numeros = [2, 3, 4, 5, 6, 7, 8, 20, 21, 23, 24]
lista_pares = [ numero for numero in numeros if numero % 2 == 0]
lista_pares_2 = []

for numero in numeros:
    if numero % 2 == 0:
        lista_pares_2.append(numero)


print(f"Lista de numeros: {numeros}")
print(f"Lista nueva con numeros pares: {lista_pares}")
print(f"Lista nueva con numeros pares: {lista_pares_2}")

