while True:
    login1 = input("Informe o seu login: ")
    senha1 = input("Informe sua senha: ")

    if login1 != senha1:
        while True:
            login2 = ("Informe o login da pessoa 2: ")
            senha2 = ("Informe a senha da pessoa 2: ")

            if login2 != login1 and login2 != senha2:
                break
            else:
                print("Login e senha são iguais")

    break
else:
    print("Login1 e senha1 são iguais")