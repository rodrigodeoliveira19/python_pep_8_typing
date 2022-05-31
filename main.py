from fila_normal import FilaNormal
from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

# fila_teste = FilaNormal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(6))
# print(fila_teste.estatistica("27/05/2022", 1044, "detail"))


fila_teste2 = FabricaFila.pega_fila("NORMAL")
fila_teste2.atualiza_fila()
print(fila_teste2.chama_cliente(10))
print(fila_teste2.estatistica(EstatisticaDetalhada("27/05/2022", 1044)))