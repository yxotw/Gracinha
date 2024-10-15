#Importações padrão wlayres
import tkinter as tk
from tkinter import Frame, PhotoImage, messagebox, ttk
import mysql.connector
from mysql.connector import Error
import customtkinter as ctk
from customtkinter import CTkCanvas, CTkLabel, CTkEntry, CTkButton, CTkToplevel
from customtkinter import *
from PIL import ImageTk, Image
import pyglet
import webbrowser

    
def fechar_tela():
    tela.destroy()

def calcular():
    #Soma
    n1 = float(input1.get())
    n2 = float(input2.get())
    result = n1 + n2
    result1.configure(text=f'Resultado da Soma: {result}')
    
    #Multiplicação
    n1 = float(input1.get())
    n2 = float(input2.get())
    multi = n1 * n2
    result2.configure(text=f'Resultado da Multiplicação: {multi}')
    
    #Divisão
    n1 = float(input1.get())
    n2 = float(input2.get())
    divisao = n1 / n2
    result3.configure(text=f'Resutlado da Divisão: {divisao}')
    
    #Produto Notável +
    n1 = float(input1.get())
    n2 = float(input2.get())
    prdt = (n1+n2)*(n1+n2)
    result4.configure(text=f'Resultado do Produto Notável(+): {prdt}')
    
def limpar_tela():
    input1.delete(0, ctk.END)
    input2.delete(0, ctk.END)

#Tela    
tela = ctk.CTk()
tela.title('Graçinha')
tela.geometry('500x500')
tela.resizable(False, False)

texto = ctk.CTkLabel(tela, text='Calculadora da Gracinha', font=('Inter', 40))
texto.pack()

frame_input = CTkFrame(tela)
frame_input.pack()

input1 = ctk.CTkEntry(frame_input)
input1.grid(row=0, column=0, padx=10, pady=10)

input2 = ctk.CTkEntry(frame_input)
input2.grid(row=0, column=1, padx=10, pady=10)

butao2 = ctk.CTkButton(tela, text='Calcular', command=calcular)
butao2.pack()

frame_result = CTkFrame(tela)
frame_result.pack(pady=50)

result1 = ctk.CTkLabel(frame_result, text='Resultado da Soma: ',font=('Inter', 20))
result1.pack()

result2 = ctk.CTkLabel(frame_result, text='Resultado da Multiplicação: ',font=('Inter', 20))
result2.pack()

result3 = ctk.CTkLabel(frame_result, text='Resulta da Divisão: ',font=('Inter', 20))
result3.pack()

result4 = ctk.CTkLabel(frame_result, text='Resultado do Produto Nótavel(+): ',font=('Inter', 20))
result4.pack()

butao_fechar = ctk.CTkButton(tela, text='Fechar', command=fechar_tela)
butao_fechar.pack(pady=50)

butao_limpar = ctk.CTkButton(tela, text='Limpar', command=limpar_tela)
butao_limpar.pack()

tela.mainloop()#Final do Codigo