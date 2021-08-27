import unittest
from main import Cliente, Loja

class TestaEmprestimoBikes(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente(2, 1, 12)
        self.loja = Loja(100)


if __name__ == "__main__":
    unittest.main()