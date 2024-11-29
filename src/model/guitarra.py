from .instrumento import Instrumento

class Guitarra(Instrumento):
    def __init__(self, marca, preco, modelo, captador):
        super().__init__(marca, preco)
        self._modelo = modelo
        self._captador = captador

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_captador(self):
        return self._captador

    def set_captador(self, captador):
        self._captador = captador
