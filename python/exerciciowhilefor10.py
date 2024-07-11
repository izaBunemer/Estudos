print('LANCHONETE')

print('1 - coxinha RS 5,00')
print('2 - pastel RS 7,00')
print('3 - café RS 4,00')
print('4 - suco RS 6,00')
print('5 - SAIR')

total = 0 
while True:
    op = int(input('Qual item gostaria de comprar? '))
    qtd = int(input('Quantas unidades que comprar? '))
    
    if (op == 1):
        total = total + qtd * 5.00 
    elif (op == 2):
        total = total + qtd * 7.00    
    elif (op == 3):
        total = total + qtd * 4.00       
    elif (op == 4):
        total = total + qtd * 6.00    
             
    elif (op == 5):
        break
        
    else:
        print('Produto invalido!! Selecione outro.')
        
print(f'O total gasto no pedido é de RS: {total}.')
        
