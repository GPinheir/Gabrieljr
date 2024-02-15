import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    # Verifique se o usuário e a senha são válidos (substitua isso por sua lógica de autenticação real)
    if usuario == "gabriel" and senha == "gostoso":
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo, " + usuario + "!")
    else:
        messagebox.showerror("Login falhou", "Usuário ou senha incorretos.")

# Crie a janela principal
janela = tk.Tk()
janela.title("Tela de Login")

# Crie os widgets (rótulos, entradas e botões)
rotulo_usuario = tk.Label(janela, text="Usuário:")
rotulo_senha = tk.Label(janela, text="Senha:")
entrada_usuario = tk.Entry(janela)
entrada_senha = tk.Entry(janela, show="*")  # A opção show="*" exibe asteriscos para senhas

botao_login = tk.Button(janela, text="Login", command=verificar_login)

# Posicione os widgets na janela
rotulo_usuario.grid(row=0, column=0, padx=10, pady=10)
entrada_usuario.grid(row=0, column=1, padx=10, pady=10)
rotulo_senha.grid(row=1, column=0, padx=10, pady=10)
entrada_senha.grid(row=1, column=1, padx=10, pady=10)
botao_login.grid(row=2, column=0, columnspan=2, pady=10)

# Inicie o loop principal da interface gráfica
janela.mainloop()