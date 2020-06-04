import tkinter as tk
from tkinter import messagebox
from random import randint
from tkinter import Entry
import psycopg2
from psycopg2 import Error
from menuAdmin import *
from reporteria import *
from menuUsuario import *

def recomendacion(genero):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        create_table_query = ''''''

        cursor.execute(create_table_query)
        result = cursor.fetchall()

        for row in result:
            print("Anio =", row[0],)
            print("Total Ventas =", row[1],)
            print("Semana =" , row[2], "\n")
            
        connection.commit()                 
            
        messagebox.showinfo(message=result, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el producto.", title="Consulta fallida")
        print ("No se pudo realizar lo solicitado", error)
            
    finally:
            #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

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

    combobox2 = ttk.Combobox(cancionFr, width=10, values = ["Rock", "Jazz", "Latin", "Pop", "World"], state = "readonly")
    combobox2.pack(side = tk.LEFT)
    combobox2.current(0)
    
    cancionFr.pack(side=tk.TOP)

    label5 = tk.Label(venMain, text="  ", font=("Courier", 13), bg="LightGreen", fg="black")
    label5.pack()

    genero = combobox2.current()
        

    def geti():
        genero = combobox2.current()
        if(genero == 0):
            genero = 1
            print(genero)
                
        elif(genero == 1):
            genero = 2
            print(genero)
                
        elif(genero == 2):
            genero = 7
            print(genero)

        elif(genero == 3):
            genero = 9
            print(genero)

        elif(genero == 4):
            genero = 16
            print(genero)

        else:
            genero = 16
            print(genero)
        gen = str(genero)
        
        recomendacion(gen)

    regArtista = tk.Button(venMain, text="Descubrir", command=geti)
    regArtista.config(font=("Courier", 20))
    regArtista.pack()

    venMain.mainloop()
