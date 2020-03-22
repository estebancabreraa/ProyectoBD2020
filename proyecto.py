################################################################################
#                                    PROYECTO 1                                #
################################################################################
#BASES DE DATOS

#INTEGRANTES:
#Esteban Cabrera - 17781
#Andrea Elias - 17046
#Kevin Macario - 17163

import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint

################################################################################
#                                    MAIN                                      #
################################################################################
#Simulacion
#simulacionCompras(10000,"2019/05/16")
#GUI
login = tk.Tk()
login.title("ESPLORIFY")
login.geometry('800x600')
login.configure(background="green")

#TITULO
label1 = tk.Label(login, text="Esplorify", bg="green", fg="black")
label1.config(font=("Courier", 44), pady=40)
label1.pack()


#Usuario
user = tk.Frame(login)
    
label2 = tk.Label(user, text="Usuario:", bg="green", fg="black")
label2.config(font=("Courier", 12))
label2.pack(side=tk.LEFT)

edit1 = tk.Text(user, width=30, height=1)
edit1.pack(side=tk.LEFT)
user.pack(side=tk.TOP, anchor="c",  pady=10)

#PASSWORD
password = tk.Frame(login)
    
label3 = tk.Label(password, text="Contraseña", bg="green", fg="black")
label3.config(font=("Courier", 12))
label3.pack(side=tk.LEFT)

edit2 = tk.Text(password, width=30, height=1)
edit2.pack(side=tk.LEFT)
password.pack(side=tk.TOP, anchor="c",  pady=10)
    
#Buttons
button1 = tk.Button(login, text="Entrar")#, command=mostrarVentanaClientes)
button1.config(font=("Courier", 20))
button1.pack(pady=10, ipadx=8)

button2 = tk.Button(login, text="Restaurar\ncontraseña")#, command=mostrarVentanaProductos)
button2.config(font=("Courier", 20))
button2.pack(pady=10)



login.mainloop()
