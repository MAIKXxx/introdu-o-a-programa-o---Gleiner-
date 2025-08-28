# Inicializa as variáveis para controle
maior_media = float('-inf')
menor_media = float('inf')
alunos_aprovados = 0
alunos_reprovados = 0
for i in range(1, 11):
    print(f"Aluno {i}:")
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    media = (n1 + n2 + n3) / 3
    if media > maior_media:
        maior_media = media
    if media < menor_media:
        menor_media = media
    if media >= 6:
        alunos_aprovados += 1
    else:
        alunos_reprovados += 1
print(f"\nMaior média: {maior_media:.2f}")
print(f"Menor média: {menor_media:.2f}")
print(f"Quantidade de alunos aprovados: {alunos_aprovados}")
print(f"Quantidade de alunos reprovados: {alunos_reprovados}")
