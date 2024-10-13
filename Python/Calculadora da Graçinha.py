import customtkinter as ctk
from customtkinter import CTkCanvas, CTkLabel, CTkEntry, CTkButton, CTkToplevel

def btn():
    tela.destroy()

def calcular():
    n1 = float(input1.get())
    n2 = float(input2.get())
    result = n1 + n2
    result1.configure(text=f'Resultado da Soma: {result}')
    #Multiplicação da calculadora (adicionei essa graça aí)
    n1 = float(input1.get())
    n2 = float(input2.get())
    multi = n1 * n2
    result2.configure(text=f'Resultado da Multiplicação: {multi}')
    #Divisão
    n1 = float(input1.get())
    n2 = float(input2.get())
    divisao = n1 / n2
    result3.configure(text=f'Resutlado da Divisão: {divisao}')
    
    
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

result1 = ctk.CTkLabel(tela, text='Resultado da Soma: ')
result1.pack()

result2 = ctk.CTkLabel(tela, text='Resultado da Multiplicação: ')
result2.pack()

result3 = ctk.CTkLabel(tela, text='Resulta da Divisão: ')
result3.pack()

butao = ctk.CTkButton(tela, text='Fechar', command=btn)
butao.pack()

tela.mainloop()#Final do Codigo