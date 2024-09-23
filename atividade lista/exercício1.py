valores = []
impar = 0
contador = 0

print("Por favor, insira 7 valores:")
for contador in range(7):
        valor = int(input(f"Digite o valor {contador + 1}: "))
        valores.append(valor) #novo item no final da lista
        print(valores)

# Contar a quantidade de números ímpares na lista
for elementos in valores: #valores é a lista
    if elementos % 2 != 0: #calcula o resto da divisão por 2, elementos % 2 != 0 é True, significa que elementos é um número ímpar.
        impar += 1 #adiciona 1 ao contador de números ímpares sempre que um número ímpar é encontrado

# Mostrar o resultado
print(type(f"A quantidade de números ímpares na lista é: {impar}"))
            