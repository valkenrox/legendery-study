# import tkinter as tk

# root = tk.Tk()
# root.title("Lista de Componentes")

# # Label
# lbl = tk.Label(root, text="Label")
# lbl.pack()

# # Entry
# entry = tk.Entry(root)
# entry.pack()

# # Button
# btn = tk.Button(root, text="Button")
# btn.pack()

# # Checkbox
# checkbox = tk.Checkbutton(root, text="Checkbox")
# checkbox.pack()

# # Listbox
# listbox = tk.Listbox(root)
# listbox.pack()

# # Frame
# frame = tk.Frame(root, width=200, height=200, bg="gray")
# frame.pack()

# root.mainloop()
import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1")
label1.place(x=50, y=50)

label2 = tk.Label(root, text="Label 2")
label2.place(x=100, y=100)

button = tk.Button(root, text="Button")
button.place(x=150, y=150)

root.mainloop()