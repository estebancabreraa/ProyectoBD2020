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

def queriesRecords(query):
    try:  
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT artist1.name, count(artist1.name)
from album album1 join artist artist1 on album1.artistid = artist1.artistid
group by artist1.name
order by count(artist1.name) desc LIMIT 5;
'''
        
        cursor.execute(create_table_query)

        result = cursor.fetchall()

        createCSV("artistaAlbum.csv")
        listFile(result, "artistaAlbum.csv", ["album", "vendidos"])
        
        for row in result:
            print("Nombre =", row[0],)
            print("Albumes =" , row[1], "\n")
        
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
