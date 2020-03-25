import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint

from proyecto import *

def ventanaInactivarCancion():
    inactivar = tk.Tk()
    inactivar.title("Registrar albumes")
    inactivar.geometry("800x600")
    inactivar.configure(background="LightGreen")

    #LABELS
    label7 = tk.Label(inactivar, text="INACTIVACION", bg="LightGreen", fg="black")
    label7.config(font=("Courier", 44), pady=40)
    label7.pack()

    label8 = tk.Label(inactivar, text="INACTIVAR UNA CANCION", bg="LightGreen", fg="black")
    label8.config(font=("Courier", 24))
    label8.pack(side=tk.TOP, anchor=tk.NW)



    #TITULO
    tituloCancionFrame = tk.Frame(inactivar)
    
    tituloo = tk.Label(tituloCancionFrame, text="Titulo:", bg="LightGreen", fg="black")
    tituloo.config(font=("Courier", 12))
    tituloo.pack(side=tk.LEFT)

    tituloEdit = tk.Text(tituloCancionFrame, width=30, height=1)
    tituloEdit.pack(side=tk.LEFT)

    tituloCancionFrame.pack(side=tk.TOP, anchor=tk.NW)
        
    def borrarCampos4():
        tituloEdit.delete('1.0', 'end-1c')
        
    def inactivarCancion():
        titulo = tituloEdit.get("1.0",'end-1c')
        
        #LLAMAR A FUNCION AQUI
        
        borrarCampos4()

    #BOTONES
    registrarborrarFrame = tk.Frame(inactivar, bg="LightGreen")
    
    button1 = tk.Button(registrarborrarFrame, text="INACTIVAR", bg="green", command=inactivarCancion)
    button1.config(font=("Courier", 20))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button2 = tk.Button(registrarborrarFrame, text="BORRAR", bg="red", command=borrarCampos4)
    button2.config(font=("Courier", 20))
    button2.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)
