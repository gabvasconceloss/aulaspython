# Exemplo com entrada de dados do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá, {nome}!")

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

if idade >= 65:
    print("Você está na faixa etária de idoso.")
elif idade >= 18:
    print("Você está na faixa etária adulta.")
elif idade >= 12:
    print("Você está na faixa etária adolescente.")
else:
    print("Você está na faixa etária infantil.")
