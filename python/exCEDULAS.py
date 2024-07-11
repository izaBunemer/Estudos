valor = int(input('Digite o valor em reais: '))

while True:
    if valor >= 100:
        cont100 = valor // 100
        valor = valor - cont100 * 100
        print(f'Cédulas de 100: {cont100}')
        if not valor:
            break
        
    if valor >= 20:
        cont20 = valor // 20
        valor = valor - cont20 * 20
        print(f'Cédulas de 20: {cont20}')
        if not valor:
            break
        
    if valor >= 10:
        cont10 = valor // 10
        valor = valor - cont10 * 10
        print(f'Cédulas de 10: {cont10}')
        if not valor:
            break
        
    if valor >= 5:
        cont5 = valor // 5
        valor = valor - cont5 * 5
        print(f'Cédulas de 5: {cont5}')
        if not valor:
            break
        
    if valor:
        cont1 = valor
        print(f'Cédulas de1 1: {cont1}')
        
        break