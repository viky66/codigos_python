contador = 1 #inicializando uma variavel 

while contador <= 5:
    print(contador)
    contador = contador + 1 #é o mesmo que contador +=1

print("="*40)

#2ª forma de utilizar o while - loop condicional normal

valor = 0 #inicializando a variavel
while valor >=0:
    valor = int(input("Informe um valor qualquer(digite um valor negativo para terminar): "))

    print(f"Voce digitou {valor}")

#3ª forma de utilizar while - como se fosse faça...
while True:
    senha = input("Informe a senha: ")
    if senha == "123" : 
        print("Parabéns, senha correta!")
        break #forma de encerrar o while
    else:
        print("Senha incorreta, tente novamente.")