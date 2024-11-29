import tkinter as tk
from tkinter import messagebox
from controller import InstrumentoController

class App:
    def __init__(self, root):
        self.controller = InstrumentoController()
        self.root = root
        self.root.title("Gerenciador de Instrumentos")

        # Formulário
        tk.Label(root, text="Marca").grid(row=0, column=0)
        self.marca_entry = tk.Entry(root)
        self.marca_entry.grid(row=0, column=1)

        tk.Label(root, text="Preço").grid(row=1, column=0)
        self.preco_entry = tk.Entry(root)
        self.preco_entry.grid(row=1, column=1)

        tk.Label(root, text="Modelo").grid(row=2, column=0)
        self.modelo_entry = tk.Entry(root)
        self.modelo_entry.grid(row=2, column=1)

        tk.Label(root, text="Captador (apenas para guitarras)").grid(row=3, column=0)
        self.captador_entry = tk.Entry(root)
        self.captador_entry.grid(row=3, column=1)

        # Botões
        tk.Button(root, text="Adicionar Guitarra", command=self.adicionar_guitarra).grid(row=4, column=0)
        tk.Button(root, text="Adicionar Violão", command=self.adicionar_violao).grid(row=4, column=1)
        tk.Button(root, text="Listar Instrumentos", command=self.listar_instrumentos).grid(row=5, column=0, columnspan=2)

    def adicionar_guitarra(self):
        marca = self.marca_entry.get()
        preco = self.preco_entry.get()
        modelo = self.modelo_entry.get()
        captador = self.captador_entry.get()

        if marca and preco and modelo and captador:
            self.controller.adicionar_guitarra(marca, float(preco), modelo, captador)
            messagebox.showinfo("Sucesso", "Guitarra adicionada com sucesso!")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    def adicionar_violao(self):
        marca = self.marca_entry.get()
        preco = self.preco_entry.get()
        modelo = self.modelo_entry.get()

        if marca and preco and modelo:
            self.controller.adicionar_violao(marca, float(preco), modelo)
            messagebox.showinfo("Sucesso", "Violão adicionado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    def listar_instrumentos(self):
        instrumentos = self.controller.listar_instrumentos()
        lista = "\n".join([f"{i}. {type(instr).__name__} - Marca: {instr.get_marca()}, Preço: {instr.get_preco()}"
                           for i, instr in enumerate(instrumentos)])
        messagebox.showinfo("Lista de Instrumentos", lista if lista else "Nenhum instrumento cadastrado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
