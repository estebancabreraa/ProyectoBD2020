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
from recomendacion import *

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

    f2 = tk.Frame(menu, bg = "LightGreen")
    buscar = tk.Button(f2, text="Buscar", command=ventanaBuscar)
    buscar.config(font=("Courier", 20))
    buscar.pack(side=tk.LEFT, padx=20, pady=10, ipadx=10)

    comprar = tk.Button(f2, text="Comprar", command=ventanaComprar)
    comprar.config(font=("Courier", 20))
    comprar.pack(side=tk.LEFT, padx=20, pady=10, ipadx=10)
    f2.pack(side=tk.TOP)

    f3 = tk.Frame(menu, bg = "LightGreen")
    checko = tk.Button(f3, text="Check out", command=ventanaCheckout)
    checko.config(font=("Courier", 20))
    checko.pack(side=tk.LEFT, padx=20, pady=10, ipadx=10)

    reproducir = tk.Button(f3, text="Reproducir", command=ventanaReproduccion)
    reproducir.config(font=("Courier", 20))
    reproducir.pack(side=tk.LEFT, padx=20, pady=10, ipadx=10)
    f3.pack(side=tk.TOP)

    f4 = tk.Frame(menu, bg = "LightGreen")
    reporteria = tk.Button(f4, text="Reporteria", command=ventanaReporteria)
    reporteria.config(font=("Courier", 20))
    reporteria.pack(side=tk.LEFT, padx=20, pady=10, ipadx=10)

    records = tk.Button(f4, text = "Records", command = ventanaRecords)
    records.config(font = ("Courier", 20))
    records.pack(side=tk.LEFT, padx=20, pady=10, ipadx=10)
    f4.pack(side=tk.TOP)

    f5 = tk.Frame(menu, bg = "LightGreen")
    sim = tk.Button(f5, text = "Simulacion", command = simulacion)
    sim.config(font = ("Courier", 20))
    sim.pack(side=tk.LEFT, padx=20, pady=10, ipadx=10)

    bit = tk.Button(f5, text = "Bitacora", command = bitacora)
    bit.config(font = ("Courier", 20))
    bit.pack(side=tk.LEFT, padx=20, pady=10, ipadx=10)
    f5.pack(side=tk.TOP)

    re = tk.Button(menu, text = "Recomendacion", command = reco)
    re.config(font = ("Courier", 20))
    re.pack(pady = 10)
    menu.mainloop()
