""" ==================================================
Questão 8 - Pesquisa de Números
==================================================
Enunciado: Solicite ao usuário 10 números inteiros e armazene-os em uma lista. 
Utilize for para exibir os números digitados e contar quantos são positivos, 
negativos e iguais a zero. """

# Código-fonte:
numeros = [0] * 10
positivos = 0
negativos = 0
zeros = 0

for i in range(10):
  numeros[i] = int(input(f"Digite o {i+1}° número: "))

print(f"\nNúmeros digitados: {numeros}")

for num in numeros:
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")

# Explicação da lógica: Usa um for com range(10) para popular a lista 
# com .append(). Depois, outro for itera sobre a lista classificando cada número.