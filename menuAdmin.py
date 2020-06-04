import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint
from regArtista import *
from regAlbum import *
from regCancion import *
from inactivar import *
from buscar import *
from reporteria import *
from records import *
from querys_mongo import *
from comprar import *
from checkout import *
from reproducir import *

################################################################################
#                                    MENU                                      #
################################################################################
def ventanaMenu():
    
    menu = tk.Tk()
    menu.title("Menu")
    menu.geometry("800x800")
    menu.configure(background="LightGreen")

    
    #TITULO
    labelMenu = tk.Label(menu, text="Menu: Administrador", bg="LightGreen", fg="black")
    labelMenu.config(font=("Century", 44), pady=15)
    labelMenu.pack()

    #Buttons
    emailF = tk.Frame(menu, bg = "LightGreen")
    regArtista = tk.Button(emailF, text="Registrar Artista", command=ventanaRegArtista)
    regArtista.config(font=("Courier", 20))
    regArtista.pack(side=tk.LEFT, padx=20, pady=10, ipadx=10)

    regAlbum = tk.Button(emailF, text="Registrar Album", command=ventanaRegAlbum)
    regAlbum.config(font=("Courier", 20))
    regAlbum.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    emailF.pack(side=tk.TOP)

    f1 = tk.Frame(menu, bg = "LightGreen")
    regCancion = tk.Button(f1, text="Registrar Cancion", command=ventanaRegCancion)
    regCancion.config(font=("Courier", 20))
    regCancion.pack(side=tk.LEFT, padx=20, pady=10, ipadx=10)

    inactivar = tk.Button(f1, text="Inactivar Cancion", command=ventanaInactivarCancion)
    inactivar.config(font=("Courier", 20))
    inactivar.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    f1.pack(side=tk.TOP)

    buscar = tk.Button(menu, text="Buscar", command=ventanaBuscar)
    buscar.config(font=("Courier", 20))
    buscar.pack(pady=10, ipadx=8)

    comprar = tk.Button(menu, text="Comprar", command=ventanaComprar)
    comprar.config(font=("Courier", 20))
    comprar.pack(pady=10, ipadx=8)

    checko = tk.Button(menu, text="Check out", command=ventanaCheckout)
    checko.config(font=("Courier", 20))
    checko.pack(pady=10, ipadx=8)

    reproducir = tk.Button(menu, text="Reproducir", command=ventanaReproduccion)
    reproducir.config(font=("Courier", 20))
    reproducir.pack(pady=10, ipadx=8)

    reporteria = tk.Button(menu, text="Reporteria", command=ventanaReporteria)
    reporteria.config(font=("Courier", 20))
    reporteria.pack(pady=10)

    records = tk.Button(menu, text = "Records", command = ventanaRecords)
    records.config(font = ("Courier", 20))
    records.pack(pady = 10)

    sim = tk.Button(menu, text = "Simulacion", command = simulacion)
    sim.config(font = ("Courier", 20))
    sim.pack(pady = 10)

    bitacora = tk.Button(menu, text = "Bitacora", command = listFile)
    bitacora.config(font = ("Courier", 20))
    bitacora.pack(pady = 10)



