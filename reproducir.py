import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint
from querys_mongo import *
import webbrowser
from tkinter import messagebox


################################################################################
#                                    Reproducir                                #
################################################################################
def ventanaReproduccion():
    
    reproduccion = tk.Tk()
    reproduccion.title("Reproduccion")
    reproduccion.geometry("500x100")
    reproduccion.configure(background="LightGreen")

    buscarCancionFrame = tk.Frame(reproduccion, bg="LightGreen")
    
    label20 = tk.Label(buscarCancionFrame, text="REPRODUCIR UNA CANCION", bg="LightGreen", fg="black")
    label20.config(font=("Courier", 24))
    label20.pack(side=tk.TOP, anchor=tk.NW)
    
    titulocan = tk.Label(buscarCancionFrame, text="Titulo:", bg="LightGreen", fg="black")
    titulocan.config(font=("Courier", 12))
    titulocan.pack(side=tk.LEFT)

    tituloCancionEdit = tk.Text(buscarCancionFrame, width=30, height=1)
    tituloCancionEdit.pack(side=tk.LEFT)

    mensaje = ""
    def reproducirCancion():
        track = tituloCancionEdit.get("1.0",'end-1c')
        habilitada = False
        habilitada = verificarCompra(track)
        if habilitada:
            webbrowser.open('https://www.youtube.com/watch?v=S-Abebn5kpM', new=2)
        else:
            mensaje = "No se puede reproducir la cancion porque usted no la ha comprado."
            messagebox.showinfo(message=mensaje, title="Reproduccion")
        
    button1 = tk.Button(buscarCancionFrame, text="Reproducir", bg="green", command=reproducirCancion)
    button1.config(font=("Courier", 15))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    buscarCancionFrame.pack(side=tk.TOP, anchor=tk.NW)

