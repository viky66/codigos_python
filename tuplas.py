#Trabalhando com tuplas

objetos = ('Lápis','Borracha','Caderno') #criação, muda a forma como são organizados

print(type(objetos)) #type exibe o tipo de dados que é o objetos, que nesse caso é 'tuple'

print(objetos)
print(objetos[1]) #exibe o item da posição 1

# exibindo todos os dados da tupla
print('-'*50)

#for item in range(0,3): # ignora o 3, range cria uma lista, so que objetos ja é uma coleção, entao usa objetos no lugar do range
    #print(objetos[item])

#for item in objetos:
    #print(item)

objetos[0] = 'Caneta' #ocorre um erro pois os valores de uma tupla são imutaveis
print(objetos)