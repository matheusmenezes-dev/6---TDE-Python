class DocumentoInvalido(Exception):
    pass

class CpfInvalido(Exception):
    def __init__(self, msg="CPF Inválido", *args: object, **kwargs) -> None:
        super().__init__(*args, **kwargs)