n = int(input("Digite um número inteiro: "))

soma_div = 0

for i in range(1, n):
    if n % i == 0:
        soma_div += i
    
# Verifica se o número é perfeito e exibe o resultado
if soma_div == n:
    print(f"O número {n} é um número perfeito.")
else:
    print(f"O número {n} não é um número perfeito.")
