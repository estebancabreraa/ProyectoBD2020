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
from recordsQueries import *



def ventanaRecords():

    values = ["Ventas por rango de fecha", "Artistas con mas ventas por rango de fecha", "Ventas por genero por rango de fecha", "Canciones con mas reproducciones de un artista"]
    
    def q1():
        date.configure(state = "readonly")
        date2. configure(state = "readonly")
        usuario.configure(state = "disabled")
        combobox2.configure(state = "disabled")
        
    def q2():
        date.configure(state = "readonly")
        date2. configure(state = "readonly")
        usuario.configure(state = "disabled")
        combobox2.configure(state = "readonly")
    def q3():
        date.configure(state = "readonly")
        date2. configure(state = "readonly")
        usuario.configure(state = "disabled")
        combobox2.configure(state = "disabled")
    def q4():
        date.configure(state = "disabled")
        date2. configure(state = "disabled")
        usuario.configure(state = "normal")
        combobox2.configure(state = "readonly")
        
    def method_unknown():
        label1.configure(text="unknown selected")

    def handler(event):
        current = combobox.current()
        value = values[current]
        print("current:", current, "value:", value)
        func_map = {
            "Ventas por rango de fecha": q1,
            "Artistas con mas ventas por rango de fecha": q2,
            "Ventas por genero por rango de fecha": q3,
            "Canciones con mas reproducciones de un artista": q4
            
        }
        func = func_map.get(value, method_unknown)
        func()
    
    records = tk.Tk()
    records.title("Records")
    records.geometry("800x600")
    records.configure(background = "LightGreen")

    label1= tk.Label(records, text="Records", font=("Century", 44), pady=40, bg="LightGreen", fg="black")
    label1.pack()

    campo1 = tk.Frame(records, bg = "LightGreen")
    
    label1 = tk.Label(campo1, text="Seleccione record:", font=("Courier", 23), bg="LightGreen", fg="black")
    label1.pack(side=tk.TOP)

    combobox = ttk.Combobox(campo1, width=50, values = ["Ventas por rango de fecha", "Artistas con mas ventas por rango de fecha", "Ventas por genero por rango de fecha ", "Canciones con mas reproducciones de un artista"], state='readonly')
    combobox.bind("<<ComboboxSelected>>", handler)
    combobox.pack(side = tk.BOTTOM)
    combobox.current(0)
    
    campo1.pack(side=tk.TOP)

    

    label4 = tk.Label(records, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    label4.pack(side=tk.TOP)

    
    
    campo2 = tk.Frame(records, bg = "LightGreen")
    label2 = tk.Label(campo2, text="Seleccione rango de fecha:", font=("Courier", 17), bg="LightGreen", fg="black")
    label2.pack(side=tk.TOP)
    
    label2 = tk.Label(campo2, text="Inicio:", font=("Courier", 13), bg="LightGreen", fg="black")
    label2.pack(side=tk.LEFT, ipady = 7)
    
    date = DateEntry(campo2, background='darkblue', foreground='white', year=2020, state='readonly' )
    date.pack(side = tk.LEFT)
    
    label3 = tk.Label(campo2, text="     Final:", font=("Courier", 13), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT, ipady = 7)
    
    date2 = DateEntry(campo2, background='darkblue', foreground='white', year=2020, state='readonly')
    date2.pack(side = tk.LEFT)

    campo2.pack(side=tk.TOP)


    label4 = tk.Label(records, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    label4.pack(side=tk.TOP)


    campo3 = tk.Frame(records, bg = "LightGreen")

    label4 = tk.Label(campo3, text="Ingrese elementos a mostrar:", font=("Courier", 17), bg="LightGreen", fg="black")
    label4.pack(side=tk.TOP)

    label5 = tk.Label(campo3, text="Usuario:", font=("Courier", 13), bg="LightGreen", fg="black")
    label5.pack(side=tk.LEFT, ipady = 7)

    usuario = tk.Text(campo3, width=12, height=1, state = "disabled")
    usuario.pack(side = tk.LEFT)

    label6 = tk.Label(campo3, text="   Cantidad:", font=("Courier", 13), bg="LightGreen", fg="black")
    label6.pack(side=tk.LEFT, ipady = 7)

    combobox2 = ttk.Combobox(campo3, width=10, values = [20, 17, 15, 13, 10, 7, 5, 1], state='disabled')
    combobox2.pack(side = tk.LEFT)
    combobox2.current(0)
    
    campo3.pack(side=tk.TOP)

    label5 = tk.Label(records, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    label5.pack(side=tk.TOP)

    def mostrarRes():
        query = combobox.current()
        inicio = str(date.get_date())
        final = str(date2.get_date())
        nombre = str(usuario.get("1.0",'end-1c'))
        numero = str(combobox2.get())
        
        if(query == 0):
            ventasSemanales(inicio, final)
                
        elif(query == 1):
            ventasArtista(inicio, final, numero)
            
        elif(query == 2):
            ventasGenero(inicio, final)

        elif(query == 3):
            masRep(numero, nombre)
                
        else:
            print(query)

    
    campo4 = tk.Frame(records, bg = "LightGreen") 
    mostrar = tk.Button(campo4, text = "Mostrar", font=("Courier", 15), command=mostrarRes)
    mostrar.pack(side=tk.BOTTOM)
    campo4.pack(ipadx = 50)

    label6 = tk.Label(records, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    label6.pack(side=tk.TOP)

    records.mainloop()
 
