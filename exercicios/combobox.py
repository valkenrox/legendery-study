import tkinter as tk
import tkinter.ttk as ttk


janela = tk.Tk()
combo = ttk.Combobox(janela)

janela.title("Meu primeiro combo box")

janela.geometry("300x300")

combo['values'] = (1, 2, 3, 4, 5, "Texto 1", "Texto 2", "Texto 3")


combo.current(0)

combo.grid(column=0, row=0)
resultado = combo.get()


estado = tk.BooleanVar()
estado.set(True)

estado2 = tk.StringVar()
estado2.set("Aew")
def evento():
    
    return print("Estado: ", estado.get())

def evento2():
    return print("Estado: ", estado2.get())




check = tk.Checkbutton(janela, text="Checkbutton",variable=estado, onvalue=1, offvalue=0, command=evento)

check1 = tk.Checkbutton(janela, text="Checkbutton",variable=estado2, onvalue="Aew", offvalue="Nao aew", command=evento2)


check.grid(column=0, row=1)
check1.grid(column=0, row=2)



janela.mainloop()

# print(resultado)

