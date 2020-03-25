import psycopg2
from psycopg2 import Error
from random import randint
from tkinter import messagebox

def buscarArtista():
    try:
        nombre = "AC/DC"
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto1")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM artist WHERE name=%s;'''
        
        cursor.execute(create_table_query, (nombre,))

        result = cursor.fetchall()

        idArtista = ""
        nombre = ""
        
        for row in result:
            idArtista = str(row[0])
            nombre = row[1]
            
        
        connection.commit()
        
        mensaje = "ID: " + idArtista + ".\n" + "Nombre: " + nombre + ".\n"
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el producto.", title="Consulta fallida")
        print ("No se pudo registrar cliente.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")






buscarArtista()
