#Ejercicio 2: Contar palabras largas

#Enunciado inicial:
#Crea un programa que recorra una lista de palabras y cuente cuántas palabras tienen más de 5
#letras.

palabras = ["Jarra", "Palabra", "Baño", "Educación", "Estructura"]
contador = 0

for palabra in palabras:
    if len(palabra) > 5:
        contador +=1 
        
print(contador)