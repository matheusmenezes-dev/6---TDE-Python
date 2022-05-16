import unittest
from documentos import CPF

class TestCpf(unittest.TestCase):
    def test_validar_cpf_valido(self):
        cpf = CPF("49768353830")
        self.assertTrue(cpf.eh_valido)
        self.assertEqual(cpf.cpf, "497.683.538.30")

    def test_algoritmo_validador(self):
        cpf = CPF("49768353830")
        self.assertTrue(cpf.algoritmo_validação("49768353830", -2))
        self.assertTrue(cpf.algoritmo_validação("49768353830", -1))
        
