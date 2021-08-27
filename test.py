import unittest
import datetime
import principal
from classes import Loja, Cliente

class TestaEmprestimoBikes(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente(2, 1, 12)
        self.loja = Loja(100)

    def testeMostraEstoque(self):
        print("\nTeste de LOJA - Mostrar Estoque")
        self.assertEqual(self.loja.mostrarEstoque())


if __name__ == "__main__":
    unittest.main()