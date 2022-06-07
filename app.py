from tkinter import *

window = Tk()
window.geometry("750x575")
window.title("Cadastro de Funcionários")


#=======================================================#

label_nome = Label(window, text='Nome')
label_nome.grid(row=0,column=0, padx=10, pady=10)

label_idade = Label(window, text='Idade')
label_idade.grid(row=1, column=0, padx=10, pady=10)

label_cpf = Label(window, text='CPF')
label_cpf.grid(row=2, column=0, padx=10, pady=10)

label_cargo = Label(window, text='Cargo')
label_cargo.grid(row=3, column=0, padx=10, pady=10)

label_admissao = Label(window, text='Admissão')
label_admissao.grid(row=4, column=0 , padx=10, pady=10)

#=======================================================#

scroll_funcionarios = Scrollbar(window)

lista_funcionarios = Listbox(window, relief=SOLID, border=1, width=30, height=25, font=("Gentium Basic", 11))
lista_funcionarios.grid(row=0, column=6, rowspan=10, padx=5, pady=15, ipadx=40)

#=======================================================#

entry_nome = Entry(window , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

entry_idade = Entry(window, width =35)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

entry_cpf = Entry(window, width =35)
entry_cpf.grid(row=2, column=1 , padx=10, pady=10)

entry_cargo = Entry(window, width =35)
entry_cargo.grid(row=3, column=1, padx=10, pady=10)

entry_admissao = Entry(window, width =35)
entry_admissao.grid(row=4, column=1, padx=10, pady=10)

#=======================================================#

botao_cadastrar = Button(text='Cadastrar Funcionário')
botao_cadastrar.grid(row=5, column=0,columnspan=2, pady=5, ipadx = 40)

botao_descadastrar = Button(text='Descadastrar Funcionário')
botao_descadastrar.grid(row=6, column=0,columnspan=2, pady=5, ipadx = 30)

#=======================================================#

for i in range (100):
    lista_funcionarios.insert(END, i)
    
lista_funcionarios.config(yscrollcommand=scroll_funcionarios.set)
scroll_funcionarios.config(command=lista_funcionarios.yview)


window.mainloop()