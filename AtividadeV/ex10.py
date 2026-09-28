def cadastrar_estudante(estudantes):
	"""Cadastra um estudante e sua nota na lista de dicionários."""
	nome = input("Nome: ").strip()

	while True:
		try:
			nota = float(input("Nota: ").replace(",", "."))
			if 0 <= nota <= 10:
				break
			print("A nota deve estar entre 0 e 10.")
		except ValueError:
			print("Informe uma nota válida.")

	estudantes.append({"nome": nome, "nota": nota})
	print("Estudante cadastrado com sucesso.")


def calcular_media(estudantes):
	if not estudantes:
		return 0
	return sum(estudante["nota"] for estudante in estudantes) / len(estudantes)


def maior_nota(estudantes):
	if not estudantes:
		return None
	return max(estudantes, key=lambda estudante: estudante["nota"])


def listar_aprovados(estudantes):
	aprovados = [estudante for estudante in estudantes if estudante["nota"] >= 7]
	if not aprovados:
		print("Nenhum estudante aprovado.")
		return

	print("\nEstudantes aprovados:")
	for estudante in aprovados:
		print(f"- {estudante['nome']}: {estudante['nota']:.1f}")


def main():
	estudantes = []

	while True:
		print("\n1 - Cadastrar estudante")
		print("2 - Exibir média da turma")
		print("3 - Exibir estudante com maior nota")
		print("4 - Listar aprovados")
		print("5 - Sair")
		opcao = input("Escolha uma opção: ").strip()

		if opcao == "1":
			cadastrar_estudante(estudantes)
		elif opcao == "2":
			if estudantes:
				print(f"Média da turma: {calcular_media(estudantes):.2f}")
			else:
				print("Nenhum estudante cadastrado.")
		elif opcao == "3":
			estudante = maior_nota(estudantes)
			if estudante:
				print(f"Maior nota: {estudante['nome']} - {estudante['nota']:.1f}")
			else:
				print("Nenhum estudante cadastrado.")
		elif opcao == "4":
			listar_aprovados(estudantes)
		elif opcao == "5":
			print("Sistema encerrado.")
			break
		else:
			print("Opção inválida.")


if __name__ == "__main__":
	main()
