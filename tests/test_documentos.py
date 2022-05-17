import unittest
from documentos import CNPJ, CPF

class TestCpf(unittest.TestCase):
    def test_validar_cpf_valido(self):
        cpf = CPF("49768353830")
        self.assertTrue(cpf.eh_valido)

    def test_algoritmo_validador(self):
        cpf = CPF("49768353830")
        self.assertTrue(cpf.algoritmo_validação("49768353830"))
        

class TestCnpj(unittest.TestCase):
    def test_algoritmo_validador(self):
        cnpj = CNPJ("11222333000181")
        self.assertTrue(cnpj.algoritmo_validação("11222333000181"))
        
