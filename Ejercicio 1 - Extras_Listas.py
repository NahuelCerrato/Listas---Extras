lista = [5, 12, 8, 20, 3]
cuadrados = []
cuadrado_list = [x**2 for x in lista]
for numero in lista:
    cuadrados.append(numero**2)


print(cuadrado_list)
print(cuadrados)
