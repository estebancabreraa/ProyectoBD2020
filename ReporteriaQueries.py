import csv
import psycopg2
from psycopg2 import Error
from random import randint
from tkinter import messagebox

lista = []

def createCSV(filename):
    nombreArchivo = open(filename, "w")
    nombreArchivo.close()

def listFile(lista, filename,lista2):
    with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerow(lista2) 
            writer.writerows(lista)
            
def artistaAlbum():
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

def CancionGenero():
    try:
       
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT genre1.name, count(genre1.name)
from genre genre1 join track track1 on genre1.genreid = track1.genreid
group by genre1.name
order by count(genre1.name) desc LIMIT 5
'''
        
        cursor.execute(create_table_query)
        

        result = cursor.fetchall()

        createCSV("cancionGenero.csv")
        listFile(result, "cancionGenero.csv", ["Genero", "Canciones"])
        
        for row in result:
            print("Genero =", row[0],)
            print("Canciones =" , row[1], "\n")
            
        
        connection.commit()
        
        
        print(result)
        
        messagebox.showinfo(message=result, title="Canciones por Genero")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el producto.", title="Consulta fallida")
        print ("No se pudo realizar lo solicitado", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def playlistDuracion():
    try:
       
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT playlist.playlistid, playlist.name, SUM(track.milliseconds/1000) AS Cuenta
FROM playlist
LEFT JOIN playlisttrack ON playlisttrack.playlistid = playlist.playlistid
LEFT JOIN track ON track.trackid = playlisttrack.trackid
WHERE track.milliseconds IS NOT NULL
GROUP BY playlist.playlistid 
ORDER BY Cuenta desc;
'''
        
        cursor.execute(create_table_query)
        

        result = cursor.fetchall()

        createCSV("playlistDuracion.csv")
        listFile(result, "playlistDuracion.csv", ["idPlaylist", "Nombre", "Duraciom"])
        
        for row in result:
            print("idPlaylist =", row[0],)
            print("Nombre =" , row[1],)
            print("Duracion =" , row[2], "\n")
        
        connection.commit()
        
        
        print(result)
        
        messagebox.showinfo(message=result, title="Canciones por Genero")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el producto.", title="Consulta fallida")
        print ("No se pudo realizar lo solicitado", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def CancionMayorDuracion():
    try:
       
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT artist1.name, track1.name, (track1.milliseconds/1000) AS Duracion
from album album1 join artist artist1 on album1.artistid = artist1.artistid join track track1 on track1.albumid = album1.albumid 
WHERE track1.mediatypeid = 1 OR track1.mediatypeid = 2 OR track1.mediatypeid = 4 OR track1.mediatypeid = 5
order by (track1.milliseconds) desc LIMIT 5;
'''
        
        cursor.execute(create_table_query)
        

        result = cursor.fetchall()

        createCSV("CancionMayorDuracion.csv")
        listFile(result, "CancionMayorDuracion.csv", ["Artista", "Cancion", "Duracion"])
        
        for row in result:
            print("artista =", row[0],)
            print("cancion =" , row[1],)
            print("Duracion =" , row[2], "\n")
        
        connection.commit()
        
        
        print(result)
        
        messagebox.showinfo(message=result, title="Canciones de Mayor Duracion")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el producto.", title="Consulta fallida")
        print ("No se pudo realizar lo solicitado", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def usuariosTop():
    try:
       
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT customer1.firstname, customer1.lastname , COUNT (track1.colaborador) AS Canciones_Agregadas
FROM track track1 JOIN customer customer1 ON customer1.email = track1.colaborador
GROUP BY customer1.firstname, customer1.lastname
ORDER BY Canciones_Agregadas DESC LIMIT 5;
'''
        
        cursor.execute(create_table_query)
        

        result = cursor.fetchall()

        createCSV("usuariosTop.csv")
        listFile(result, "usuariosTop.csv", ["Nombre", "Apellido", "Canciones Agregadas"])
        
        for row in result:
            print("Nombre =", row[0],)
            print("Apellido =" , row[1],)
            print("Canciones Agregadas =" , row[2], "\n")
        
        connection.commit()
        
        
        print(result)
        
        messagebox.showinfo(message=result, title="Top Usuarios")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el producto.", title="Consulta fallida")
        print ("No se pudo realizar lo solicitado", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def promedioGenero():
    try:
       
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT genre1.name, AVG((track1.milliseconds/1000)) AS AveragePerGenre
FROM genre genre1 join track track1 on genre1.genreid = track1.genreid
WHERE track1.mediatypeid = 2 OR track1.mediatypeid = 4 OR track1.mediatypeid = 5 OR track1.mediatypeid = 1
GROUP BY genre1.name
ORDER BY AveragePerGenre DESC

'''
        
        cursor.execute(create_table_query)
        

        result = cursor.fetchall()

        createCSV("promedioGenero.csv")
        listFile(result, "promedioGenero.csv", ["Genero", "Duracion Promedio"])
        
        for row in result:
            print("Genero =", row[0],)
            print("Duracion Promedio =" , row[1], "\n")
        
        connection.commit()
        
        
        print(result)
        
        messagebox.showinfo(message=result, title="Duracion promedio por genero")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el producto.", title="Consulta fallida")
        print ("No se pudo realizar lo solicitado", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def playlistArtista():
    try:
       
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT playlist1.name, count(artist1.artistid)
from playlist playlist1 join playlisttrack playlisttrack1 on playlist1.playlistid = playlisttrack1.playlistid join track track1 on track1.trackid = playlisttrack1.trackid join album album1 on album1.albumid = track1.albumid join artist artist1 on artist1.artistid = album1.artistid
group by playlist1.name
order by count(artist1.name) desc

'''
        
        cursor.execute(create_table_query)
        

        result = cursor.fetchall()

        createCSV("playlistArtista.csv")
        listFile(result, "playlistArtista.csv", ["Genero", "Total Artistas"])
        
        for row in result:
            print("Genero =", row[0],)
            print("Total Artistas =" , row[1], "\n")
        
        connection.commit()
        
        
        print(result)
        
        messagebox.showinfo(message=result, title="Artistas por Genero")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el producto.", title="Consulta fallida")
        print ("No se pudo realizar lo solicitado", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def diversidad():
    try:
       
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT artist1.name, count(DISTINCT track1.genreid) as generos
from genre genre1 join track track1 on genre1.genreid = track1.genreid join album album1 on album1.albumid = track1.albumid join artist artist1 on artist1.artistid = album1.artistid
group by artist1.name
order by count(genre1.genreid) desc LIMIT 5
'''
        
        cursor.execute(create_table_query)
        

        result = cursor.fetchall()

        createCSV("diversidad.csv")
        listFile(result, "diversidad.csv", ["Artista", "Genero"])
        
        for row in result:
            print("Artista =", row[0],)
            print("Generos =" , row[1], "\n")
        
        connection.commit()
        
        
        print(result)
        
        messagebox.showinfo(message=result, title="Artistas con mayor diversidad de Generos")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el producto.", title="Consulta fallida")
        print ("No se pudo realizar lo solicitado", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")