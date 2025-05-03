nombres = ["Nahuel", "Hugo", "Ignacio", "Martina", "Ivan"]
acumulador_5 = 0
contador = 0

for nombre in nombres:
    if len(nombre) > 5:
        acumulador_5 +=1
        
print(f" Los nombres de la lista son: {nombres}")
print(f" La cantidad de nombres con más de 5 letras son: {acumulador_5}")
