import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint

from proyecto import *
from querys import *

def ventanaRegCancion():
    registroCancion = tk.Tk()
    registroCancion.title("Registrar canciones")
    registroCancion.geometry("800x600")
    registroCancion.configure(background="LightGreen")

    #LABELS
    label5 = tk.Label(registroCancion, text="CANCIONES", bg="LightGreen", fg="black")
    label5.config(font=("Courier", 44), pady=40)
    label5.pack()

    label6 = tk.Label(registroCancion, text="REGISTRAR NUEVA CANCION", bg="LightGreen", fg="black")
    label6.config(font=("Courier", 24))
    label6.pack(side=tk.TOP, anchor=tk.NW)

    #ID
    idCancionFrame = tk.Frame(registroCancion)
    
    idd = tk.Label(idCancionFrame, text="ID:", bg="LightGreen", fg="black")
    idd.config(font=("Courier", 12))
    idd.pack(side=tk.LEFT)

    idEdit = tk.Text(idCancionFrame, width=30, height=1)
    idEdit.pack(side=tk.LEFT)

    idCancionFrame.pack(side=tk.TOP, anchor=tk.NW)

    #TITULO CANCION
    tituloCancionFrame = tk.Frame(registroCancion)
    
    tituloo = tk.Label(tituloCancionFrame, text="Titulo cancion:", bg="LightGreen", fg="black")
    tituloo.config(font=("Courier", 12))
    tituloo.pack(side=tk.LEFT)

    tituloEdit = tk.Text(tituloCancionFrame, width=30, height=1)
    tituloEdit.pack(side=tk.LEFT)

    tituloCancionFrame.pack(side=tk.TOP, anchor=tk.NW)

    #TITULO Album
    tituloAlbumFrame = tk.Frame(registroCancion)
    
    titulooo = tk.Label(tituloAlbumFrame, text="Titulo album:", bg="LightGreen", fg="black")
    titulooo.config(font=("Courier", 12))
    titulooo.pack(side=tk.LEFT)

    tituloAlbumEdit = tk.Text(tituloAlbumFrame, width=30, height=1)
    tituloAlbumEdit.pack(side=tk.LEFT)

    tituloAlbumFrame.pack(side=tk.TOP, anchor=tk.NW)
    
    #ARTISTA
    artistaFrame = tk.Frame(registroCancion)
    
    artistaa = tk.Label(artistaFrame, text="Artista:", bg="LightGreen", fg="black")
    artistaa.config(font=("Courier", 12))
    artistaa.pack(side=tk.LEFT)

    artistaEdit = tk.Text(artistaFrame, width=30, height=1)
    artistaEdit.pack(side=tk.LEFT)

    artistaFrame.pack(side=tk.TOP, anchor=tk.NW)

    #Genero:
    generoFrame = tk.Frame(registroCancion)
    
    generoo = tk.Label(generoFrame, text="Genero:", bg="LightGreen", fg="black")
    generoo.config(font=("Courier", 12))
    generoo.pack(side=tk.LEFT)

    generoEdit = tk.Text(generoFrame, width=30, height=1)
    generoEdit.pack(side=tk.LEFT)

    generoFrame.pack(side=tk.TOP, anchor=tk.NW)

    #Precio:
    precioFrame = tk.Frame(registroCancion)
    
    precioo = tk.Label(precioFrame, text="Precio unitario:", bg="LightGreen", fg="black")
    precioo.config(font=("Courier", 12))
    precioo.pack(side=tk.LEFT)

    precioEdit = tk.Text(precioFrame, width=30, height=1)
    precioEdit.pack(side=tk.LEFT)

    precioFrame.pack(side=tk.TOP, anchor=tk.NW)

    #e.bind("<Tab>", focus_next_widget)
    def borrarCampos3():
        idEdit.delete('1.0', 'end-1c')
        tituloEdit.delete('1.0', 'end-1c')
        tituloAlbumEdit.delete('1.0', 'end-1c')
        artistaEdit.delete('1.0', 'end-1c')
        generoEdit.delete('1.0', 'end-1c')
        precioEdit.delete('1.0', 'end-1c')
        
    def registrarCancion():
        idCancion = idEdit.get("1.0",'end-1c')
        titulo = tituloEdit.get("1.0",'end-1c')
        tituloAlbum = tituloAlbumEdit.get("1.0",'end-1c')
        artista = artistaEdit.get("1.0",'end-1c')
        genero = generoEdit.get("1.0",'end-1c')
        precio = precioEdit.get("1.0",'end-1c')

        insertarCancion(idCancion, titulo, tituloAlbum, artista, genero, precio)
        
        borrarCampos3()

    #BOTONES
    registrarborrarFrame = tk.Frame(registroCancion, bg="LightGreen")
    
    button1 = tk.Button(registrarborrarFrame, text="REGISTRAR", bg="green", command=registrarCancion)
    button1.config(font=("Courier", 20))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button2 = tk.Button(registrarborrarFrame, text="BORRAR", bg="red", command=borrarCampos3)
    button2.config(font=("Courier", 20))
    button2.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)



