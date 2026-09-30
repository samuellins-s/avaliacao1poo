from datetime import date

class QuantidadeInvalidaError(Exception):
    '''Quantidade inválida'''

class MedicamentoVencidoError(Exception):
    '''O medicamento é vencido'''

class Medicamento:
    def __init__(self, nome: str, lote: str, validade: date, quantidade: int, valor: float) -> None:
        # validacao quantidade e valor na criacao do objeto
        if quantidade <= 0:
            raise ValueError('Digite uma quantidade maior que zero (0)')

        if valor <= 0:
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
        return self.nome == outro.nome and self.lote == outro.lote

    def __lt__(self, outro: object) -> bool:
        return self.validade < outro.validade

    # methods objeto
    def dispensar(self, quantidade: int) -> None:
        hoje = date.today()

        if quantidade <= 0:
            raise QuantidadeInvalidaError('Digite uma quantidade maior que zero (0)')
    
        elif quantidade > self._quantidade:
            raise QuantidadeInvalidaError('A quantidade escolhida ultrapassou à disponível em estoque')

        elif self.validade > hoje:
            raise MedicamentoVencidoError('A data de validade do lote passou')

        else:
            self._quantidade -= quantidade

    def repor(self, quantidade: int):
        if quantidade <= 0:
            raise QuantidadeInvalidaError('Digite uma quantidade maior que zero (0)')
            
        self._quantidade += quantidade

    # metodo de classe
    @classmethod
    def de_registro(cls, remedio: str) -> object:
        nome,lote,validade,quantidade,valor = remedio.split(";")
        data_string = validade
        date_object = date.fromisoformat(data_string)
        return cls(nome, lote, date_object, int(quantidade), float(valor))


# main program
if __name__ == '__main__':
    m1 = Medicamento("Dipirona 500mg", "L2026A", date(2026, 1, 31), 100, 12.50)
    m2 = Medicamento.de_registro("Amoxicilina 500mg;L2026B;2026-10-15;40;18.90")
    print(m1)
    print(m2)

    m1.dispensar(3)
    print(m1)

    m1.repor(3)
    print(m1)
    print([m1])

    outro = Medicamento("Dipirona 500mg", "L2026A", date(2026, 1, 31), 100, 12.50)
    print(f"m1 é igual a outro? {m1 == outro}")
