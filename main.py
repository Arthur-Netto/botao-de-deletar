import tkinter as tk
from tkinter import messagebox
import os

# Caminho do arquivo que você quer deletar
file_path = "caminho/do/seu/arquivo.txt"

# Função chamada quando o botão for clicado
def on_button_click():
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            messagebox.showinfo("Sucesso", f"Arquivo {file_path} deletado com sucesso!")
        else:
            messagebox.showwarning("Aviso", f"O arquivo {file_path} não existe.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao deletar o arquivo: {str(e)}")

# Criação da janela principal
root = tk.Tk()
root.title("Deletar Arquivo")


button = tk.Button(root, text="Deletar Arquivo", command=on_button_click)
button.pack(pady=20)

root.mainloop()
