qtd_jogadores = int(input("Digite o numero de jogadores: "))
1 = 0 
soma_alturas = 0 

while i < qtd_jogadores:
    altura = float(input(f"Digite a altura do jogador {i+1}: "))
    soma_alturas += altura
    i +=1 

media = soma_alturas / qtd_jogadores 
print("A altura média do time é:", media)