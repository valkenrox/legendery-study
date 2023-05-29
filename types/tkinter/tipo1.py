from tkinter import *

janela = Tk()

janela.title("Minha primeira janela!")
janela.geometry('400x200')
# janela.col
lbl = Label(janela,text="Daniel brabao",font=("Arial Bold",20), fg="Green",bg="Black")
lbl.grid(column=50,row=50)


def acao_btn():
    print("Aew galera to testando!")
    lbl_funcao = Label(janela,text="Criei esse texto",font=("Arial Bold",15))
    lbl_funcao.grid(column=120,row=120)
    entrada = Entry(janela)
    entrada.grid(column=0,row=150)
    resultado = entrada.get()
    lbl.configure(text= resultado)
    lbl.grid(column=1,row=0)

    return lbl_funcao



btn = Button(janela,text="Clica aqui",command=acao_btn)
btn.grid(column=100,row=100)



janela.mainloop()