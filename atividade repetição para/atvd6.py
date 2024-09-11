num = int(input("Digite um número inteiro: "))

soma_div = 0

for i in range(1, num):
    if num % i == 0:
        soma_div += i
    
# Verifica se o número é perfeito e exibe o resultado
if soma_div == num:
    print(f"O número {num} é um número perfeito.")
else:
    print(f"O número {num} não é um número perfeito.")
