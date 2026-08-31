# Programa para calcular a média e a situação do aluno

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7.0:
    situacao = "Aprovado"
elif media >= 5.0:
    situacao = "Em recuperação"
else:
    situacao = "Reprovado"

print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")
