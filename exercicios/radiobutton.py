import tkinter as tk

janela = tk.Tk()

janela.title("Meu primeiro radio button")
janela.geometry("300x300")

radio = tk.Radiobutton(janela, text="Radio 1", value=1)

radio2 = tk.Radiobutton(janela, text="Radio 2", value=2)

radio3 = tk.Radiobutton(janela, text="Radio 3", value=3)

radio.grid(column=0, row=0,padx=10, pady=10)
radio2.grid(column=0, row=1,padx=20, pady=20)
radio3.grid(column=0, row=2,padx=30, pady=30)
# radio.grid(column=0, row=0,padx=10, pady=10)

janela.mainloop()
