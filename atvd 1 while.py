
contador = 0
soma_positivos = 0
quantidade_negativos = 0
while contador < 20:
    valor = int(input(f"Digite o {contador + 1}º valor inteiro: "))
    
    if valor >= 0:
        soma_positivos += valor
    else:
        quantidade_negativos += 1
    
    contador += 1
print(f"\nSoma dos números positivos: {soma_positivos}")
print(f"Quantidade de números negativos: {quantidade_negativos}")