import abc

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senhaatual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo > TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def inserir_cliente(self):
        self.fila.append(self.senhaatual)

    @abc.abstractmethod
    def gerar_senha_atual(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self):
        ...

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gerar_senha_atual()
        self.inserir_cliente()
#
