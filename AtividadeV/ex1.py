def autenticar(usuario, senha):
	return usuario == "admin" and senha == "1234"


tentativas = 0
autorizado = False

while tentativas < 3 and not autorizado:
	usuario = input("Digite o usuário: ")
	senha = input("Digite a senha: ")

	if autenticar(usuario, senha):
		autorizado = True
		print("Acesso autorizado!")
	else:
		tentativas += 1
		print("Usuário ou senha incorretos.")

if not autorizado:
	print("Acesso bloqueado.")

