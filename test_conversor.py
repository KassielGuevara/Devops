import unittest
from conversor import real_para_dolar, real_para_euro, mostrar_historico, historico

class TestConversor(unittest.TestCase):

    def setUp(self):
        # Limpa histórico antes de cada teste
        historico.clear()

    def test_real_para_dolar(self):
        resultado = real_para_dolar(10)
        self.assertEqual(resultado, 2)

    def test_real_para_euro(self):
        resultado = real_para_euro(12)
        self.assertEqual(resultado, 2)

    def test_historico_registrado_dolar(self):
        real_para_dolar(10)
        self.assertEqual(len(historico), 1)

    def test_historico_registrado_euro(self):
        real_para_euro(12)
        self.assertEqual(len(historico), 1)

    def test_mostrar_historico(self):
        real_para_dolar(10)
        h = mostrar_historico()
        self.assertIsInstance(h, list)

    def test_multiplas_conversoes(self):
        real_para_dolar(10)
        real_para_euro(12)
        self.assertEqual(len(historico), 2)


if __name__ == "__main__":
    unittest.main()