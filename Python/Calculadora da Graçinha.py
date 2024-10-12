import customtkinter as ctk
from customtkinter import CTkCanvas, CTkLabel, CTkEntry, CTkButton, CTkToplevel

def btn():
    tela.destroy()

def calcular():
    n1 = float(input1.get())
    n2 = float(input2.get())
    result = n1 + n2
    print(f'Essa é a soma: {result}')
    result1.configure(text=f'Resultado: {result}')

tela = ctk.CTk()
tela.title('Vossa tela')
tela.geometry('1000x800')
tela.resizable(False, False)

texto = ctk.CTkLabel(tela, text='Calculadora da Graçinha', font=('enter', 40))
texto.pack()

input1 = ctk.CTkEntry(tela)
input1.pack()

input2 = ctk.CTkEntry(tela)
input2.pack()

butao2 = ctk.CTkButton(tela, text='Calcular', command=calcular)
butao2.pack()

result1 = ctk.CTkLabel(tela, text='Resultado: ')
result1.pack()

butao = ctk.CTkButton(tela, text='Fechar', command=btn)
butao.pack()

tela.mainloop()#Final do Codigo