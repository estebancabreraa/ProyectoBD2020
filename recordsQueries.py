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

def ventasSemanales(inicio, final):
        try:  
        
            connection = psycopg2.connect(user = "postgres",
                                          password = "123456",
                                          host = "127.0.0.1",
                                          port = "5433",
                                          database = "proyecto2")
            cursor = connection.cursor()
            
            create_table_query = '''SELECT invoice1.invoicedate, genre1.name, invoiceline1.trackid, COUNT(invoiceline1.trackid) as totalVentas
FROM genre genre1 join track track1 on genre1.genreid = track1.trackid join invoiceline invoiceline1 on invoiceline1.trackid =genre1.genreid join invoice invoice1 on invoiceline1.invoiceid = invoice1.invoiceid
WHERE invoicedate > '''+ "'" + inicio + "'" + ''' and invoicedate < ''' + "'" + final + "'" + '''
GROUP BY genre1.name, invoiceline1.trackid, invoice1.invoicedate
ORDER BY totalVentas DESC'''
            
            
            cursor.execute(create_table_query)

            result = cursor.fetchall()

            createCSV("9.ventasSemanales.csv")
            listFile(result, "9.ventasSemanales.csv", ["Anio", "Total de Ventas", "Semana"])
            
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

def ventasArtista(inicio, final, cantidad):
        try:  
        
            connection = psycopg2.connect(user = "postgres",
                                          password = "123456",
                                          host = "127.0.0.1",
                                          port = "5433",
                                          database = "proyecto2")
            cursor = connection.cursor()
            
            create_table_query = '''SELECT invoice1.invoicedate, artist1.name, invoiceline1.trackid, SUM(invoice1.total) as totalVentas
FROM album album1 join artist artist1 on album1.artistid = artist1.artistid join invoiceline invoiceline1 on invoiceline1.trackid = album1.albumid join invoice invoice1 on invoiceline1.invoiceid = invoice1.invoiceid
WHERE invoicedate > '''+ "'" + inicio + "'" + ''' and invoicedate < '''+ "'" + final + "'" + ''' and invoice1.total IS NOT NULL
GROUP BY artist1.name, invoiceline1.trackid, invoice1.invoicedate
ORDER BY totalVentas DESC
LIMIT ''' + cantidad 
            
            
            cursor.execute(create_table_query)

            result = cursor.fetchall()

            createCSV("10.ventasArtista.csv")
            listFile(result, "10.ventasArtista.csv", ["Fechas", "Artista", "Id Cancion", "Total Ventas"])
            
            for row in result:
                print("Fecha =", row[0])
                print("Artista =", row[1])
                print("Id Cancion =", row[2])
                print("Total Totales =" , row[3], "\n")
            
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

def ventasGenero(inicio, final, cantidad):
        try:  
        
            connection = psycopg2.connect(user = "postgres",
                                          password = "123456",
                                          host = "127.0.0.1",
                                          port = "5433",
                                          database = "proyecto2")
            cursor = connection.cursor()
            
            create_table_query = '''SELECT invoice1.invoicedate, genre1.name, invoiceline1.trackid, track1.genreid, sum(invoice1.total) as totalVentas
FROM genre genre1 join track track1 on genre1.genreid = track1.genreid join invoiceline invoiceline1 on invoiceline1.trackid =track1.trackid join invoice invoice1 on invoiceline1.invoiceid = invoice1.invoiceid
WHERE invoicedate > '''+ "'" + inicio + "'" + ''' and invoicedate < '''+ "'" + final + "'" + ''' and invoice1.total IS NOT NULL
GROUP BY genre1.name, invoiceline1.trackid, invoice1.invoicedate, track1.genreid
ORDER BY totalVentas DESC
LIMIT ''' + cantidad 
            
            cursor.execute(create_table_query)

            result = cursor.fetchall()

            createCSV("11.ventasGenero.csv")
            listFile(result, "11.ventasGenero.csv", ["Fecha", "Genero", "Id Cancion", "Total Ventas"])
            
            for row in result:
                print("Fecha =", row[0])
                print("Genero =", row[1])
                print("Id Cancion =", row[2])
                print("Total Ventas =" , row[3], "\n")
            
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

def masRep(cantidad, artista):
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
ORDER BY track1.rep DESC
LIMIT ''' + cantidad
            
            cursor.execute(create_table_query)

            result = cursor.fetchall()

            createCSV("12.masReproducidas.csv")
            listFile(result, "12.masReproducidas.csv", ["Artista", "Cancion", "Numero de Reproducciones"])
            
            for row in result:
                print("Artista =", row[0])
                print("Nombre de la cancion =" , row[1])
                print("Numero de reproducciones =", row[2])
                
                
            
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
