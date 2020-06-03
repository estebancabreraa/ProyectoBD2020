import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from checkout import *
from querys import *
from querys_mongo import *


################################################################################
#                                    Comprar                                   #
################################################################################
def ventanaCompraCancion(tituloCancion):
    
    compraCancion = tk.Tk()
    compraCancion.title("Comprar")
    compraCancion.geometry("800x600")
    compraCancion.configure(background="LightGreen")

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

    #LABELS
    label15 = tk.Label(compraCancion, text="CANCIONES", bg="LightGreen", fg="black")
    label15.config(font=("Courier", 44), pady=40)
    label15.pack()

    label16 = tk.Label(compraCancion, text="COMPRAR UNA CANCION", bg="LightGreen", fg="black")
    label16.config(font=("Courier", 24))
    label16.pack(side=tk.TOP, anchor=tk.NW)

    #ID
    idCancionFrame = tk.Frame(compraCancion)
    
    idd = tk.Label(idCancionFrame, text="ID:", bg="LightGreen", fg="black")
    idd.config(font=("Courier", 12))
    idd.pack(side=tk.LEFT)

    idEdit = tk.Text(idCancionFrame, width=30, height=1)
    idEdit.pack(side=tk.LEFT)

    idEdit.insert(1.0, idCancion)

    idCancionFrame.pack(side=tk.TOP, anchor=tk.NW)

    #TITULO CANCION
    tituloCancionFrame = tk.Frame(compraCancion)
    
    tituloo = tk.Label(tituloCancionFrame, text="Titulo cancion:", bg="LightGreen", fg="black")
    tituloo.config(font=("Courier", 12))
    tituloo.pack(side=tk.LEFT)

    tituloEdit = tk.Text(tituloCancionFrame, width=30, height=1)
    tituloEdit.pack(side=tk.LEFT)

    tituloEdit.insert(1.0, titulo)

    tituloCancionFrame.pack(side=tk.TOP, anchor=tk.NW)

    #TITULO Album
    tituloAlbumFrame = tk.Frame(compraCancion)
    
    titulooo = tk.Label(tituloAlbumFrame, text="Titulo album:", bg="LightGreen", fg="black")
    titulooo.config(font=("Courier", 12))
    titulooo.pack(side=tk.LEFT)

    tituloAlbumEdit = tk.Text(tituloAlbumFrame, width=30, height=1)
    tituloAlbumEdit.pack(side=tk.LEFT)

    tituloAlbumEdit.insert(1.0, tituloAlbum)

    tituloAlbumFrame.pack(side=tk.TOP, anchor=tk.NW)
    
    #ARTISTA
    artistaFrame = tk.Frame(compraCancion)
    
    artistaa = tk.Label(artistaFrame, text="Artista:", bg="LightGreen", fg="black")
    artistaa.config(font=("Courier", 12))
    artistaa.pack(side=tk.LEFT)

    artistaEdit = tk.Text(artistaFrame, width=30, height=1)
    artistaEdit.pack(side=tk.LEFT)

    artistaEdit.insert(1.0, composer)

    artistaFrame.pack(side=tk.TOP, anchor=tk.NW)

    #Genero:
    generoFrame = tk.Frame(compraCancion)
    
    generoo = tk.Label(generoFrame, text="Genero:", bg="LightGreen", fg="black")
    generoo.config(font=("Courier", 12))
    generoo.pack(side=tk.LEFT)

    generoEdit = tk.Text(generoFrame, width=30, height=1)
    generoEdit.pack(side=tk.LEFT)

    generoEdit.insert(1.0, genero)

    generoFrame.pack(side=tk.TOP, anchor=tk.NW)

    #Duracion:
    duracionFrame = tk.Frame(compraCancion)
    
    duracionn = tk.Label(duracionFrame, text="Duracion (milisegundos):", bg="LightGreen", fg="black")
    duracionn.config(font=("Courier", 12))
    duracionn.pack(side=tk.LEFT)

    duracionEdit = tk.Text(duracionFrame, width=30, height=1)
    duracionEdit.pack(side=tk.LEFT)

    duracionEdit.insert(1.0, milliseconds)

    duracionFrame.pack(side=tk.TOP, anchor=tk.NW)

    #Precio:
    precioFrame = tk.Frame(compraCancion)
    
    precioo = tk.Label(precioFrame, text="Precio unitario):", bg="LightGreen", fg="black")
    precioo.config(font=("Courier", 12))
    precioo.pack(side=tk.LEFT)

    precioEdit = tk.Text(precioFrame, width=30, height=1)
    precioEdit.pack(side=tk.LEFT)

    precioEdit.insert(1.0, unitprice)

    precioFrame.pack(side=tk.TOP, anchor=tk.NW)

    #e.bind("<Tab>", focus_next_widget)

    def anadirCarrito():
        idCancion = idEdit.get("1.0",'end-1c')
        precio = precioEdit.get("1.0",'end-1c')
        insertarCarrito(1, idCancion, precio)
        

    #BOTONES
    registrarborrarFrame = tk.Frame(compraCancion, bg="LightGreen")
    
    button1 = tk.Button(registrarborrarFrame, text="Añadir al Carrito", bg="green", command=anadirCarrito)
    button1.config(font=("Courier", 20))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)


    button2 = tk.Button(registrarborrarFrame, text="Check Out", bg="red", command=ventanaCheckout)
    button2.config(font=("Courier", 20))
    button2.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)

