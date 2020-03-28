from tkinter import *

janela = Tk()

janela.title("Teste com criação de Janelas")

# Fazem a mesma função - muda a cor de fundo.
janela["bg"] = "green"
janela["background"] = "green"

# ("Altura x Largura + Distância da esquerda + Distância da direita")
janela.geometry("800x600+50+100")

Label(janela, text="Olá mundo!").pack()

# Ficará em contante atualização da janela.
janela.mainloop()
