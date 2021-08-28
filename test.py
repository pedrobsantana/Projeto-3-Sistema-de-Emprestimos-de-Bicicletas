import unittest
import datetime
import main
from classes import Loja, Cliente

class TestaEmprestimoBikes(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente(2, 1, 12)
        self.loja = Loja(100)

    def testeMostraEstoque(self):
        print("\nTeste de LOJA - Mostrar Estoque")
        self.assertEqual(self.loja.mostrarEstoque(), None)

    def testeLocacaoHora(self):
        print("\nTeste de LOJA - Locação Hora")
        self.assertEqual(self.loja.locacaoHora,(10, 13))

if __name__ == "__main__":
    unittest.main()