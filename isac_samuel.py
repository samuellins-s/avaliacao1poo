from datetime import date

class QuantidadeInvalidaError(Exception):
    '''Quantidade inválida'''

class MedicamentoVencidoError(Exception):
    '''O medicamento é vencido'''

class Medicamento:
    def __init__(self, nome: str, lote: str, validade: date, quantidade: int, valor: float) -> None:
        # validacao quantidade e valor na criacao do objeto
        if self.quantidade <= 0:
            raise ValueError('Digite uma quantidade maior que zero (0)')

        if self.valor <= 0:
            raise ValueError('Digite um valor maior que zero (0)')

        # atributos do objeto
        self.nome = nome
        self.lote = lote
        self.validade = validade
        self._quantidade = quantidade
        self._valor = valor

    # getters e setters atrib quantidade
    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor <= 0:
            raise ValueError('Digite uma quantidade maior que zero (0)')
        self._quantidade = valor

    # getters e setters atrib valor
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor <= 0:
            raise ValueError('Digite um valor maior que zero (0)')
        self._valor = valor

    # dunder methods
    def __str__(self) -> str:
        return f'Medicamento: {self.nome}\nLote: {self.lote}\nQuantidade: {self._quantidade}\n Validade {self.validade}'

    def __repr__(self) -> str:
        return f'Medicamento: ({self.nome})\nLote: ({self.lote})\nQuantidade: ({self._quantidade})\n Validade ({self.validade})'

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Medicamento):
            return NotImplemented
        self.nome == outro.nome and self.lote == outro.lote

    def __lt__(self, outro: object) -> bool:
        return self.validade < outro.validade

    # methods objeto
    def dispensar(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise QuantidadeInvalidaError('Digite uma quantidade maior que zero (0)')
    
        elif quantidade > self._quantidade:
            raise QuantidadeInvalidaError('A quantidade escolhida ultrapassou à disponível em estoque')

        elif ...: # se a data de validade do lote já tiver passado (comparando com date.today());
            raise MedicamentoVencidoError('A data de validade do lote passou')

        else:
            self._quantidade -= valor

    def repor(self, quantidade: int):
        ...