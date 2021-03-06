import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint
from regArtista import *
from regAlbum import *
from regCancion import *
from inactivar import *
from buscar import *
from reporteria import *

################################################################################
#                                    MENU                                      #
################################################################################
def ventanaMenuUsuario():

    menu = tk.Tk()
    menu.title("Menu")
    menu.geometry("800x700")
    menu.configure(background="LightGreen")

    #TITULO
    labelMenu = tk.Label(menu, text="Menu", bg="LightGreen", fg="black")
    labelMenu.config(font=("Century", 44), pady=20)
    labelMenu.pack()
    
    labelMenu1 = tk.Label(menu, text="Usuario", bg="LightGreen", fg="black")
    labelMenu1.config(font=("Century", 20), pady=5)
    labelMenu1.pack()

    #Buttons
    regArtista = tk.Button(menu, text="Registrar Artista", command=ventanaRegArtista)
    regArtista.config(font=("Courier", 20))
    regArtista.pack(pady=10, ipadx=8)

    regAlbum = tk.Button(menu, text="Registrar Album", command=ventanaRegAlbum)
    regAlbum.config(font=("Courier", 20))
    regAlbum.pack(pady=10)

    regCancion = tk.Button(menu, text="Registrar Cancion", command=ventanaRegCancion)
    regCancion.config(font=("Courier", 20))
    regCancion.pack(pady=10)

    buscar = tk.Button(menu, text="Buscar", command=ventanaBuscar)
    buscar.config(font=("Courier", 20))
    buscar.pack(pady=10, ipadx=8)

    recomendacion = tk.Button(menu, text="Buscar", command="")
    recomendacion.config(font=("Courier", 20))
    recomendacion.pack(pady=10, ipadx=8)
