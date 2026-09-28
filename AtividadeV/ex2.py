
def cadastrar_produto(produtos, nome, preco):
	produtos[nome] = preco


produtos = {}

while True:
	nome = input("Nome do produto: ").strip()
	while not nome:
		print("O nome do produto não pode ficar vazio.")
		nome = input("Nome do produto: ").strip()

	while True:
		try:
			preco = float(input("Preço do produto: R$ ").replace(",", "."))
			if preco > 0:
				break
			print("O preço deve ser maior que zero.")
		except ValueError:
			print("Digite um preço válido.")

	cadastrar_produto(produtos, nome, preco)

	continuar = input("Deseja cadastrar outro produto? (s/n): ").strip().lower()
	if continuar != "s":
		break

print("\nProdutos cadastrados:")
for nome, preco in produtos.items():
	print(f"{nome}: R$ {preco:.2f}")
