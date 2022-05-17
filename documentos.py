from exceptions import CepInvalido, CnpjInvalido, CpfInvalido, DocumentoInvalido
import httpx

class CPF:
    def __init__(self, cpf:str) -> None:
        self.__cpf = cpf
    
    @property
    def eh_valido(self):
        return self.validar_cpf()
    
    @property
    def cpf(self):
        if self.eh_valido:
            return f"{self.__cpf[0:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}.{self.__cpf[9:11]}"
        else:
            raise CpfInvalido()
    
    def validar_cpf(self):
        cpf = str(self.__cpf)
        # Aqui são feitos os checks de validez
        if len(cpf) != 11: return False
        if not self.algoritmo_validação(cpf): return False
        return True
    
    # Utilizando o algoritmo explicado em: 
    # https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/
    def algoritmo_validação(self, cpf:str):
        for indice_digito_comparador in [-2, -1]:
            soma = 0
            multiplicador = 12 + indice_digito_comparador
            for digito in cpf[:indice_digito_comparador]:
                soma += int(digito) * multiplicador
                multiplicador -= 1
            resultado = (soma * 10) % 11 
            resultado = resultado if resultado != 10 else 0
            if resultado != int(cpf[indice_digito_comparador]): return False
            return True
        
class CNPJ:
    def __init__(self, cnpj:str) -> None:
        self.__cnpj = cnpj

    @property
    def eh_valido(self):
        cnpj = str(self.__cnpj)
        # Aqui vão os checks de validação
        if len(cnpj) != 14: return False
        if not self.algoritmo_validação(cnpj): return False
        return True

    @property
    def cnpj(self):
        if self.eh_valido: return self.__cnpj
        raise CnpjInvalido()    

    def algoritmo_validação(self, cnpj:str):
        # Aplicação do algoritmo explicado em:
        # https://www.macoratti.net/alg_cnpj.htm
        
        cnpj = str(cnpj)        
        for digito_verificador in [-2, -1]:
            multiplicadores =  [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            digitos = cnpj[:digito_verificador]
            soma = sum([multiplicadores[i + (-1 + (digito_verificador * -1))] * int(digitos[i]) for i in range(len(digitos))])
            resultado = soma % 11
            resultado = 11 - resultado if resultado > 2 else 0
            if resultado != int(cnpj[digito_verificador]): return False
        return True

class CEP:
    def __init__(self, cep:str) -> None:
        self.__cep = str(cep)
        self.__cep.replace('.', '').replace('-', '').replace(' ', '-')
        response = httpx.get(f"https://viacep.com.br/ws/{self.__cep}/json/")
        self.__eh_valido = False
        if response.status_code == 200 and not "erro" in response.json():
            self.__eh_valido = True
        if self.__eh_valido:
            dados = response.json()
            self.__formatado = dados["cep"] 
            self.__logradouro = dados["logradouro"]
            self.__complemento = dados["complemento"]
            self.__bairro = dados["bairro"]
            self.__localidade = dados["localidade"]
            self.__uf = dados["uf"]
            self.__ibge = dados["ibge"]
            self.__gia = dados["gia"]
            self.__ddd = dados["ddd"]
            self.__siafi = dados["siafi"]

    @property
    def cep(self):
        if self.eh_valido: return self.__formatado 
        raise CepInvalido()

    @property
    def logradouro(self):
        if self.eh_valido: return self.__logradouro 
        raise CepInvalido()

    @property
    def complemento(self):
        if self.eh_valido: return self.__complemento 
        raise CepInvalido()

    @property
    def bairro(self):
        if self.eh_valido: return self.__bairro 
        raise CepInvalido()

    @property
    def localidade(self):
        if self.eh_valido: return self.__localidade 
        raise CepInvalido()

    @property
    def uf(self):
        if self.eh_valido: return self.__uf 
        raise CepInvalido()

    @property
    def ibge(self):
        if self.eh_valido: return self.__ibge 
        raise CepInvalido()

    @property
    def gia(self):
        if self.eh_valido: return self.__gia 
        raise CepInvalido()

    @property
    def ddd(self):
        if self.eh_valido: return self.__ddd 
        raise CepInvalido()

    @property
    def siafi(self):
        if self.eh_valido: return self.__siafi 
        raise CepInvalido()

    @property
    def eh_valido(self):
        return self.__eh_valido
    

class Documento:
    def __init__(self, documento:str) -> None:
        documento = str(documento)
        # Removendo possiveis caracteres que invalidariam as validaçõoes
        documento.replace('.', '').replace('-', '').replace(' ', '')
        cpf = CPF(documento)
        if cpf.eh_valido: return cpf
        cnpj = CNPJ(documento)
        if cnpj.eh_valido: return cnpj
        raise DocumentoInvalido("Não foi possivel validar um CPF ou CNPJ")
        

class Cadastro:
    def __init__(self, documento:str, telefone:int, cep:int, email:str) -> None:
        self.documento = documento
        self.telefone = telefone
        self.cep = cep
        self.email= email