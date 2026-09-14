""" Identificação do estudante: Gabriel Vasconcelos Franco Martins
Nome da atividade: Avaliação Formativa - Lista de Exercícios IV

==================================================
Questão 1 - Números de 1 a 20
==================================================
Enunciado: Desenvolver um programa em Python que utilize a estrutura for para percorrer os números de 1 a 20. 
Exibir todos os números, identificar quais são pares e apresentar a quantidade de números pares encontrados.
 """
# Código-fonte:
pares = 0
print("Números de 1 a 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} (Par)")
        pares += 1
    else:
        print(i)
print(f"\nQuantidade de números pares: {pares}")

# Explicação da lógica: O laço for itera de 1 a 20. O operador módulo % verifica se o resto da divisão por 2 é 
# zero para identificar os pares e incrementar o contador.