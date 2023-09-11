import tkinter as tk
import pytube as pt


janela = tk.Tk()

janela.geometry("500x300")
janela.resizable(True, True)

janela.title("Video Downloader - Youtube (by: @valkenrox)")

label = tk.Label(janela, text="Insira o link do vídeo para o Download: ", font=("Arial", 12)).place(x=100, y=60)

link = tk.StringVar()

entrada_link = tk.Entry(janela, width=50, textvariable= link).place(x= 100, y = 100)

def Downloader():
    url = pt.YouTube(str(link.get()))
#      >>> yt.streams
#   ... .filter(progressive=True, file_extension='mp4')
#   ... .order_by('resolution')
#   ... .desc()
#   ... .first()
#   ... .download()
# ```
    video = url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download()

    tk.Label(janela,text = "Download Completo", font=("Arial", 11)).place(x= 150, y= 200)

botao = tk.Button(janela, text="Download", font= ("Arial", 12), width=10, bg="green", padx=2, command=Downloader).place(x= 300, y= 150)

janela.mainloop()
