import tkinter as tk

janela = tk.Tk()

janela.title("Exercício 5")

janela.geometry("300x300")

label = tk.Label(janela, text="Escrevendo algo legal para ganhar ponto")
label.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Clique para me dar um ponto")
botao.pack()
resultado = entrada.get()
lbl = tk.Label(janela,text=resultado)
lbl.configure(text= resultado)
lbl.pack()

check = tk.Checkbutton(janela, text="Clique para me dar outro ponto")
check.pack()

caixa = tk.Listbox(janela)
caixa.insert(1, "Clique para me dar mais um ponto")
caixa.pack()


frame = tk.Frame(janela, borderwidth=2,width=50,height=80)
frame.pack()


janela.mainloop()