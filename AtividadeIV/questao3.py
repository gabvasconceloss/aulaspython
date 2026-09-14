""" ==================================================
Questão 3 - Soma dos Números
==================================================
Enunciado: Crie um programa que utilize for para percorrer os números de 1 a 50 e calcular a 
soma de todos os números, a soma somente dos números pares e a soma somente dos números ímpares. """

# Código-fonte:
soma_total = 0
soma_pares = 0
soma_impares = 0

for i in range(1, 51):
    soma_total += i
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i

print(f"Soma total: {soma_total}")
print(f"Soma dos pares: {soma_pares}")
print(f"Soma dos ímpares: {soma_impares}")

# Explicação da lógica: Três acumuladores armazenam as somas. O laço percorre de 1 a 50, 
# adicionando o valor à soma_total e usando uma condicional para direcionar o valor para 
# soma_pares ou soma_impares.