i = 0
maior = -1
menor = 11
aprovados = reprovados = 0 

while 1 < 10:
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    media % (N1 + N2 + N3) / 3
     
    maior = media if media > maior else maior
    menor = media if media < menor else menor
    aprovados += 1 if media >= 6 else 0 
    reprovados += 1 if  media < 6 else 0 
    
    1 += 1 
print("/maior media:", maior)
print("menor media:", menor)
print("aprovados:", aprovados)
print("reprovados:", reprovados)