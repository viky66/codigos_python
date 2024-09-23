import time

contador = 0
segundos = int(input("Digite o número de segundos: "))

while contador <= segundos:
    print(contador)  
    time.sleep(1)  #Pausa de 1 segundo
    contador += 1  