""" ==================================================
Questão 9 - Análise de Vendas
==================================================
Enunciado: Uma empresa registrou vendas durante 6 dias. 
Desenvolva um programa utilizando for para exibir as vendas de cada dia, 
calcular o total, a média diária, identificar os dias acima da média e informar 
o maior número de vendas. """

# Código-fonte:
vendas = [15, 22, 18, 30, 25, 20]
total = 0
maior_venda = vendas[0]

for i in range(len(vendas)):
    print(f"Dia {i+1}: {vendas[i]} produtos")
    total += vendas[i]
    if vendas[i] > maior_venda:
        maior_venda = vendas[i]

media = total / len(vendas)

print(f"\nTotal de produtos vendidos: {total}")
print(f"Média diária de vendas: {media:.2f}")
print(f"Maior número de vendas registrado: {maior_venda}")

print("\nDias com vendas acima da média:")
for i in range(len(vendas)):
    if vendas[i] > media:
        print(f"Dia {i+1} ({vendas[i]} vendas)")

# Explicação da lógica: A função enumerate() foi utilizada junto com o for para acessar 
# tanto o índice (representando o dia) quanto o valor da venda na lista.