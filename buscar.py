import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint

from modCancion import *
from modAlbum import *
from modArtista import *

def ventanaBuscar():
    buscar = tk.Tk()
    buscar.title("Buscar")
    buscar.geometry("800x600")
    buscar.configure(background="LightGreen")

    #LABELS
    label9 = tk.Label(buscar, text="BUSCAR", bg="LightGreen", fg="black")
    label9.config(font=("Courier", 44), pady=40)
    label9.pack()

    #CANCION

    
    buscarCancionFrame = tk.Frame(buscar, bg="LightGreen")
    
    label10 = tk.Label(buscarCancionFrame, text="BUSCAR UNA CANCION", bg="LightGreen", fg="black")
    label10.config(font=("Courier", 24))
    label10.pack(side=tk.TOP, anchor=tk.NW)
    
    tituloc = tk.Label(buscarCancionFrame, text="Titulo:", bg="LightGreen", fg="black")
    tituloc.config(font=("Courier", 12))
    tituloc.pack(side=tk.LEFT)

    tituloCancionEdit = tk.Text(buscarCancionFrame, width=30, height=1)
    tituloCancionEdit.pack(side=tk.LEFT)

    def buscarCancion():
        tituloCancionB = tituloCancionEdit.get("1.0",'end-1c')
        ventanaModCancion(tituloCancionB)

    button1 = tk.Button(buscarCancionFrame, text="BUSCAR", bg="green", command=buscarCancion)
    button1.config(font=("Courier", 20))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    buscarCancionFrame.pack(side=tk.TOP, anchor=tk.NW)
    
    #ALBUM
    buscarAlbumFrame = tk.Frame(buscar, bg="LightGreen")
    
    label11 = tk.Label(buscarAlbumFrame, text="BUSCAR UN ALBUM", bg="LightGreen", fg="black")
    label11.config(font=("Courier", 24))
    label11.pack(side=tk.TOP, anchor=tk.NW)
    
    tituloa = tk.Label(buscarAlbumFrame, text="Titulo:", bg="LightGreen", fg="black")
    tituloa.config(font=("Courier", 12))
    tituloa.pack(side=tk.LEFT)

    tituloAlbumEdit = tk.Text(buscarAlbumFrame, width=30, height=1)
    tituloAlbumEdit.pack(side=tk.LEFT)

    def buscarAlbum():
        tituloAlbumB = tituloAlbumEdit.get("1.0",'end-1c')
        ventanaModAlbum(tituloAlbumB)
    
    button2 = tk.Button(buscarAlbumFrame, text="BUSCAR", bg="green", command=buscarAlbum)
    button2.config(font=("Courier", 20))
    button2.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    buscarAlbumFrame.pack(side=tk.TOP, anchor=tk.NW)

    #ARTISTA
    buscarArtistaFrame = tk.Frame(buscar, bg="LightGreen")
    
    label12 = tk.Label(buscarArtistaFrame, text="BUSCAR UN ARTISTA", bg="LightGreen", fg="black")
    label12.config(font=("Courier", 24))
    label12.pack(side=tk.TOP, anchor=tk.NW)
    
    nombrear = tk.Label(buscarArtistaFrame, text="Nombre:", bg="LightGreen", fg="black")
    nombrear.config(font=("Courier", 12))
    nombrear.pack(side=tk.LEFT)

    nombreArtistaEdit = tk.Text(buscarArtistaFrame, width=30, height=1)
    nombreArtistaEdit.pack(side=tk.LEFT)

    def buscarArtista():
        nombreArtistaB = nombreArtistaEdit.get("1.0",'end-1c')
        ventanaModArtista(nombreArtistaB)
    
    button3 = tk.Button(buscarArtistaFrame, text="BUSCAR", bg="green", command=buscarArtista)
    button3.config(font=("Courier", 20))
    button3.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)


    buscarArtistaFrame.pack(side=tk.TOP, anchor=tk.NW)
    
    #reproduccion

    rep = tk.Frame(buscar, bg="LightGreen")

    button4 = tk.Button(rep, text="Reproducir", bg="green", command=buscarCancion)
    button4.config(font=("Courier", 20))
    button4.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    rep.pack(side=tk.TOP, anchor=tk.NW)

