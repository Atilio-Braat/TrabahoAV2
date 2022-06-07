import tkinter as tk

window = tk.Tk()

label_nome = tk.Label(window, text='Nome')
label_nome.grid(row=0,column=0, padx=10, pady=10)

label_idade = tk.Label(window, text='Idade')
label_idade.grid(row=1, column=0, padx=10, pady=10)

label_cep = tk.Label(window, text='Telefone')
label_cep.grid(row=2, column=0, padx=10, pady=10)

label_cargo = tk.Label(window, text='Cargo')
label_cargo.grid(row=3, column=0, padx=10, pady=10)

label_admissao = tk.Label(window, text='Admissão')
label_admissao.grid(row=4, column=0 , padx=10, pady=10)


#Caixas Entradas:
entry_nome = tk.Entry(window , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

entry_idade = tk.Entry(window, width =35)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

entry_cep = tk.Entry(window, width =35)
entry_cep.grid(row=2, column=1 , padx=10, pady=10)

entry_cargo = tk.Entry(window, width =35)
entry_cargo.grid(row=3, column=1, padx=10, pady=10)

entry_admissao = tk.Entry(window, width =35)
entry_admissao.grid(row=4, column=1, padx=10, pady=10)


# lista_Funcionarios = ListBox(window)
# lista_Funcionarios.grid(row=0, column=2, rowspan=10)
# scrool_Funcionarios = ScrollBar(window)

# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Funcionário')
botao_cadastrar.grid(row=5, column=0,columnspan=2, pady=5, ipadx = 40)

# Botão de Excluir

botao_descadastrar = tk.Button(text='Descadastrar Funcionário')
botao_descadastrar.grid(row=6, column=0,columnspan=2, pady=5, ipadx = 30)


window.mainloop()