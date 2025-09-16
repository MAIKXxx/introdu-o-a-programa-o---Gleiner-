def soma(a, b):
    return a + b

def subtração(a, b):
    return a -  b

def multiplicação(a, b):
    return a * b

def divisão(a, b):
    if b == 0:
        return "erro: divisão por zero!"
    return a / b 

def par_ou_impar(n):
    return "par" if n % 2 == 0 else "impar"

def primo(n):
    if n <= 1:
        return "Não é primo"
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return "Não é primo"
        return "É primo"
    
    def fatorial(n):
        if n < 0:
            return "Não existe fatorial de número negativo!"
        fat = 1 
        for i in range(1, n + 1):
            fat *= i
        return fat 
    
while True:
    print("\n=== MENU DE OPERAÇÕES ===")
    print("1 - Soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - par ou impar")
    print("6 - número primo")
    print("7 - fatorial")
    print("0 - sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("saindo... até mais!")
        break

    # para operações com dois 