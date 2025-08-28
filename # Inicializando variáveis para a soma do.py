# Inicializando variáveis para a soma dos positivos e contagem dos negativos
soma_positivos = 0
quantidade_negativos = 0
for i in range(20):
    valor = int(input(f"Digite o {i+1}º valor: "))
    
    if valor > 0:
        soma_positivos += valor
    elif valor < 0:
        quantidade_negativos += 1
print(f"A soma dos números positivos é: {soma_positivos}")
print(f"A quantidade de valores negativos é: {quantidade_negativos}")
