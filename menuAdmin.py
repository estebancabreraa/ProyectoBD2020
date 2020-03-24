import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint

from proyecto import *
from regArtista import *
from regAlbum import *

################################################################################
#                                    MENU                                      #
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
    regArtista = tk.Button(menu, text="Registrar Artista", command=ventanaRegArtista)
    regArtista.config(font=("Courier", 20))
    regArtista.pack(pady=10, ipadx=8)

    regAlbum = tk.Button(menu, text="Registrar Album", command=ventanaRegAlbum)
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

