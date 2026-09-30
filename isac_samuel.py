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
    def quantidade(self) -> int:
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor: int) -> None:
        if valor <= 0:
            raise ValueError('Digite uma quantidade maior que zero (0)')
        self._quantidade = valor

    # getters e setters atrib valor
    @property
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError('Digite um valor maior que zero (0)')
        self._valor = valor

    # dunder methods
    def __str__(self) -> str:
        return f'Medicamento: {self.nome}\nLote: {self.lote}\nQuantidade: {self._quantidade}\nValidade {self.validade}\n'

    def __repr__(self) -> str:
        return f'Medicamento: ({self.nome})\nLote: ({self.lote})\nQuantidade: ({self._quantidade})\nValidade ({self.validade})\n'

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

    def repor(self, quantidade: int) -> None:
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

    # staticmethod
    @staticmethod
    def dias_para_vencer(date: object) -> int:
        date_hoje = date.today()

        quantidade_dias_vencer = date - date_hoje

        return quantidade_dias_vencer.days


# teste no main program
if __name__ == '__main__':

    print('LEIA OS COMENTÁRIOS, PROFESSOR\n')
    m1 = Medicamento("Dipirona 500mg", "L2026A", date(2026, 12, 31), 100, 12.50)
    m2 = Medicamento.de_registro("Amoxicilina 500mg;L2026B;2026-10-15;40;18.90")

    print(f"Dados de m1: {m1}") # ex.: Dipirona 500mg (L2026A) - 100 un. - val. 31/12/2026
    print(f"Dados de m2: {m2}") # ex.: Amoxicilina 500mg (L2026B) - 40 un. - val. 15/10/2026
    print(f"Dias para vencer de m2: {Medicamento.dias_para_vencer(m2.validade)}")
    print("Dispensando 20 medicamentos de m1")

    try:
        m1.dispensar(20)
        print(f"Quantidade de m1: {m1.quantidade}")
    except MedicamentoVencidoError as error:
        print(error)
    try:
        m2.dispensar(999)
    except QuantidadeInvalidaError as erro:
        print(f"Erro esperado: {erro}")

    vencido = Medicamento("Soro Fisiológico", "L2025X", date(2025, 1, 10), 10, 5.0)

    try:
        vencido.dispensar(1)
    except MedicamentoVencidoError as erro:
        print(f"Erro esperado: {erro}")

    try:
        # ATENCAO   
        # como o atributo quantidade é zero na criação do objeto, lançara a exceceçao ValueError e pulará todo o try except
        # quando o atributo quantidade é maior que zero, fará o __eq__ e __lt__ dentro do bloco do try except

        outro = Medicamento("Dipirona 500mg", "L2026A", date(2026, 1, 1), 0, 1.0)
        print(f"m1 é igual a outro? {m1 == outro}")

        estoque = [m1, m2, vencido, outro]
        print("Exibindo lista ordenada por data (mais antigos primeiro): ")
        for lote in sorted(estoque):
            print(lote)

    except ValueError as erro:
        print(f"Erro esperado: {erro}")
    
    try:
        m1.quantidade = -5
    except ValueError as erro:
        print(f"Erro esperado: {erro}")