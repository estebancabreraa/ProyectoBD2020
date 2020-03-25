import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint

from proyecto import *

def ventanaModArtista(nombreArtista):
    registroArtista = tk.Tk()
    registroArtista.title("Modificar artista")
    registroArtista.geometry("800x600")
    registroArtista.configure(background="LightGreen")

    #LABELS
    label1 = tk.Label(registroArtista, text="ARTISTAS", bg="LightGreen", fg="black")
    label1.config(font=("Courier", 44), pady=40)
    label1.pack()

    label2 = tk.Label(registroArtista, text="MODIFICAR ARTISTA", bg="LightGreen", fg="black")
    label2.config(font=("Courier", 24))
    label2.pack(side=tk.TOP, anchor=tk.NW)

    #ID
    idArtistaFrame = tk.Frame(registroArtista)
    
    idd = tk.Label(idArtistaFrame, text="ID:", bg="LightGreen", fg="black")
    idd.config(font=("Courier", 12))
    idd.pack(side=tk.LEFT)

    idEdit = tk.Text(idArtistaFrame, width=30, height=1)
    idEdit.pack(side=tk.LEFT)

    idArtistaFrame.pack(side=tk.TOP, anchor=tk.NW)

    #NOMBRE
    nombreArtistaFrame = tk.Frame(registroArtista)
    
    nombree = tk.Label(nombreArtistaFrame, text="Nombre:", bg="LightGreen", fg="black")
    nombree.config(font=("Courier", 12))
    nombree.pack(side=tk.LEFT)

    nombreEdit = tk.Text(nombreArtistaFrame, width=30, height=1)
    nombreEdit.pack(side=tk.LEFT)

    nombreEdit.insert(1.0, nombreArtista)
    
    nombreArtistaFrame.pack(side=tk.TOP, anchor=tk.NW)

    def modificarArtista():
        idArtista = idEdit.get("1.0",'end-1c')
        nombreArtista = nombreEdit.get("1.0",'end-1c')

        #LLAMAR A FUNCION AQUI

    c=""
    def eliminarArtista():
         c = "1"

    #BOTONES
    registrarborrarFrame = tk.Frame(registroArtista, bg="LightGreen")
    
    button1 = tk.Button(registrarborrarFrame, text="MODIFICAR", bg="green", command=modificarArtista)
    button1.config(font=("Courier", 20))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button2 = tk.Button(registrarborrarFrame, text="ELIMINAR", bg="red", command=eliminarArtista)
    button2.config(font=("Courier", 20))
    button2.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)


