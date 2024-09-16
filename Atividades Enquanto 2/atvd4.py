while True:
    nome = input("Digite um nome (com mais de 15 letras): ")
    
    if len(nome) > 15:
        print("Nome aceito!")
        break #enecerrando o while
    else:
        print("O nome deve ter mais de 15 letras, faz dnv meo")