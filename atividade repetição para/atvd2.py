numeros = []
for i in range(8):
    numero= float(input(f"Número {i + 1}: "))
    numeros.append(numero)

negativo = 0
soma_positivo = 0

for numero in numeros:
    if numero < 0:
        negativo +=1
    elif numero > 0:
        soma_positivo += numero
print(f"Números negativos: {negativo}")
print(f"Soma dos números positivos: {soma_positivo}")


