import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint

from querys import *

def ventanaRegAlbum():
    registroAlbum = tk.Tk()
    registroAlbum.title("Registrar albumes")
    registroAlbum.geometry("800x600")
    registroAlbum.configure(background="LightGreen")

    #LABELS
    label3 = tk.Label(registroAlbum, text="ALBUMES", bg="LightGreen", fg="black")
    label3.config(font=("Courier", 44), pady=40)
    label3.pack()

    label4 = tk.Label(registroAlbum, text="REGISTRAR NUEVO ALBUM", bg="LightGreen", fg="black")
    label4.config(font=("Courier", 24))
    label4.pack(side=tk.TOP, anchor=tk.NW)

    #ID
    idAlbumFrame = tk.Frame(registroAlbum)
    
    idd = tk.Label(idAlbumFrame, text="ID:", bg="LightGreen", fg="black")
    idd.config(font=("Courier", 12))
    idd.pack(side=tk.LEFT)

    idEdit = tk.Text(idAlbumFrame, width=30, height=1)
    idEdit.pack(side=tk.LEFT)

    idAlbumFrame.pack(side=tk.TOP, anchor=tk.NW)

    #TITULO
    tituloAlbumFrame = tk.Frame(registroAlbum)
    
    tituloo = tk.Label(tituloAlbumFrame, text="Titulo:", bg="LightGreen", fg="black")
    tituloo.config(font=("Courier", 12))
    tituloo.pack(side=tk.LEFT)

    tituloEdit = tk.Text(tituloAlbumFrame, width=30, height=1)
    tituloEdit.pack(side=tk.LEFT)

    tituloAlbumFrame.pack(side=tk.TOP, anchor=tk.NW)
    
    #ARTISTA
    artistaFrame = tk.Frame(registroAlbum)
    
    artistaa = tk.Label(artistaFrame, text="Artista:", bg="LightGreen", fg="black")
    artistaa.config(font=("Courier", 12))
    artistaa.pack(side=tk.LEFT)

    artistaEdit = tk.Text(artistaFrame, width=30, height=1)
    artistaEdit.pack(side=tk.LEFT)

    artistaFrame.pack(side=tk.TOP, anchor=tk.NW)

    #Campo
    Campo = tk.Frame(registroAlbum)
    
    campo1 = tk.Label(Campo, text="Campo:", bg="LightGreen", fg="black")
    campo1.config(font=("Courier", 12))
    campo1.pack(side=tk.LEFT)

    campo2 = tk.Text(Campo, width=30, height=1)
    campo2.pack(side=tk.LEFT)
    Campo.pack(side=tk.TOP, anchor=tk.NW)

    #NOMBRE
    emailF = tk.Frame(registroAlbum)
    
    email = tk.Label(emailF, text="Email:", bg="LightGreen", fg="black")
    email.config(font=("Courier", 12))
    email.pack(side=tk.LEFT)

    emailEd = tk.Text(emailF, width=30, height=1)
    emailEd.pack(side=tk.LEFT)
    emailF.pack(side=tk.TOP, anchor=tk.NW)
    
    def borrarCampos2():
        idEdit.delete('1.0', 'end-1c')
        tituloEdit.delete('1.0', 'end-1c')
        artistaEdit.delete('1.0', 'end-1c')
        
    def registrarAlbum():
        idAlbum = idEdit.get("1.0",'end-1c')
        titulo = tituloEdit.get("1.0",'end-1c')
        artista = artistaEdit.get("1.0",'end-1c')
        campo = campo2.get("1.0",'end-1c')
        emailV = emailEd.get("1.0",'end-1c')

        insertarAlbum(idAlbum, titulo, artista, campo, emailV)
        
        borrarCampos2()

    #BOTONES
    registrarborrarFrame = tk.Frame(registroAlbum, bg="LightGreen")
    
    button1 = tk.Button(registrarborrarFrame, text="REGISTRAR", bg="green", command=registrarAlbum)
    button1.config(font=("Courier", 20))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button2 = tk.Button(registrarborrarFrame, text="BORRAR", bg="red", command=borrarCampos2)
    button2.config(font=("Courier", 20))
    button2.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)


