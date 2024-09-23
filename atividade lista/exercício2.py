valores = []

# Passo 2: Solicitar ao usuário 10 valores inteiros e inseri-los na lista
print("Por favor, insira 10 valores inteiros:")
for contador in range(10):
    valor = int(input(f"Digite o valor {contador + 1}: "))
    valores.append(valor)
            
# Passo 3: Verificar a existência de elementos iguais a 10 e mostrar suas posições
print("Posições (índices) onde o valor 10 aparece:")

for contador in range(len(valores)):
    if valores[contador] == 10:
        print(f"Valor 10 encontrado na posição: {contador}")
    
