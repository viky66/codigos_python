#função com retorno
def somar(num1, num2):
    resultado = num1 + num2

    return resultado #devolvendo o valor para quem chamou a função

#chamando a função
print(somar(10,5))

#função sem retorno
def multiplicar(valor1, valor2):
    resultado = valor1 * valor2
    print(resultado)

#chamando a função
multiplicar(2,6)