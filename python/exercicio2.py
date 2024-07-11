km = int(input('Quantos Km foram percorridos?: '))
dias = int(input('Quantos dias foram percorridos?'))

preco = 60 * dias + 0.15 * km

print('km = {km}. Dias: {dias}')
print(f'Valor a ser pago: {preco}')