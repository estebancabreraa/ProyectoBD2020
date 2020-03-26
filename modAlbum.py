import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint

from querys import *

def ventanaModAlbum(tituloAlbum):
    bAlbum = buscarAlbumMod(tituloAlbum)
    idAlbum = bAlbum[0]
    titulo = bAlbum[1]
    
    registroAlbum = tk.Tk()
    registroAlbum.title("Registrar albumes")
    registroAlbum.geometry("800x600")
    registroAlbum.configure(background="LightGreen")

    #LABELS
    label14 = tk.Label(registroAlbum, text="ALBUMES", bg="LightGreen", fg="black")
    label14.config(font=("Courier", 44), pady=40)
    label14.pack()

    label15 = tk.Label(registroAlbum, text="MODIFICAR UN ALBUM", bg="LightGreen", fg="black")
    label15.config(font=("Courier", 24))
    label15.pack(side=tk.TOP, anchor=tk.NW)

    #ID
    idAlbumFrame = tk.Frame(registroAlbum)
    
    idd = tk.Label(idAlbumFrame, text="ID:", bg="LightGreen", fg="black")
    idd.config(font=("Courier", 12))
    idd.pack(side=tk.LEFT)

    idEdit = tk.Text(idAlbumFrame, width=30, height=1)
    idEdit.pack(side=tk.LEFT)

    idEdit.insert("end-1c", idAlbum)
    idEdit.configure(state="disabled")

    idAlbumFrame.pack(side=tk.TOP, anchor=tk.NW)

    #TITULO
    tituloAlbumFrame = tk.Frame(registroAlbum)
    
    tituloo = tk.Label(tituloAlbumFrame, text="Titulo:", bg="LightGreen", fg="black")
    tituloo.config(font=("Courier", 12))
    tituloo.pack(side=tk.LEFT)

    tituloEdit = tk.Text(tituloAlbumFrame, width=30, height=1)
    tituloEdit.pack(side=tk.LEFT)

    tituloEdit.insert(1.0, titulo)
    
    tituloAlbumFrame.pack(side=tk.TOP, anchor=tk.NW)
        
        
    def modificarAlbum2():
        idAlbum = idEdit.get("1.0",'end-1c')
        titulo = tituloEdit.get("1.0",'end-1c')

        modificarAlbum(idAlbum, titulo)

    def eliminarAlbum2():
         eliminarAlbum(idAlbum)

    #BOTONES
    registrarborrarFrame = tk.Frame(registroAlbum, bg="LightGreen")
    
    button1 = tk.Button(registrarborrarFrame, text="MODIFICAR", bg="green", command=modificarAlbum2)
    button1.config(font=("Courier", 20))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button2 = tk.Button(registrarborrarFrame, text="ELIMINAR", bg="red", command=eliminarAlbum2)
    button2.config(font=("Courier", 20))
    button2.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)



