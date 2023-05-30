numeros = []
suma = 0

while True:
    try:
        valor = int(input("Ingresa un número entero (o un valor no numérico para salir): "))
        numeros.append(valor)
        suma += valor
    except ValueError:
        break

promedio = suma / len(numeros)

print("La sumatoria de los números digitados es:", suma)
print("El promedio de los números digitados es:", promedio)
