import unittest
from documentos import CEP, CNPJ, CPF

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

    def test_validar_cnpj_valido(self):
        cnpj = CNPJ("11222333000181")
        self.assertTrue(cnpj.eh_valido)

class TestCep(unittest.TestCase):
    def setUp(self) -> None:
        self.cep = CEP("13208-050")
        self.target_endereço = {
            'cep': '13208-050', 'logradouro': 'Avenida Comandante Videlmo Munhoz',
            'complemento': '',
            'bairro': 'Anhangabaú', 'localidade': 'Jundiaí',
            'uf': 'SP', 'ibge': '3525904', 'gia': '4078', 'ddd': '11', 'siafi': '6619'
        }

    def test_validar_cep_valido(self):
        self.assertTrue(self.cep.eh_valido)
    
    def test_validar_cep_invalido(self):
        cep = CEP("12345678")
        self.assertFalse(cep.eh_valido)
        cep = CEP("678")
        self.assertFalse(cep.eh_valido)
    
    def test_cep_formatado(self):
        self.assertEqual(self.cep.cep, self.target_endereço["cep"])
            
    def test_logradouro(self):
        self.assertEqual(self.cep.logradouro, self.target_endereço["logradouro"])

    def test_complemento(self):
        self.assertEqual(self.cep.complemento, self.target_endereço["complemento"])

    def test_bairro(self):
        self.assertEqual(self.cep.bairro, self.target_endereço["bairro"])

    def test_localidade(self):
        self.assertEqual(self.cep.localidade, self.target_endereço["localidade"])

    def test_uf(self):
        self.assertEqual(self.cep.uf, self.target_endereço["uf"])

    def test_ibge(self):
        self.assertEqual(self.cep.ibge, self.target_endereço["ibge"])

    def test_gia(self):
        self.assertEqual(self.cep.gia, self.target_endereço["gia"])

    def test_siafi(self):
        self.assertEqual(self.cep.siafi, self.target_endereço["siafi"])
