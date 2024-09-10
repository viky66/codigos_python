frequencia = float(input("Informe a frequencia do aluno: "))
nota_final = float(input("Informe a nota final do aluno: "))

if nota_final >= 7 and frequencia >= 75:
    print("O aluno está aprovado!")
else:
    print("O aluno está reprovado!")