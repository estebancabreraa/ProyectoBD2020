import tkinter as tk
from tkinter import messagebox
from random import randint
from tkinter import Entry
from tkinter import ttk
#import psycopg2
#from psycopg2 import Error

#from proyecto import *
#from regArtista import *
#from regAlbum import *



def Reporteria():

    reporteria = tk.Tk()
    reporteria.title("Reporteria")
    reporteria.geometry("800x600")
    reporteria.configure(background = "LightGreen")

    label1= tk.Label(reporteria, text="Reporteria", font=("Century", 44), pady=40, bg="LightGreen", fg="black")
    label1.pack()
    ########
    #QUERYS#
    ########

    #ARTISTAS CON MAS ALBUMES

    campo2 = tk.Frame(reporteria, bg = "LightGreen")
    label2 = tk.Label(campo2, text="Artistas con mas albumes: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label2.pack(side=tk.LEFT)
    button2 = tk.Button(campo2, text = "Mostrar", font=("Courier", 15), command="")
    button2.pack(side = tk.LEFT)
    campo2.pack(side=tk.TOP, anchor=tk.NW, ipady = 2)

    #Generos con mas artistas

    campo3 = tk.Frame(reporteria, bg = "LightGreen")
    label3 = tk.Label(campo3, text="Generos con mas artistas: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT)
    button3 = tk.Button(campo3, text = "Mostrar", font=("Courier", 15), command="")
    button3.pack(side = tk.LEFT)
    campo3.pack(side=tk.TOP, anchor=tk.NW, ipady = 2)

    #Total de duracion de cada playlist

    campo3 = tk.Frame(reporteria, bg = "LightGreen")
    label3 = tk.Label(campo3, text="Total de duracion de cada playlist: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT)
    button3 = tk.Button(campo3, text = "Mostrar", font=("Courier", 15), command="")
    button3.pack(side = tk.LEFT)
    campo3.pack(side=tk.TOP, anchor=tk.NW, ipady = 2)

    #Cancion con mas duracion

    campo3 = tk.Frame(reporteria, bg = "LightGreen")
    label3 = tk.Label(campo3, text="Cancion con más duración: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT)
    button3 = tk.Button(campo3, text = "Mostrar", font=("Courier", 15), command="")
    button3.pack(side = tk.LEFT)
    campo3.pack(side=tk.TOP, anchor=tk.NW, ipady = 2)

    #Usuarios con mas canciones

    campo3 = tk.Frame(reporteria, bg = "LightGreen")
    label3 = tk.Label(campo3, text="Usuarios con mas canciones: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT)
    button3 = tk.Button(campo3, text = "Mostrar", font=("Courier", 15), command="")
    button3.pack(side = tk.LEFT)
    campo3.pack(side=tk.TOP, anchor=tk.NW, ipady = 2)

    #Promedio de duracion de cada cancion por genero

    campo3 = tk.Frame(reporteria, bg = "LightGreen")
    label3 = tk.Label(campo3, text="Promedio de duracion de cada cancion por genero: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT)
    button3 = tk.Button(campo3, text = "Mostrar", font=("Courier", 15), command="")
    button3.pack(side = tk.LEFT)
    campo3.pack(side=tk.TOP, anchor=tk.NW, ipady = 2)

    #Cantidad de artistas diferentes por playlist

    campo3 = tk.Frame(reporteria, bg = "LightGreen")
    label3 = tk.Label(campo3, text="Cantidad de artistas diferentes por playlist: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT)
    button3 = tk.Button(campo3, text = "Mostrar", font=("Courier", 15), command="")
    button3.pack(side = tk.LEFT)
    campo3.pack(side=tk.TOP, anchor=tk.NW, ipady = 2)

    #Los artistas con mas diversidad de generos musicales

    campo3 = tk.Frame(reporteria, bg = "LightGreen")
    label3 = tk.Label(campo3, text="artistas con mas diversidad de generos musicales: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT)
    button3 = tk.Button(campo3, text = "Mostrar", font=("Courier", 15), command="")
    button3.pack(side = tk.LEFT)
    campo3.pack(side=tk.TOP, anchor=tk.NW, ipady = 2)

    reporteria.mainloop()

Reporteria()
