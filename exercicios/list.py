import tkinter as tk

janela = tk.Tk()
janela.geometry("300x300")
janela.title("Listbox")




f_1 = tk.Frame(janela, width=150, height=100, bg="blue")
f_1.grid(row=0, column=0, padx=5, pady=5)

f_2 = tk.Frame(janela, width=150, height=100, bg="yellow")
f_2.grid(row=0, column=1,padx=5, pady=5)

f_3 = tk.Frame(janela, width=150, height=100, bg="red")
f_3.grid(row=1, column=0,padx=5, pady=5)

f_4 = tk.Frame(janela, width=150, height=100, bg="green")
f_4.grid(row=1, column=1,padx=5, pady=5)



lista = tk.Listbox(f_1, height=3, selectmode="unique")

lista.grid(column=0, row=0,sticky='N')

def teste():
    print(lista.curselection())
    print(lista.get(lista.curselection()))


# Para se excluir elementos de uma Listbox, usa-se os metodos abaixo listados:
# delete (start, last) - exclui linhas no intervalo especificado.
# delete (ANCHOR) -  Excluir elemento selecionado
# delete (2) - Exclua o segundo elemento da posição
# delete (0, END) # Excluir todos os elementos

lista.insert(1, "Python")
lista.insert(2, "C++")
lista.insert(3, "C#")

b = tk.Button(f_2, text="Clique aqui", command=teste)
b.grid(column=0, row=1,sticky='NSWE')

janela.mainloop()