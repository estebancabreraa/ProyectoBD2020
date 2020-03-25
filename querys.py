import psycopg2
from psycopg2 import Error
from random import randint
from tkinter import messagebox

def buscarArtista(nombre):
    try:
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

    return result

def buscarAlbum(nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto1")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM album WHERE title=%s;'''
        
        cursor.execute(create_table_query, (nombre,))

        result = cursor.fetchall()

        albumid = ""
        title = ""
        artistid = ""
        
        for row in result:
            albumid = str(row[0])
            title = row[1]
            artistid = row[2]
            
        
        connection.commit()
        
        mensaje = "Se encontro el album exitosamente."
        print(result)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el album.", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    return result

def buscarCancion(nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto1")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM track WHERE name=%s;'''
        
        cursor.execute(create_table_query, (nombre,))

        result = cursor.fetchall()

        trackid = ""
        name = ""
        albumid = ""
        mediatypeid = ""
        genreid = ""
        composer = ""
        miliseconds = ""
        bytess = 0
        unitprice = 0
        estado = True
        colaborador = ""
        
        for row in result:
            trackid = row[0]
            name = row[1]
            albumid = row[2]
            mediatypeid = row[3]
            genreid = row[4]
            composer = row[5]
            miliseconds = row[6]
            bytess = row[7]
            unitprice = row[8]
            estado = row[9]
            colaborador = row[10]
            
        
        connection.commit()

        mensaje = "La cancion se encontro exitosamente."
        
        messagebox.showinfo(message=mensaje, title="Consulta")
        print(result)
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro la cancion.", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    return result


