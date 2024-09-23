velocidade = float(input("Informe a velocidade registrada do veículo (km/h): "))
limite = float(input("Informe o limite da velocidade na via (km/h): "))

def calculo_multa(velocidade, limite):

    if velocidade <= limite:
        return "sem multa"
    elif 1 <= velocidade - limite <= 10:
        return "A multa é um total de: R$ 50,00"
    elif 11 <= velocidade - limite <= 20:
        return "A multa é um total de: R$ 100,00"
    else: 
        return "A multa é um total de R$ 200,00"

resultado = calculo_multa(velocidade, limite)
print(resultado)