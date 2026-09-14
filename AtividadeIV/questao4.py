""" ==================================================
Questão 4 - Lista de Notas
==================================================
Enunciado: Utilizando for, percorra a lista de notas, exiba cada nota, calcule a 
média da turma e informe quantos estudantes obtiveram nota maior ou igual a 7.0.
 """
# Código-fonte:
notas = [7.5, 8.0, 6.5, 9.0, 5.5, 8.5]
soma = 0
aprovados = 0

print("Notas da turma:")
for nota in notas:
    print(f"- {nota}")
    soma += nota
    if nota >= 7.0:
        aprovados += 1

media = soma / len(notas)
print(f"\nMédia da turma: {media:.2f}")
print(f"Estudantes com nota >= 7.0: {aprovados}")

# Explicação da lógica: O for itera diretamente sobre os elementos da lista notas. 
# A função len() ajuda a calcular a média dividindo a soma acumulada pelo total de elementos.