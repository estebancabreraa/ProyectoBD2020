import tkinter as tk
from tkinter import messagebox
from random import randint
from tkinter import Entry
from tkinter import ttk
import psycopg2
from psycopg2 import Error
from reporteria import *
from ReporteriaQueries import *
from tkcalendar import *


def ventanaRecords():

    records = tk.Tk()
    records.title("Records")
    records.geometry("800x600")
    records.configure(background = "LightGreen")

    label1= tk.Label(records, text="Records", font=("Century", 44), pady=40, bg="LightGreen", fg="black")
    label1.pack()

    campo1 = tk.Frame(records, bg = "LightGreen")
    
    label1 = tk.Label(campo1, text="Seleccione record:", font=("Courier", 23), bg="LightGreen", fg="black")
    label1.pack(side=tk.TOP)

    combobox = ttk.Combobox(campo1, width=50, values = ["q1", "q2", "q3", "q4", "q5"])
    combobox.pack(side = tk.BOTTOM)
    
    campo1.pack(side=tk.TOP)

    

    label4 = tk.Label(records, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    label4.pack(side=tk.TOP)

    
    
    campo2 = tk.Frame(records, bg = "LightGreen")
    label2 = tk.Label(campo2, text="Seleccione rango de fecha:", font=("Courier", 17), bg="LightGreen", fg="black")
    label2.pack(side=tk.TOP)
    
    label2 = tk.Label(campo2, text="Inicio:", font=("Courier", 13), bg="LightGreen", fg="black")
    label2.pack(side=tk.LEFT, ipady = 7)
    
    date = DateEntry(campo2, background='darkblue', foreground='white', year=2020)
    date.pack(side = tk.LEFT)
    
    label3 = tk.Label(campo2, text="     Final:", font=("Courier", 13), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT, ipady = 7)
    
    date = DateEntry(campo2, background='darkblue', foreground='white', year=2020)
    date.pack(side = tk.LEFT)

    campo2.pack(side=tk.TOP)


    label4 = tk.Label(records, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    label4.pack(side=tk.TOP)


    campo3 = tk.Frame(records, bg = "LightGreen")

    label4 = tk.Label(campo3, text="Ingrese elementos a mostrar:", font=("Courier", 17), bg="LightGreen", fg="black")
    label4.pack(side=tk.TOP)

    label5 = tk.Label(campo3, text=" Usuario:", font=("Courier", 13), bg="LightGreen", fg="black")
    label5.pack(side=tk.LEFT, ipady = 7)

    usuario = ttk.Entry(campo3, width=15)
    usuario.pack(side = tk.LEFT)

    label6 = tk.Label(campo3, text="   Cantidad:", font=("Courier", 13), bg="LightGreen", fg="black")
    label6.pack(side=tk.LEFT, ipady = 7)

    combobox = ttk.Combobox(campo3, width=10, values = [20, 17, 15, 13, 10, 7, 5, 1])
    combobox.pack(side = tk.LEFT)
    
    campo3.pack(side=tk.TOP)

    label5 = tk.Label(records, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    label5.pack(side=tk.TOP)
    
    campo4 = tk.Frame(records, bg = "LightGreen") 
    mostrar = tk.Button(campo4, text = "Mostrar", font=("Courier", 15), command="")
    mostrar.pack(side=tk.BOTTOM)
    campo4.pack(ipadx = 50)

    label6 = tk.Label(records, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    label6.pack(side=tk.TOP)

    

    records.mainloop()

    
