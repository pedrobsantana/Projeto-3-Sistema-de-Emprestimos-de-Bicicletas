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

    # não consegui fazer um teste para a função locacaoHora
    #def testeLocacaoHora(self):
    #    print("\nTeste de LOJA - Locação Hora")
    #    self.assertEqual(self.loja.locacaoHora,(datetime))

if __name__ == "__main__":
    unittest.main()