#tupla se cria com (), lista se cria com []
animais = ['cachorro', 'gato', 'vaca']
print(type(animais)) #exibindo o tipo de variavel

print(animais)

print('-'*50)

#exibindo todos os itens da lista animais

for elementos in animais:
    print(elementos)

#1ª etapa: atualização de dados
print('-'*50)
animais[0] = 'Coelho'
print(animais)

#2ª etapa: Inserir itens na lista
print('-'*50)
#forma 1 - usando append
animais.append("cavalo") #irá inserir um novo item no final da lista, append, insert são unicos das listas
print(animais)

#forma 2 - usando insert
animais.insert(1, "pássaro") #insert precisa de 2 valores, o 1 será índice da lista que deseja inserir o valor, o 2será o conteúdo que quero inserir na lista
print(animais)

#3ª etapa: Excluir itens da lista
print('-'*50)

#forma 1 - usando pop()
animais.pop()#excluir sempre o último item
print(animais)

#forma 2 - usando pop() com indice
animais.pop(0) #aqui escolhe qual indice da lista será excluído
print(animais)

#forma 3 - usando remove
animais.remove("vaca") #irá remover o item pelo seu conteúdo
print(animais)
