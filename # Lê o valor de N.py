# Lê o valor de N
N = int(input("Digite um número N: "))
soma = 0
for i in range(1, N + 1):
    soma += i
print(f"A soma de todos os números inteiros de 1 a {N} é: {soma}")
