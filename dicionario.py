pessoa = ["Maria", "48", "Rua 10"]
print(pessoa)

# Iniciando com dicionário
dados_pessoais = {
    'Nome':'João',
    'Idade':23,
    'Endereço':'Avenida 4'
}

print(dados_pessoais)

# Exibindo as chaves utilizando o comando keys ()
print(dados_pessoais.keys())

# Exibindo os valores utilizando o comando values ()
print(dados_pessoais.values())

# Exibindo tanto a chave quanto o valor com o comando items ()
print(dados_pessoais.items())

# Exibindo o dicionário detalhado

for chave, valor in dados_pessoais.items():
    print(f"{chave} : {valor}")

# Realizando operações com dicionário
# Adicionando dados ao dicionário
# FORMA - 1
dados_pessoais["Peso"] = 68
print(dados_pessoais)

# FORMA - 2, usando update()
dados_pessoais.update({"Profissão":"Engenheiro"})
print(dados_pessoais)

# Remover dados do dicionário
# FORMA - 1, usando pop()
dados_pessoais.pop("Endereço")# preciso passar a chave para poder excluir o registro
print(dados_pessoais)

# FORMA - 2, usando del()
del(dados_pessoais["Idade"])
print(dados_pessoais)