comp = float(input("Informe o comprimento da caixa: "))#estamos convertendo os valores textuais em valores decimais
larg = float(input("Informe a largura da caixa: "))
alt = float(input("Informe a altura da caixa: "))

volume = (comp + larg + alt)

print(f"O volume da sua caixa é {volume:.2f}")