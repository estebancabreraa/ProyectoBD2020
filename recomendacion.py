import tkinter as tk
from tkinter import messagebox
from random import randint
from tkinter import Entry
import psycopg2
from psycopg2 import Error
from menuAdmin import *
from reporteria import *
from menuUsuario import *

def ventanaRecomendacion():
    
    venMain = tk.Tk()
    venMain.title("Descubrimiento Semanal")
    venMain.geometry("800x700")
    venMain.configure(background="LightGreen")

    #TITULO
    labelMenu = tk.Label(venMain, text="Descubrimiento Semanal", bg="LightGreen", fg="black")
    labelMenu.config(font=("Century", 44), pady=50)
    labelMenu.pack()

    cancionFr = tk.Frame(venMain, bg = "LightGreen")

    label5 = tk.Label(cancionFr, text="Genero:", font=("Courier", 13), bg="LightGreen", fg="black")
    label5.pack(side=tk.LEFT, ipady = 7)

    combobox2 = ttk.Combobox(cancionFr, width=10, values = [""], state = "readonly")
    combobox2.pack(side = tk.LEFT)
    combobox2.current(0)
    
    cancionFr.pack(side=tk.TOP)

    label5 = tk.Label(venMain, text="  ", font=("Courier", 13), bg="LightGreen", fg="black")
    label5.pack()

    def rec():
        genero = combobox.current()

        recomendacion(genero)

    regArtista = tk.Button(venMain, text="Descubrir", command="")
    regArtista.config(font=("Courier", 20))
    regArtista.pack()

    venMain.mainloop()
ventanaRecomendacion()
