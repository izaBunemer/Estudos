#Exibindo menu de pratos:
print('Escolha seu ramen e envie para nós!')
print('1 - Tonkotso misso ramen')
print('2 - Tonkotso shio ramen')
print('3 - Shoyo ramen de frango')
print('4 - Shio ramen de frango')

total_pagar = 0

# Loop para pedidos de pratos
while True:
    pedido = int(input('o que você gostaria de pedir? (Digite 0 para finalizar o pedido!) '))
    if pedido == 0:
        break

    qtd = int(input('Quantas unidades voce gostaria de pedir?'))

    if (pedido == 1):
        pagar = qtd * 33.90
        print(f'Você pediu {qtd} Tonkotso misso ramen. O total parcial do pedido é {pagar} reais. ')
    
    elif (pedido == 2):
        pagar = qtd * 30.90
        print(f'Você pediu {qtd} Tonkotso shio ramen. O total parcial do pedido é {pagar} reais. ')

    elif (pedido == 3):
        pagar = qtd * 29.90
        print(f'Você pediu {qtd} Shoyo ramen de frango. O total parcial do pedido é {pagar} reais. ')
    
    elif (pedido == 4):
        pagar = qtd * 27.90
        print(f'Você pediu {qtd} Shio ramen de frango. O total parcial do pedido é {pagar} reais. ')   
    
    else:
        print('Ramen inexistente!!') 
        
    
        continue
    
    total_pagar += pagar
    
#Exibindo menu de bebidas
print('\nEscolha sua bebida :')
print('1 - Coca-Cola')
print('2 - Coca-Cola Zero')
print('3 - Guaraná Antártica')
print('4 - Guaraná Antártica Zero')
print('5 - Chá Verde')
print('6 - Suco Natural de Laranja')

#Loop para pedido de bebidas
while True:
    pedido = int(input('Qual bebida você gostaria de pedir? (Digite 0 para finalizar o pedido de bebidas!) '))
    if pedido == 0:
        break

    qtd = int(input('Quantas bebidas você gostaria de pedir? '))
    
    if pedido == 1:
        pagar = qtd * 5.50
        print(f'Você pediu {qtd} Coca-Cola. O total parcial do pedido é {pagar:.2f} reais.')
        
    elif pedido == 2:
        pagar = qtd * 5.50
        print(f'Você pediu {qtd} Coca-Cola Zero. O total parcial do pedido é {pagar:.2f} reais.')
        
    elif pedido == 3:
        pagar = qtd * 5.50
        print(f'Você pediu {qtd} Guaraná Antártica. O total parcial do pedido é {pagar:.2f} reais.')
        
    elif pedido == 4:
        pagar = qtd * 5.50
        print(f'Você pediu {qtd} Guaraná Antártica Zero. O total parcial do pedido é {pagar:.2f} reais.') 
        
    elif pedido == 5:
        pagar = qtd * 6.00
        print(f'Você pediu {qtd} Chá Verde. O total parcial do pedido é {pagar:.2f} reais.')  
    
    elif pedido == 6:
        pagar = qtd * 9.00
        print(f'Você pediu {qtd} Suco Natural de Laranja. O total parcial do pedido é {pagar:.2f} reais.')  
        
    else:
        print('Bebida inexistente!!') 
        continue
    
  

    print(f'\nO total do seu pedido é {total_pagar:.2f} reais.')
    total_pagar += pagar


               





    