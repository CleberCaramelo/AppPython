#a = 10
#b = 5
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('soma: {soma}; \nsubtração: {subtracao}; '
      '\nMultiplicação: {multiplicacao};'
      '\nDivisão: {divisao};'
      '\nResto: {resto}.'.format(soma=soma,
                                subtracao=subtracao,
                                resto=resto,
                                multiplicacao=multiplicacao,
                                divisao=divisao))
print(resultado)
#print('soma: ' + str(soma))
#print('subtracao: ' + str(subtracao))
#print(multiplicacao)
#print(int(divisao))
#print(divisao)
#print(resto)
#x = '1'
##soma2 = int(x) + 1
#print(soma2)
