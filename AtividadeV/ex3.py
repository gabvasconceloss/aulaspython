def contar_palavras(frase):
	palavras = frase.lower().split()
	contagem = {}

	for palavra in palavras:
		contagem[palavra] = contagem.get(palavra, 0) + 1

	return contagem


frase = input("Digite uma frase: ")
print(contar_palavras(frase))
