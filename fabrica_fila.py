from typing import Union
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from fila_normal import FilaNormal

class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila: str) -> Union[FilaNormal]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaNormal()
        else:
            NotImplementedError("Tipo de fila não existe")