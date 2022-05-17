class DocumentoInvalido(Exception):
    pass

class CpfInvalido(Exception):
    def __init__(self, msg="CPF Inválido", *args: object, **kwargs) -> None:
        super().__init__(*args, **kwargs)

class CnpjInvalido(Exception):
    def __init__(self, msg="CNPJ Inválido", *args: object, **kwargs) -> None:
        super().__init__(*args, **kwargs)

class CepInvalido(Exception):
    def __init__(self, msg="CEP Inválido", *args: object, **kwargs) -> None:
        super().__init__(*args, **kwargs)