num = input("Digite um numero: ")
soma = 0 

for dig in num:
    soma += int(dig)

media = soma / len(num)

mais_prox = min(num, key=lambda x: abs(int(x)) - media)
print("Digito mais proximo da media:", mais_prox)