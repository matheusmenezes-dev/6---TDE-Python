from exceptions import CpfInvalido, DocumentoInvalido

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
        # Qualquer exceção nesse bloco indica um cpf inválido
        try:
            cpf = str(self.__cpf)
            # Aqui são feitos os checks de validez
            if len(self.__cpf) != 11: return False
            
            # Verificando se os ultimos digitos concordam
            # com o algoritmo de verificação
            if not self.algoritmo_validação(self.__cpf, -2): return False
            if not self.algoritmo_validação(self.__cpf, -1): return False

            return True
        except:
            return False
    
    # Utilizando o algoritmo explicado em: 
    # https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/
    def algoritmo_validação(self, cpf:str, indice_digito_comparador:int):
            soma = 0
            multiplicador = 12 + indice_digito_comparador
            for digito in cpf[:indice_digito_comparador]:
                soma += int(digito) * multiplicador
                multiplicador -= 1
            resultado = (soma * 10) % 11 
            resultado = resultado if resultado != 10 else 0
            if resultado != int(cpf[indice_digito_comparador]): return False
            return True
        

class Documento:
    def __init__(self, cpf:str=None, cnpj:str=None) -> None:
        self.cpf = self.validar_cpf(cpf)
        self.cnpj = self.validar_cnpj(cnpj)

        if not (self.cnpj or self.cpf):
            raise DocumentoInvalido("Não foi possivel validar um CPF ou CNPJ")
        
    def validar_cpf(self, cpf):
        cpf:CPF = CPF(cpf)
        return cpf if cpf.eh_valido else None
        

class Cadastro:
    def __init__(self, documento:str, telefone:int, cep:int, email:str) -> None:
        self.documento = documento
        self.telefone = telefone
        self.cep = cep
        self.email= email