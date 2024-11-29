from model.guitarra import Guitarra
from model.violao import Violao

class InstrumentoController:
    def __init__(self):
        self.instrumentos = []

    def adicionar_guitarra(self, marca, preco, modelo, captador):
        guitarra = Guitarra(marca, preco, modelo, captador)
        self.instrumentos.append(guitarra)

    def adicionar_violao(self, marca, preco, modelo):
        violao = Violao(marca, preco, modelo)
        self.instrumentos.append(violao)

    def listar_instrumentos(self):
        return self.instrumentos

    def remover_instrumento(self, index):
        if 0 <= index < len(self.instrumentos):
            del self.instrumentos[index]
