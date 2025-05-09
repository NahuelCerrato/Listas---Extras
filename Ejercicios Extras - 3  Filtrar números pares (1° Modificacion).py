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
multiplos_de_4 = [ numero for numero in numeros if numero % 4 == 0]

print(multiplos_de_4)