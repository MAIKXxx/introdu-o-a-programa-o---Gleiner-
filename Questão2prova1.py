numero=int(input("Digite um número: "))
n=numero
binario=0
base=1
while n > 0:
    resto = n % 2
    binario = binario + resto * base
    n = n // 2
    base = base * 10
print("A conversão do número" , numero , "em binário é: " , binario)
