usuario="admin"
senha="12345"
login=input("Usuario: ")
pwd = input("Senha: ")
if login==usuario:
    if pwd==senha:
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta!")
else:
    print("Usuario inexistente!")