import unittest

from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calc= Calculadora()

    def test_soma(self):
        self.assertEqual(self.calc.soma(10, 20), 30)
    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(20, 10), 10)
    def test_multiplicacao(self):
        self.self.assertEqual(self.calc.multiplicacao(20, 10), 10)
    def test_divisao(self):
        self.assertEqual(self.calc.divisao(20, 10), 10)
    
    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divisao(10,0)
if __name__ == '__main__':
    unittest.main()
