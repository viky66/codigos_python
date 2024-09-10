horas = float (input("Informe a quantidade de horas trabalhadas: "))
valor_hora = float (input("Informe o valor por hora: "))

if horas > 40:
    horas_normais = 40
    horas_extras = horas - 40
    salario_base = horas_normais * valor_hora
    bonus = horas_extras * valor_hora * 1.5

else:
    horas_extras = horas 
    horas_extras= 0
    salario_base = horas * valor_hora
    bonus = 0

    salario_total = salario_base + bonus

print(f"O salário total é: R${salario_total:.2f}")