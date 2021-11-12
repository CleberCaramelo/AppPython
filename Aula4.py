nota = int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('Nota inválida. Entre com a nota correta: '))
print(nota)

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# a = int(input('Entre com o numero: '))
# #for x in range(100):
# #    print(x)
# div = 0
# for x in range(1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div +=  1
#
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))