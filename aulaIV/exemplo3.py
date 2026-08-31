valor_fatura = float(input('Digite o valor da fatura: '))
dias_atraso = int(input('Digite o número de dias de atraso: '))
valor_final = 0

if dias_atraso > 10:
    valor_final = valor_fatura + valor_fatura * 0.1
else:
    valor_final = valor_fatura + valor_fatura * 0.05
print('Você atrasou a sua fatura em {} dias. O valor da fatura com juros é R$ {:.2f}.'.format(dias_atraso, valor_final))