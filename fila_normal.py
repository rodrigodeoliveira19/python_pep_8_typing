class filanormal:
    codigo: int = 0
    fila = []
    clientesatendidos = []
    senhaatual: str = ""

    def gerar_senha_atual(self)->None:
        self.senhaatual = f"ROD{self.senhaatual}"