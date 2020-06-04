import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint

from querys import *

def ventanaModCancion(tituloCancion):
    bCancion = buscarCancion(tituloCancion)
    idCancion = bCancion[0]
    titulo = bCancion[1]
    albumid = bCancion[2]
    mediatype = bCancion[3]
    genreid = bCancion[4]
    composer = bCancion[5]
    milliseconds = bCancion[6]
    bytess = bCancion[7]
    unitprice = bCancion[8]
    estado = bCancion[9]
    colaborador = bCancion[10]

    genero = buscarGeneroID(genreid)
    tituloAlbum = buscarAlbumNombre(albumid)
    
    registroCancion = tk.Tk()
    registroCancion.title("Registrar canciones")
    registroCancion.geometry("800x600")
    registroCancion.configure(background="LightGreen")

    #LABELS
    label15 = tk.Label(registroCancion, text="CANCIONES", bg="LightGreen", fg="black")
    label15.config(font=("Courier", 44), pady=40)
    label15.pack()

    label16 = tk.Label(registroCancion, text="MODIFICAR UNA CANCION", bg="LightGreen", fg="black")
    label16.config(font=("Courier", 24))
    label16.pack(side=tk.TOP, anchor=tk.NW)

    #ID
    idCancionFrame = tk.Frame(registroCancion)
    
    idd = tk.Label(idCancionFrame, text="ID:", bg="LightGreen", fg="black")
    idd.config(font=("Courier", 12))
    idd.pack(side=tk.LEFT)

    idEdit = tk.Text(idCancionFrame, width=30, height=1)
    idEdit.pack(side=tk.LEFT)

    idEdit.insert(1.0, idCancion)

    idCancionFrame.pack(side=tk.TOP, anchor=tk.NW)

    #TITULO CANCION
    tituloCancionFrame = tk.Frame(registroCancion)
    
    tituloo = tk.Label(tituloCancionFrame, text="Titulo cancion:", bg="LightGreen", fg="black")
    tituloo.config(font=("Courier", 12))
    tituloo.pack(side=tk.LEFT)

    tituloEdit = tk.Text(tituloCancionFrame, width=30, height=1)
    tituloEdit.pack(side=tk.LEFT)

    tituloEdit.insert(1.0, titulo)

    tituloCancionFrame.pack(side=tk.TOP, anchor=tk.NW)

    #TITULO Album
    tituloAlbumFrame = tk.Frame(registroCancion)
    
    titulooo = tk.Label(tituloAlbumFrame, text="Titulo album:", bg="LightGreen", fg="black")
    titulooo.config(font=("Courier", 12))
    titulooo.pack(side=tk.LEFT)

    tituloAlbumEdit = tk.Text(tituloAlbumFrame, width=30, height=1)
    tituloAlbumEdit.pack(side=tk.LEFT)

    tituloAlbumEdit.insert(1.0, tituloAlbum)

    tituloAlbumFrame.pack(side=tk.TOP, anchor=tk.NW)
    
    #ARTISTA
    artistaFrame = tk.Frame(registroCancion)
    
    artistaa = tk.Label(artistaFrame, text="Artista:", bg="LightGreen", fg="black")
    artistaa.config(font=("Courier", 12))
    artistaa.pack(side=tk.LEFT)

    artistaEdit = tk.Text(artistaFrame, width=30, height=1)
    artistaEdit.pack(side=tk.LEFT)

    artistaEdit.insert(1.0, composer)

    artistaFrame.pack(side=tk.TOP, anchor=tk.NW)

    #Genero:
    generoFrame = tk.Frame(registroCancion)
    
    generoo = tk.Label(generoFrame, text="Genero:", bg="LightGreen", fg="black")
    generoo.config(font=("Courier", 12))
    generoo.pack(side=tk.LEFT)

    generoEdit = tk.Text(generoFrame, width=30, height=1)
    generoEdit.pack(side=tk.LEFT)

    generoEdit.insert(1.0, genero)

    generoFrame.pack(side=tk.TOP, anchor=tk.NW)

    #Duracion:
    duracionFrame = tk.Frame(registroCancion)
    
    duracionn = tk.Label(duracionFrame, text="Duracion (milisegundos):", bg="LightGreen", fg="black")
    duracionn.config(font=("Courier", 12))
    duracionn.pack(side=tk.LEFT)

    duracionEdit = tk.Text(duracionFrame, width=30, height=1)
    duracionEdit.pack(side=tk.LEFT)

    duracionEdit.insert(1.0, milliseconds)

    duracionFrame.pack(side=tk.TOP, anchor=tk.NW)

    #Precio:
    precioFrame = tk.Frame(registroCancion)
    
    precioo = tk.Label(precioFrame, text="Precio unitario):", bg="LightGreen", fg="black")
    precioo.config(font=("Courier", 12))
    precioo.pack(side=tk.LEFT)

    precioEdit = tk.Text(precioFrame, width=30, height=1)
    precioEdit.pack(side=tk.LEFT)

    precioEdit.insert(1.0, unitprice)

    precioFrame.pack(side=tk.TOP, anchor=tk.NW)

    #Campo
    Campo = tk.Frame(registroCancion)
    
    campo1 = tk.Label(Campo, text="Campo:", bg="LightGreen", fg="black")
    campo1.config(font=("Courier", 12))
    campo1.pack(side=tk.LEFT)

    campo2 = tk.Text(Campo, width=30, height=1)
    campo2.pack(side=tk.LEFT)
    Campo.pack(side=tk.TOP, anchor=tk.NW)

    #NOMBRE
    emailF = tk.Frame(registroCancion)
    
    email = tk.Label(emailF, text="Email:", bg="LightGreen", fg="black")
    email.config(font=("Courier", 12))
    email.pack(side=tk.LEFT)

    emailEd = tk.Text(emailF, width=30, height=1)
    emailEd.pack(side=tk.LEFT)
    emailF.pack(side=tk.TOP, anchor=tk.NW)
    
    #e.bind("<Tab>", focus_next_widget)

    def modificarCancion1():
        idCancion = idEdit.get("1.0",'end-1c')
        titulo = tituloEdit.get("1.0",'end-1c')
        tituloAlbum = tituloAlbumEdit.get("1.0",'end-1c')
        artista = artistaEdit.get("1.0",'end-1c')
        genero = generoEdit.get("1.0",'end-1c')
        duracion = duracionEdit.get("1.0",'end-1c')
        precio = precioEdit.get("1.0",'end-1c')
        campo = campo2.get("1.0",'end-1c')
        emailV = emailEd.get("1.0",'end-1c')
        
        modificarCancion(idCancion, titulo, precio, campo, emailV)
        
    def eliminarCancion1():
        eliminarCancion(idCancion)

    #BOTONES
    registrarborrarFrame = tk.Frame(registroCancion, bg="LightGreen")
    
    button1 = tk.Button(registrarborrarFrame, text="MODIFICAR", bg="green", command=modificarCancion1)
    button1.config(font=("Courier", 20))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button2 = tk.Button(registrarborrarFrame, text="ELIMINAR", bg="red", command=eliminarCancion1)
    button2.config(font=("Courier", 20))
    button2.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)



