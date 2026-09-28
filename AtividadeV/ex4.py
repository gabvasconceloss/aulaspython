def calcular_media(notas):
    """Calcula e retorna a média das notas de um estudante."""
    return sum(notas) / len(notas)


estudantes = {}

while True:
    nome = input("Nome do estudante (ou 'sair' para encerrar): ").strip()
    if nome.lower() == "sair":
        break
    if not nome:
        print("Informe um nome válido.")
        continue

    notas = []
    for i in range(1, 5):
        while True:
            try:
                nota = float(input(f"Nota {i} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Digite um número válido.")

    estudantes[nome] = notas

print("\n--- Resultado ---")
for nome, notas in estudantes.items():
    media = calcular_media(notas)
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    print(f"Nome: {nome} | Média: {media:.2f} | Situação: {situacao}")