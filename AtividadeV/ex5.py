def validar_senha(senha):
	return (
		len(senha) >= 8
		and any(letra.isupper() for letra in senha)
		and any(letra.islower() for letra in senha)
		and any(caractere.isdigit() for caractere in senha)
	)


senha = input("Digite uma senha: ")
while not validar_senha(senha):
	print("Senha inválida. Ela deve ter pelo menos 8 caracteres, uma letra maiúscula, uma minúscula e um número.")
	senha = input("Digite uma nova senha: ")

print("Senha válida!")
