numero = int(input("Digite um número: "))
n = numero
soma = 0
while n > 0:
 digito = n % 10
 if digito == 2 or digito == 3 or digito == 5 or digito == 7:
   soma += digito
 n //= 10
print("A soma dos números primos do número" , numero , "é: " , soma)