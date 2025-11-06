
soma_idade = 0
qtd = 0
maior_peso_m = 0
nome_maior_peso_m = ""
maior_altura_f = 0
nome_maior_altura_f = ""

while True:
    nome = input("Nome do atleta (@ para sair): ")
    if nome == "@":
        break
    sexo = input("Sexo (M/F): ").upper()
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))

    soma_idade += idade
    qtd += 1

    if sexo == "M" and peso > maior_peso_m:
        maior_peso_m = peso
        nome_maior_peso_m = nome
    if sexo == "F" and altura > maior_altura_f:
        maior_altura_f = altura
        nome_maior_altura_f = nome

if qtd > 0:
    media_idade = soma_idade / qtd
    print("Atleta masculino com maior peso:", nome_maior_peso_m)
    print("Atleta feminina com maior altura:", nome_maior_altura_f)
    print("Média de idade dos atletas:", round(media_idade, 1))
else:
    print("Nenhum atleta foi cadastrado.")