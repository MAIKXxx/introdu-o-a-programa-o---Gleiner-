
a, b = 1, 1
for i in range(3, 52):
    a, b = b, a + b

print("51º termo da sequência:", b)