class Calculadora:
    # def __init__(self):
    #         pass

    def soma(self,valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self,valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self,valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self,valor_a, valor_b):
        return valor_a / valor_b

# print(soma(1, 2))
# print(soma(3, 4))
# print(subtracao(10, 2))
# print(multiplicacao(10, 2))
# print(divisao(10, 2))

calculadora = Calculadora()
#print(calculadora.valor_a)
print(calculadora.soma(10,2))
print(calculadora.subtracao(5,3))
print(calculadora.divisao(100,5))
print(calculadora.multiplicacao(500,3))