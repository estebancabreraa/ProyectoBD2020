import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint
from compraCancion import *

################################################################################
#                                    Comprar                                   #
################################################################################
def ventanaComprar():
    
    compra = tk.Tk()
    compra.title("Comprar")
    compra.geometry("500x100")
    compra.configure(background="LightGreen")

    buscarCancionFrame = tk.Frame(compra, bg="LightGreen")
    
    label20 = tk.Label(buscarCancionFrame, text="COMPRAR UNA CANCION", bg="LightGreen", fg="black")
    label20.config(font=("Courier", 24))
    label20.pack(side=tk.TOP, anchor=tk.NW)
    
    titulocan = tk.Label(buscarCancionFrame, text="Titulo:", bg="LightGreen", fg="black")
    titulocan.config(font=("Courier", 12))
    titulocan.pack(side=tk.LEFT)

    tituloCancionEdit = tk.Text(buscarCancionFrame, width=30, height=1)
    tituloCancionEdit.pack(side=tk.LEFT)
    
    def buscarCancion():
        tituloCancionB = tituloCancionEdit.get("1.0",'end-1c')
        ventanaCompraCancion(tituloCancionB)

    button1 = tk.Button(buscarCancionFrame, text="BUSCAR", bg="green", command=buscarCancion)
    button1.config(font=("Courier", 20))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    buscarCancionFrame.pack(side=tk.TOP, anchor=tk.NW)

ventanaComprar()
   

