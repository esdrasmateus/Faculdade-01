from tkinter import *

lista1 = []
lista2 = []

def bt2_press():
    def close_window():
        janela2.destroy()
    def lista():
        lista1.append(regusuario.get())
        lista2.append(regsenha.get())

    janela2 = Tk()
    regusuario = Entry(janela2)
    regusuario.grid(row = 0, column = 1)

    regusuario_label = Label(janela2, text = "Usuário")
    regusuario_label.grid (row = 0, column = 0)

    regsenha = Entry(janela2)
    regsenha.grid(row = 1, column = 1)

    regsenha_label = Label(janela2, text = "Senha")
    regsenha_label.grid(row = 1, column = 0)

    regbt = Button(janela2, width = 20, text = "Registrar-se", command = close_window)
    regbt.grid(row = 2, column = 1)
    
    regbt2 = Button(janela2, width = 20, text = "Confirma", command = lista)
    regbt2.grid(row = 3, column = 1)
    janela2.geometry("300x100+400+400")

def login():
    if (usuario.get() in lista1 and senha.get() in lista2):
        label_label["text"] = "Login efetuado com sucesso!" 
    else:
        label_label["text"] = "Login mal-sucedido"

janela1 = Tk()

usuario = Entry(janela1)
usuario.grid(row = 0, column = 1)

usuario_label = Label(janela1, text = "Usuário: ")
usuario_label.grid(row = 0, column = 0)

senha = Entry(janela1)
senha.grid(row = 1, column = 1)
senha_label = Label(janela1, text = "Senha: ")
senha_label.grid(row = 1, column = 0)

bt1 = Button(janela1, width = 20, text = "Confirmar", command = login)
bt1.grid(row = 2, column = 1)

bt2 = Button(janela1, width = 20, text = "Registrar um novo usuário", command = bt2_press)
bt2.grid(row = 3, column = 1)

label_label = Label(janela1, text = "Aguardando dados")
label_label.grid(row = 4, column = 1)

janela1.geometry("500x300+100+100")
janela1.mainloop()