import unittest
import datetime
import main
from classes import Loja, Cliente

class TestaEmprestimoBikes(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente(0, 0, 0)
        self.loja = Loja(100)

    def testeMostraEstoque(self):
        print("\nTeste de LOJA - Mostrar Estoque")
        self.assertEqual(self.loja.mostrarEstoque(), 100)

    def testeLocacaoHora_0bikes(self):
        print("\nTeste de LOJA - Locação HORA 0 Bikes")
        self.assertEqual(self.loja.locacaoHora(0, True), None)

    def testeLocacaoHora_1bike(self):
        print("\nTeste de LOJA - Locação HORA 1 Bike")
        self.assertEqual(self.loja.locacaoHora(2, True), datetime.datetime.now())
    
    def testeLocacaoHora_bikenegativa(self):
        print("\nTeste de LOJA - Locação HORA Bike Negativa")
        self.assertEqual(self.loja.locacaoHora(-1, True), None)
    
    def testeLocacaoHora_estouraestoque(self):
        print("\nTeste de LOJA - Locação HORA Excedendo o Estoque")
        self.assertEqual(self.loja.locacaoHora(105, True), None)

    def testeLocacaoDia_0bikes(self):
        print("\nTeste de LOJA - Locação DIA 0 Bikes")
        self.assertEqual(self.loja.locacaoDia(0, True), None)

    def testeLocacaoDia_1bike(self):
        print("\nTeste de LOJA - Locação DIA 1 Bike")
        self.assertEqual(self.loja.locacaoDia(2, True), datetime.datetime.now())
    
    def testeLocacaoDia_bikenegativa(self):
        print("\nTeste de LOJA - Locação DIA Bike Negativa")
        self.assertEqual(self.loja.locacaoDia(-1, True), None)
    
    def testeLocacaoDia_estouraestoque(self):
        print("\nTeste de LOJA - Locação DIA Excedendo o Estoque")
        self.assertEqual(self.loja.locacaoDia(105, True), None)

    def testeLocacaoSemana_0bikes(self):
        print("\nTeste de LOJA - Locação SEMANA 0 Bikes")
        self.assertEqual(self.loja.locacaoSemana(0, True), None)

    def testeLocacaoSemana_1bike(self):
        print("\nTeste de LOJA - Locação SEMANA 1 Bike")
        self.assertEqual(self.loja.locacaoSemana(2, True), datetime.datetime.now())
    
    def testeLocacaoSemana_bikenegativa(self):
        print("\nTeste de LOJA - Locação SEMANA Bike Negativa")
        self.assertEqual(self.loja.locacaoSemana(-1, True), None)
    
    def testeLocacaoSemana_estouraestoque(self):
        print("\nTeste de LOJA - Locação SEMANA Excedendo o Estoque")
        self.assertEqual(self.loja.locacaoSemana(105, True), None)

    def testeLocacaoFamilia1(self):
        print("teste locação familia com apenas 1 bike")
        self.assertAlmostEqual(self.loja.locacaoFamilia(1, True), False)

    def testeLocacaoFamiliaCenarioIdeal(self):
        print("teste locação familia com cenário ideal")
        self.assertAlmostEqual(self.loja.locacaoFamilia(3, True), True)

    def testeLocacaoFamilia6(self):
        print("teste locação familia com 6 bikes")
        self.assertAlmostEqual(self.loja.locacaoFamilia(6, True), False)

    #def testeCalcularConta(self):
    #    print("\nTeste de LOJA - Calcular Conta")
    #    self.assertEqual(self.loja.calcularConta(2, True))

if __name__ == "__main__":
    unittest.main()