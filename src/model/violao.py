from .instrumento import Instrumento

class Violao(Instrumento):
    def __init__(self, marca, preco, modelo):
        super().__init__(marca, preco)
        self._modelo = modelo

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo
