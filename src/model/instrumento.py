class Instrumento:
    def __init__(self, marca, preco):
        self._marca = marca
        self._preco = preco

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_preco(self):
        return self._preco

    def set_preco(self, preco):
        self._preco = preco
