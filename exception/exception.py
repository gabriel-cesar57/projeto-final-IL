class ContinuarComMenuException(Exception):
    """Sinaliza ao loop principal que deve apenas continuar"""
    pass

class FecharMenuException(Exception):
    """Sinaliza ao loop principal que deve encerrar o menu"""
    def __init__(self, message: str = "Sair do menu"):
        super().__init__(message)