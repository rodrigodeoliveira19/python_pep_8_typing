from typing import List, Dict, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: str):
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> Dict:
        estatistica: Dict[str, Union[str, List[str], int]] = {}

        estatistica['dia'] = self.dia
        estatistica['agencia'] = self.agencia
        estatistica['clientes_atendidos'] = clientes_atendidos
        estatistica['qtd_clientes_atendidos'] = (
            len(clientes_atendidos)
        )

        return estatistica