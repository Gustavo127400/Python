import math 
print('Seja bem-vindo ao programa do Gustavo!')
print('GitHub: Gustavo127400')
print('Linkedln: www.linkedin.com/in/gustavo-de-souza-481455201/')
print('')
print('________________________PERÍMETRO DAS FIGURAS GEOMÉTRICAS________________________')
print('Figuras: Quadrado, Triângulo, Esfera, Retângulo e Losango.')
print('____________________________________________________________________________')
figura = input('Qual é a figura geométrica? ')
        
#FIGURA GEOMÉTRICA | QUADRADO      
if(figura == 'Quadrado'):
        l1 = float(input('Qual valor do lado 1? '))
        l2 = float(input('Qual valor do lado 2? '))
        l3 = float(input('Qual valor do lado 3? '))
        l4 = float(input('Qual valor do lado 4? '))
        formula1 = l1+l2+l3+l4
        print('____________________________________________________________________________')
        print('O perímetro do quadrado é: ' +  str(formula1))    
#FIGURA GEOMÉTRICA | TRIÂNGULO         
elif (figura == 'Triângulo'):
        l1 = float(input('Qual valor do lado 1? '))
        l2 = float(input('Qual valor do lado 2? '))
        l3 = float(input('Qual valor do lado 3? '))
        formula1 = l1+l2+l3
        print('____________________________________________________________________________')    
        print('O perímetro do triângulo é: ' + str(formula1))
 # FIGURA GEOMÉTRICA | ESFERA 
elif(figura == 'Esfera'):
    raio  = float(input('Qual o valor do raio? '))
    formula = 2*math.pi*raio
    print('____________________________________________________________________________')
    print('O perímetro da esfera é: ' + str(formula))
# FIGURA GEOMÉTRICA | RETÂNGULO 
elif(figura == 'Retângulo'):
    l1 = float(input('Qual valor do lado 1? '))
    l2 = float(input('Qual valor do lado 2? '))
    l3 = float(input('Qual valor do lado 3? '))
    l4 = float(input('Qual valor do lado 4? '))
    formula = l1+l2+l3+l4
    print('____________________________________________________________________________')
    print('O perímetro do retângulo é: ' +  str(formula))  
#FIGURA GEOMÉTRICA | LOSANGO         
elif(figura == 'Losango'):
    l1 = float(input('Qual valor do lado 1? '))
    l2 = float(input('Qual valor do lado 2? '))
    l3 = float(input('Qual valor do lado 3? '))
    l4 = float(input('Qual valor do lado 4? '))
    formula = l1+l2+l3+l4
    print('____________________________________________________________________________')
    print('O perímetro do Losango é: ' + str(formula))
else:
    print('Figura não encontrada!')
    print('Fim do programa.')

print('____________________________________________________________________________')
print('Obrigado por visualizar esse código, gratidão.') 
print('Não se esqueça de favoritar esse código :D')
