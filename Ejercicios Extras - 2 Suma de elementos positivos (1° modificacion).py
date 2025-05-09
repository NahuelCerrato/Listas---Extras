#Ejercicio 2: Contar palabras largas

#Enunciado inicial:
#Crea un programa que recorra una lista de palabras y cuente cuántas palabras tienen más de 5
#letras.
#Modificación 1:
#Modifica el programa para contar las palabras que tienen exactamente 5 letras.

palabras = ["Jarra", "Palabra", "Baño", "Educación", "Estructura", "Segui", "Mosca", "Maple"]
contador = 0
palabra_5 = 0

for palabra in palabras:
    if len(palabra) == 5:
        palabra_5 += 1
    if len(palabra) > 5:
        contador +=1
        
print(f"Las palabras con más de 5 letras son: {contador}")
print(f"Las palabras con 5 letras son: {palabra_5}")