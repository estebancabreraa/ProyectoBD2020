################################################################################
#                                    PROYECTO 1                                #
################################################################################
#BASES DE DATOS

#INTEGRANTES:
#Esteban Cabrera - 17781
#Andrea Elias - 17048
#Kevin Macario - 17163

import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint


################################################################################
#                                    VENTANAS                                  #
################################################################################

def ventanaMenu():
    menu = tk.Tk()
    menu.title("Menu")
    menu.geometry("800x700")
    menu.configure(background="LightGreen")

    #TITULO
    labelMenu = tk.Label(menu, text="Menu", bg="LightGreen", fg="black")
    labelMenu.config(font=("Century", 44), pady=40)
    labelMenu.pack()

    #Buttons
    regArtista = tk.Button(menu, text="Registrar Artista")#, command=mostrarVentanaClientes)
    regArtista.config(font=("Courier", 20))
    regArtista.pack(pady=10, ipadx=8)

    regAlbum = tk.Button(menu, text="Registrar Album")#, command=mostrarVentanaProductos)
    regAlbum.config(font=("Courier", 20))
    regAlbum.pack(pady=10)

    regCancion = tk.Button(menu, text="Registrar Cancion")#, command=mostrarVentanaProductos)
    regCancion.config(font=("Courier", 20))
    regCancion.pack(pady=10)

    inactivar = tk.Button(menu, text="Inactivar Cancion")#, command=mostrarVentanaProductos)
    inactivar.config(font=("Courier", 20))
    inactivar.pack(pady=10)

    modArtista = tk.Button(menu, text="Modificar Artista")#, command=mostrarVentanaClientes)
    modArtista.config(font=("Courier", 20))
    modArtista.pack(pady=10, ipadx=8)

    modAlbum = tk.Button(menu, text="Modificar Album")#, command=mostrarVentanaProductos)
    modAlbum.config(font=("Courier", 20))
    modAlbum.pack(pady=10)

    modCancion = tk.Button(menu, text="Modificar Cancion")#, command=mostrarVentanaProductos)
    modCancion.config(font=("Courier", 20))
    modCancion.pack(pady=10)

################################################################################
#                                    MAIN                                      #
################################################################################
#Simulacion
#simulacionCompras(10000,"2019/05/16")
#GUI
login = tk.Tk()
login.title("ESPLORIFY")
login.geometry('800x600')
login.configure(background="LightGreen")

#TITULO
label1 = tk.Label(login, text="Esplorify", bg="LightGreen", fg="black")
label1.config(font=("Century", 44), pady=40)
label1.pack()


#Usuario
user = tk.Frame(login)
    
label2 = tk.Label(user, text="Usuario:", bg="LightGreen", fg="black")
label2.config(font=("Courier", 12))
label2.pack(side=tk.LEFT)

edit1 = tk.Text(user, width=30, height=1)
edit1.pack(side=tk.LEFT)
user.pack(side=tk.TOP, anchor="c",  pady=10)

#PASSWORD
password = tk.Frame(login)
    
label3 = tk.Label(password, text="Contraseña", bg="LightGreen", fg="black")
label3.config(font=("Courier", 12))
label3.pack(side=tk.LEFT)

edit2 = tk.Text(password, width=30, height=1)
edit2.pack(side=tk.LEFT)
password.pack(side=tk.TOP, anchor="c",  pady=10)
    
#Buttons
button1 = tk.Button(login, text="Entrar" , command=ventanaMenu)
button1.config(font=("Courier", 20))
button1.pack(pady=10, ipadx=8)

button2 = tk.Button(login, text="Restaurar\ncontraseña")#, command=mostrarVentanaProductos)
button2.config(font=("Courier", 20))
button2.pack(pady=10)



login.mainloop()
