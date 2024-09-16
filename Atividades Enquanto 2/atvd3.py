contador = 1 #inicializando a variavel
soma = 0
negativos = 0

while contador <= 10:
        valor = int(input(f"Digite o valor inteiro {contador}: "))

        if valor < 0:
            negativos = negativos + 1
        else:
              soma = soma + valor #soma += valor


print(f"A soma dos valores é: {soma}")
print(f"A quantidade de valores negativos é: {negativos}")