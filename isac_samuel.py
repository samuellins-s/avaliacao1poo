from datetime import date

class QuantidadeInvalidaError(Exception):
    '''Quantidade inválida'''

class MedicamentoVencidoError(Exception):
    '''O medicamento é vencido'''

class Medicamento:
    def __init__(self, nome: str, lote: str, validade: date, quantidade: int, valor: float) -> None:
        if self.quantidade < 0:
            raise ValueError('Digite uma quantidade maior que zero (0)')

        if self.valor < 0:
            raise ValueError('Digite uma quantidade maior que zero (0)')

        self.nome = nome
        self.lote = lote
        self.validade = validade
        self.quantidade = quantidade
        self.valor = valor

@property
def quantidade(self):
    return self._quantidade

@quantidade.setter
def quantidade(self, valor):
    if valor < 0:
        raise ValueError('Digite uma quantidade maior que zero (0)')
    self._quantidade = valor

@property
def valor(self):
    return self._valor

@valor.setter
def valor(self, valor):
    if valor < 0:
        raise ValueError('Digite uma quantidade maior que zero (0)')
    self._valor = valor 