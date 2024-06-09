print('Olá, rede. Sejam bem-vindos! \n')

print('_____________________1ª Lei de Ohm_____________________ \n')

print("Escolha a grandeza que você deseja calcular:")
print("1. Tensão (V)")
print("2. Corrente (I)")
print("3. Resistência (R)")
print('Por exemplo (V), (I) ou (R)')
grandeza = input('Escolha a grandeza que você deseja calcular: ')

if grandeza.upper() == "V":
    print('(1) Tensão (V)\n')
    i = float(input('Qual o valor da corrente (I) em amperes? '))
    r = float(input('Qual o valor da resistência (R) em ohms? '))
    u = r * i
    print(f'O valor da tensão é: {u} V')
          
elif grandeza.upper() == "I":
    print('(2) Corrente (I)\n')
    u = float(input('Qual o valor da tensão (V) em volts? '))
    r = float(input('Qual o valor da resistência (R) em ohms? '))
    i = u / r
    print(f'O valor da corrente elétrica é: {i} A')

elif grandeza.upper() == "R":
    print('(3) Resistência (Ω)\n')
    u = float(input('Qual o valor da tensão (V) em volts? '))
    i = float(input('Qual o valor da corrente (I) em amperes? '))
    r = u / i
    print(f'O valor da resistência é: {r} Ω')

else:
    print('Escolha inválida. Por favor, escolha V, I ou R.')