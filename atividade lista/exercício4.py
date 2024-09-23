meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

temperaturas = []
contador = 0
soma = 0 
print("Informe a temperatura média do mês: ")

for contador in range(12):
    temperatura = float(input(f"Temperatura {contador + 1}: "))
    temperaturas.append(temperatura)
    print(temperaturas)

for temperatura in temperaturas:
    soma += temperatura

media = soma / len(temperaturas)

print(f"A média anual das temperaturas: {media:.2f}")


