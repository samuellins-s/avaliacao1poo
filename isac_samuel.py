class QuantidadeInvalidaError(Exception):
    '''Quantidade inválida'''

class MedicamentoVencidoError(Exception):
    '''O medicamento é vencido'''

class Medicamento:
    def __init__(self, nome: str, lote: str, validade: date, quantidade: int, valor: float) -> None:
        self.nome = nome
        self.lote = lote
        self.validade = validade
        self.quantidade = quantidade
        self.valor = valor
    