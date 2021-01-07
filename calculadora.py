#Calculadora Do Ratão

primeiro_numero= float(input('Digite o primeiro número:'))
segundo_numero=float(input('Digite o segundo número:'))

#Operações Matemáticas
soma=primeiro_numero+segundo_numero
subtracao=primeiro_numero-segundo_numero
multiplicacao=primeiro_numero*segundo_numero
divisao=primeiro_numero/segundo_numero

#Resultado dos Calculos
print(f'A soma entre { primeiro_numero} e { segundo_numero} é igual {soma}')
print(f'A subtração entre { primeiro_numero} e { segundo_numero} é igual {subtracao}')
print(f'A multiplicação entre { primeiro_numero} e { segundo_numero} é igual {multiplicacao}')
print(f'A divisão entre { primeiro_numero} e { segundo_numero} é igual {divisao}')