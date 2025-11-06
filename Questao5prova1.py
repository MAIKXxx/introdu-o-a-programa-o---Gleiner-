n = int(input("Digite um número: "))
soma = 0
texto = ""

for i in range(1, n + 1):
    fatorial = 1
    for j in range(1 , i + 1):
        fatorial = fatorial * j
    soma = soma + fatorial 

    if i == 1:
        texto == "1!"
    else: 
        texto= texto + "+" + str(i) + "!"
print(texto, "=" , soma)