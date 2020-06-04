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

def recomendacion(artista):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        create_table_query = '''SELECT  track1.rep, track1.name, artist1.name
FROM album album1 join artist artist1 on album1.artistid = artist1.artistid join track track1 on track1.albumid = album1.albumid
WHERE artist1.name =''' + "'" + artista + "'" + '''
group by artist1.name, track1.rep, track1.name
ORDER BY track1.rep DESC'''

        cursor.execute(create_table_query)
        result = cursor.fetchall()

        for row in result:
            print("Cancion =", row[1],)
            
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

def reco():
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

    combobox2 = ttk.Combobox(cancionFr, width=10, values = ["Aerosmith", "Camila Cabello", "Metallica", "Queen", "Kiss", "Incognito", "Olodum", "Skank", "Lost", "U2"], state = "readonly")
    combobox2.pack(side = tk.LEFT)
    combobox2.current(0)
    
    cancionFr.pack(side=tk.TOP)

    label5 = tk.Label(venMain, text="  ", font=("Courier", 13), bg="LightGreen", fg="black")
    label5.pack()

    genero = combobox2.current()
        
    def geti():
        artista = combobox2.get()
        ar = str(artista)
        
        recomendacion(ar)

    regArtista = tk.Button(venMain, text="Descubrir", command=geti)
    regArtista.config(font=("Courier", 20))
    regArtista.pack()

    venMain.mainloop()
reco()
