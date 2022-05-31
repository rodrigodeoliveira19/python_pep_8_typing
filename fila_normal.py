from typing import Dict, Union, List

from constantes import CODIGO_NORMAL
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida
from fila_base import FilaBase

Estatisticas = Union[EstatisticaResumida, EstatisticaDetalhada]

class FilaNormal(FilaBase):

    def gerar_senha_atual(self) -> None:
        self.senhaatual = f"{CODIGO_NORMAL}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'cliente atual: {cliente_atual} dirija-se ao caixa {caixa}'

    def estatistica(self, retorna_estatistica: Estatisticas) -> dict:

        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)
