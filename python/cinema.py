total = 0
dinheiro = 0
acc_idadedes = 0

while True:
    idade = int(input('Qual a sua idade: '))
    if idade == 0:
        break
    
    total =+ 1
    acc_idadedes += idade
    
    if idade < 3:
        ingresso = 0
        
    else:
        if idade > 12: 
            ingresso = 30
        else:
            ingresso = 15
            
    dinheiro += ingresso
    
media = acc_idadedes/ total

if total > 0:
    print(f'O total de pessoas é: {total}')
    print(f'O total arrecadado: {dinheiro}')
    print(f'A média arrecadada: {media}')


        
        
    
 