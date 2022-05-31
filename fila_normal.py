from typing import Dict, Union, List

from constantes import CODIGO_NORMAL
from fila_base import FilaBase


class FilaNormal(FilaBase):

    def gerar_senha_atual(self) -> None:
        self.senhaatual = f"{CODIGO_NORMAL}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'cliente atual: {cliente_atual} dirija-se ao caixa {caixa}'

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        estatistica: Dict[str, Union[str, List[str], int]] = {}
        if flag != "detail":
            estatistica[f'{agencia}-{dia}'] =  len(self.clientes_atendidos)
        else:
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atendidos'] = self.clientes_atendidos
            estatistica['qtd_clientes_atendidos'] = (
                len(self.clientes_atendidos)
            )

        return estatistica
