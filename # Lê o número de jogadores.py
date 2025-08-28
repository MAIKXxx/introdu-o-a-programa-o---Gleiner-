# Lê o número de jogadores
num_jogadores = int(input("Digite o número de jogadores do time: "))
soma_alturas = 0
for i in range(1, num_jogadores + 1):
    altura = float(input(f"Digite a altura do jogador {i} (em metros): "))
    soma_alturas += altura 
altura_media = soma_alturas / num_jogadores
print(f"A altura média do time é: {altura_media:.2f} metros")