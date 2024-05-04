import math 
print('Seja bem-vindo ao programa do Gustavo!')
print('GitHub: Gustavo127400')
print('Linkedln: www.linkedin.com/in/gustavo-de-souza-481455201/')
print('')
print('________________________ÁREA DAS FIGURAS GEOMÉTRICAS________________________')
print('Figuras: Quadrado, Triângulo, Esfera, Retângulo e Losango.')
print('____________________________________________________________________________')
figura = input('Qual é a figura geométrica? ')

if(figura == 'Quadrado'):
        b = float(input('Qual o valor da base? '))
        h = float(input('Qual o valor da altura? '))
        formula1 = b*h
        print('____________________________________________________________________________')
        print('A área do quadrado é: ' +  str(formula1))
        
#FIGURA GEOMÉTRICA | TRIÂNGULO         
elif (figura == 'Triângulo'):
        b = float(input('Qual é o valor da base? '))
        h = float(input('Qual é o valor da altura? '))
        formula1 = (b * h) / 2
        print('____________________________________________________________________________')    
        print('A área do triângulo é: ' + str(formula1))
 # FIGURA GEOMÉTRICA | ESFERA 
elif(figura == 'Esfera'):
    raio  = float(input('Qual o valor do raio? '))
    formula = 4*math.pi*raio**2
    print('____________________________________________________________________________')
    print('A área da esfera é: ' + str(formula))
# FIGURA GEOMÉTRICA | RETÂNGULO 
elif(figura == 'Retângulo'):
    b = int(input('Qual o valor da base? '))
    h = int(input('Qual o valor da altura? '))
    formula = b*h
    print('____________________________________________________________________________')
    print('A área do retângulo é: ' +  str(formula))  
#FIGURA GEOMÉTRICA | LOSANGO         
elif(figura == 'Losango'):
     dMaior = int(input('Qual é o valor da diagonal maior? ')) 
     dMenor = int(input('Qual é o valor da diagonal menor? ')) 
     formula = (dMaior*dMenor)/2
     print('____________________________________________________________________________')
     print('A área do Losango é: ' + str(formula))
else:
    print('Figura não encontrada!')
    print('Fim do programa.')

print('____________________________________________________________________________')
print('Obrigado por visualizar esse código, gratidão.') 
print('Não se esqueça de favoritar esse código :D')
