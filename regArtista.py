import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint

from querys import *

def ventanaRegArtista():
    registroArtista = tk.Tk()
    registroArtista.title("Registrar artista")
    registroArtista.geometry("800x600")
    registroArtista.configure(background="LightGreen")

    #LABELS
    label1 = tk.Label(registroArtista, text="ARTISTAS", bg="LightGreen", fg="black")
    label1.config(font=("Courier", 44), pady=40)
    label1.pack()

    label2 = tk.Label(registroArtista, text="REGISTRAR NUEVO ARTISTA", bg="LightGreen", fg="black")
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

    nombreArtistaFrame.pack(side=tk.TOP, anchor=tk.NW)

    #Campo
    Campo = tk.Frame(registroArtista)
    
    campo1 = tk.Label(Campo, text="Campo:", bg="LightGreen", fg="black")
    campo1.config(font=("Courier", 12))
    campo1.pack(side=tk.LEFT)

    campo2 = tk.Text(Campo, width=30, height=1)
    campo2.pack(side=tk.LEFT)
    Campo.pack(side=tk.TOP, anchor=tk.NW)

    #NOMBRE
    emailF = tk.Frame(registroArtista)
    
    email = tk.Label(emailF, text="Email:", bg="LightGreen", fg="black")
    email.config(font=("Courier", 12))
    email.pack(side=tk.LEFT)

    emailEd = tk.Text(emailF, width=30, height=1)
    emailEd.pack(side=tk.LEFT)
    emailF.pack(side=tk.TOP, anchor=tk.NW)

    def borrarCampos1():
        idEdit.delete('1.0', 'end-1c')
        nombreEdit.delete('1.0', 'end-1c')

    def registrarArtista():
        idArtista = idEdit.get("1.0",'end-1c')
        nombreArtista = nombreEdit.get("1.0",'end-1c')
        campo = campo2.get("1.0",'end-1c')
        emailV = emailEd.get("1.0",'end-1c')

        insertarArtista(idArtista, nombreArtista, campo, emailV)
        
        borrarCampos1()

    #BOTONES
    registrarborrarFrame = tk.Frame(registroArtista, bg="LightGreen")
    
    button1 = tk.Button(registrarborrarFrame, text="REGISTRAR", bg="green", command=registrarArtista)
    button1.config(font=("Courier", 20))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button2 = tk.Button(registrarborrarFrame, text="BORRAR", bg="red", command=borrarCampos1)
    button2.config(font=("Courier", 20))
    button2.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)

