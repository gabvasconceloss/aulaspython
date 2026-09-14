""" ==================================================
Questão 2 - Tabuada
==================================================
Enunciado: Desenvolva um programa que solicite ao usuário um número inteiro e utilize for para 
apresentar a tabuada desse número de 1 a 10.
 """
# Código-fonte:
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Explicação da lógica: O usuário insere um valor. O laço for gera multiplicadores de 1 a 
# 10, multiplicando o valor inserido e formatando a saída.
