print('Escolha qual fruta deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Qual a sua escolha? '))
qtd = int(input('Qual a quantidade escolhida? '))

if (produto == 1):
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} maças. O valor a se pagar é {pagar}')
    
else:
    if(produto == 2):
        pagar = qtd * 3.6
        print(f'Você comprou {qtd} laranjas. O valor a se pagar é {pagar}')
        
    else:
        if(produto == 3):
            pagar = qtd * 1.85
            print(f'Você comprou {qtd} de bananas. O valor a se pagar é {pagar}')
            
        else:
            print('produto inexistente!')