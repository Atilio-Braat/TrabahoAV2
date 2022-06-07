import tkinter as tk
from funcionario import Funcionario

def cadastrarFuncionario():
    funcionario = Funcionario()
    if entry_nome.get():
        funcionario.nome = entry_nome.get()
    else:
        entry_nome.config(highlightbackground="red")
        return

    if entry_idade.get():
        funcionario.idade = entry_idade.get() 
    else:
        entry_idade.config(highlightbackground="red") 
        return

    if entry_cpf.get():
        funcionario.cpf = entry_cpf.get()
    else:
        entry_cpf.config(highlightbackground="red")
        return

    if entry_cargo.get():
        funcionario.cargo = entry_cargo.get()
    else:
        entry_cargo.config(highlightbackground="red")
        return

    if entry_admissao.get():
        funcionario.entrada = entry_admissao.get()
    else:
        entry_admissao.config(highlightbackground="red")
        return

    funcionario.insertFuncionario()

    apagarCampos()
    

def deletarFuncionario():
    funcionario = Funcionario()

    funcionario.cpf = entry_cpf.get()
    funcionario.deletarFuncionario()

    apagarCampos()

def apagarCampos():
    entry_nome.delete(0, tk.END)
    entry_nome.config(highlightbackground="gray")
    entry_idade.delete(0, tk.END)
    entry_idade.config(highlightbackground="gray")
    entry_cpf.delete(0, tk.END)
    entry_cpf.config(highlightbackground="gray")
    entry_cargo.delete(0, tk.END)
    entry_cargo.config(highlightbackground="gray")
    entry_admissao.delete(0, tk.END)
    entry_admissao.config(highlightbackground="gray")

window = tk.Tk()
window.geometry("750x575")
window.title("Cadastro de Funcionários")


#=======================================================#

label_nome = tk.Label(window, text='Nome')
label_nome.grid(row=0,column=0, padx=10, pady=10)

label_idade = tk.Label(window, text='Idade')
label_idade.grid(row=1, column=0, padx=10, pady=10)

label_cpf = tk.Label(window, text='CPF')
label_cpf.grid(row=2, column=0, padx=10, pady=10)

label_cargo = tk.Label(window, text='Cargo')
label_cargo.grid(row=3, column=0, padx=10, pady=10)

label_admissao = tk.Label(window, text='Admissão')
label_admissao.grid(row=4, column=0 , padx=10, pady=10)

#=======================================================#

scroll_funcionarios = tk.Scrollbar(window)

lista_funcionarios = tk.Listbox(window, relief=tk.SOLID, border=1, width=30, height=25, font=("Gentium Basic", 11))
lista_funcionarios.grid(row=0, column=6, rowspan=10, padx=5, pady=15, ipadx=40)

#=======================================================#

entry_nome = tk.Entry(window , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

entry_idade = tk.Entry(window, width =35)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

entry_cpf = tk.Entry(window, width =35)
entry_cpf.grid(row=2, column=1 , padx=10, pady=10)

entry_cargo = tk.Entry(window, width =35)
entry_cargo.grid(row=3, column=1, padx=10, pady=10)

entry_admissao = tk.Entry(window, width =35)
entry_admissao.grid(row=4, column=1, padx=10, pady=10)

# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Funcionário', command=cadastrarFuncionario)
botao_cadastrar.grid(row=5, column=0,columnspan=2, pady=5, ipadx = 40)

# Botão de Excluir

botao_descadastrar = tk.Button(text='Descadastrar Funcionário (preencher somente o campo de cpf)', command=deletarFuncionario)
botao_descadastrar.grid(row=6, column=0,columnspan=2, pady=5, ipadx = 30)

#=======================================================#

for i in range (100):
    lista_funcionarios.insert(tk.END, i)
    
lista_funcionarios.config(yscrollcommand=scroll_funcionarios.set)
scroll_funcionarios.config(command=lista_funcionarios.yview)


window.mainloop()