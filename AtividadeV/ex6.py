def calcularTotal():
	total = 0.0

	while True:
		nome = input("Nome do produto (ou 'fim' para encerrar): ")
		if nome.strip().lower() == "fim":
			break

		preco = float(input("Preço unitário: R$ "))
		quantidade = int(input("Quantidade: "))
		total += preco * quantidade

	return total


def analisar_frase(frase):
	total_caracteres = len(frase)
	letras = numeros = espacos = 0
	indice = 0

	while indice < total_caracteres:
		caractere = frase[indice]
		if caractere.isalpha():
			letras += 1
		elif caractere.isdigit():
			numeros += 1
		elif caractere.isspace():
			espacos += 1
		indice += 1

	palavras = len(frase.split())
	return total_caracteres, letras, numeros, espacos, palavras


if __name__ == "__main__":
	total = calcularTotal()
	print(f"Valor total da compra: R$ {total:.2f}")

	frase = input("Digite uma frase: ")
	caracteres, letras, numeros, espacos, palavras = analisar_frase(frase)
	print(f"Quantidade total de caracteres: {caracteres}")
	print(f"Quantidade de letras: {letras}")
	print(f"Quantidade de números: {numeros}")
	print(f"Quantidade de espaços: {espacos}")
	print(f"Quantidade de palavras: {palavras}")
