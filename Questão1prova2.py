numero = int(input("Digite um número inteiro: "))
qtd_impares = 0

for digito in str(num):
    if int(digito) % 2 != 0:
        qtd_impares += 1

fat = 1 
for i in range(1, qtd_impares + 1):
    fat *= i

print("Resultado:", fat)