'''
Essa estrutura de repetição é o mais comum em qualquer outra linguagem de programação
for (contador = 1; contador <= 5; contador++){

}
'''

#1ª exemplo
for contador in range(1,6):
    print(contador)

print("-"*30)
#2ª exemplo
for contador in range(1,11,2):# o 3ª parâmetro irá aumentar os valores que estão sendo exibidos, adi~ção próximo valor
    print(contador)

print("-"*30)
#3ª exemplo - números do maior para o menor
for contador in range(10,0,-1):
    print(contador,end=" ")#o comando end, informa como python irá mostrar o final de uma exibição, por padrão irá dar um enter(\n)