A = int(input('Digite o primeiro lado do triangulo: '))
B = int(input('Digite o segundo lado do triangulo: '))
C = int(input('Digite o terceiro lado do triangulo: '))

if((A > 0 and B > 0 and C >0) and (A + B > C and A + C > B and B + C > A) ):
    #se chegou até aqui é porque o triangulo é valido!
    if(A != B and A != C and B != C):
        print('O triangulo é escaleno')
        
    elif(A == B and B == C):
        print('O triangulo é equilatero')
    
    else:
        print('O triangulo é isoceles')
else:
    print('Ao menos um dos valores indicados não servem para formar um triangulo')
    