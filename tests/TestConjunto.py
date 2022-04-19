import unittest
from src.logical.Conjunto import Conjunto

class TestConjunto (unittest.TestCase):
    def test_conjunto_vacio_retornaNonne(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())
