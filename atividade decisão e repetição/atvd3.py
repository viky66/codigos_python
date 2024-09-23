def main():
    salario = float(input("Informe o salário atual: "))
    anos = int(input("Informe o tempo de serviço em anos: "))

    if anos <= 5:
        bonificacao = 0.05
    elif 6 <= anos <= 10:
        bonificacao = 0.10
    else:
        bonificacao = 0.15

    bonificacao = salario * bonificacao
    salario_final = salario + bonificacao

    print(f"Valor do bônus: R${bonificacao:.2f}")
    print(f"Salário final com o bônus: R${salario_final:.2f}")


main()
