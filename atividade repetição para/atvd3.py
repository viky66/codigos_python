temperaturas = []
print("Informe 7 temperaturas: ")

soma = 0

for i in range(7):
    temperatura = float(input(f"Temperatura {i + 1}: "))
    temperaturas.append(temperatura)

for temp in temperaturas:
    soma += temp

media = soma / 7

igual_acima = 0
abaixo = 0

for temp in temperaturas:
    if temp >= media:
        igual_acima += 1
    else:
        abaixo += 1

print(f"Temperaturas iguais ou acima da média: {igual_acima}")
print(f"Temperaturas abaixo da média: {abaixo}")