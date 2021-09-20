#Modulos
import abc
from logging import raiseExceptions
from unittest import TestCase,main


#Classe calculadora
class Calculadora(object):
    def calcular(self,valor1,valor2,operador):
        operacao = OperacaoFabrica().criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(valor1,valor2)
            return resultado

class OperacaoFabrica(object):
    def criar(self, operador):
        if (operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()
        elif (operador == 'multiplicacao'):
            return Multiplicacao()
        elif (operador == 'potenciacao'):
            return Potenciacao()
        elif (operador == 'resto'):
            return Resto()

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self,valor1,valor2):
        pass

#Classes operações
class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado
class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado
class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado
class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado    
class Resto(Operacao):
    def executar(self,valor1,valor2):
        resultado = valor1%valor2
        return resultado
class Potenciacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 ** valor2
        return resultado


#Teste básicos
class Testes(TestCase):
    def test_soma(self):
        calculo_soma = Calculadora()
        result = calculo_soma.calcular(10,10,'soma')
        self.assertEqual(result,20)
        
    def test_multiplicacao(self):
        calculo_multiplicacao = Calculadora()
        result = calculo_multiplicacao.calcular(10,2,'multiplicacao')
        self.assertEqual(result,20)

    def test_divisao(self):
        calculo_divisao = Calculadora()
        result = calculo_divisao.calcular(20,2,'divisao')
        self.assertEqual(result,10)

    def test_subtracao(self):
        calculo_subtracao = Calculadora()
        result = calculo_subtracao.calcular(20,5,'subtracao')
        self.assertEqual(result, 15)

    def test_potenciacao(self):
        calculo_potencia = Calculadora()
        result = calculo_potencia.calcular(4,4,'potenciacao')
        self.assertEqual(result,256)
    def test_resto(self):
        calculo_resto= Calculadora()
        result= calculo_resto.calcular(99,2,'resto')
        self.assertEqual(result,1)


visor = """"CALCULADORA
Operações:\n
    Soma            +
    Subtracao       -
    Multiplicacao   x
    Divisao         /
    Potenciacao     n²
    Resto           %\n"""


def codigo():
    operacoes=['soma','subtracao','multiplicacao','divisao','potenciacao','resto']
    operacao=input("Digite o nome da operação, sem acento:\n").lower()
    if operacao not in operacoes:
        print("Operação não reconhecida")
        codigo()
    valor1=float(input("Digite o primeiro valor:\n"))
    valor2=float(input("Digite o segundo valor:\n"))
    resultado = Calculadora().calcular(valor1,valor2,operacao)
    print ("Resultado = {0:g}".format(float(resultado)))


print(visor)
codigo()
main()