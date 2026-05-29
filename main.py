def saudacao(nome):
    return f"Olá, {nome}!"

if __name__ == "__main__":
    print(saudacao("FATEC"))



def saudacao(nome):
    return f"Olá, {nome}!"

# O CodeQL agora vai detectar que o usuário pode digitar código malicioso
def calculadora_vulneravel():
    entrada_usuario = input("Digite a expressão: ")
    return eval(entrada_usuario)

if __name__ == "__main__":
    print(saudacao("FATEC"))