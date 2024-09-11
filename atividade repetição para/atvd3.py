temperaturas = []
print("digite 7 temperaturas0")

for i in range(7):
    temperatura = float(input(f"temperatura {i + 1}: "))
    temperaturas.append(temperaturas)
soma = 0
for temp in temperaturas:
    soma += temp

media = soma / 7

igual_ou_acima = 0
abaixo = 0

for temp in temperaturas:
    if temp >= media:
        igual_ou_acima += 1
    else:
        abaixo += 1

print(f"temperaturas iguais ou acima da média: {igual_ou_acima}")
print(f"temperaturas abaixo da média: {abaixo}")