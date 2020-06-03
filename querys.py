import psycopg2
from psycopg2 import Error
from random import randint
from tkinter import messagebox


################################################################################
#                                         BUSCAR                               #
################################################################################

def getClientInfo(idd):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM customer WHERE customerid=%s;'''
        
        cursor.execute(create_table_query, (idd,))

        result = cursor.fetchall()

        customerid = ""
        fname = ""
        lname = ""
        
        for row in result:
            customerid = row[0]
            fname = row[1]
            lname = row[2]

        resultado = [customerid, fname, lname]
        
        connection.commit()

        mensaje = "La cancion se encontro exitosamente."
        
      
        print(result)
    except (Exception, psycopg2.DatabaseError) as error :
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    return resultado

def buscarArtista(nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM artist WHERE name=%s;'''
        
        cursor.execute(create_table_query, (nombre,))

        result = cursor.fetchall()

        idArtista = ""
        nombre = ""
        
        for row in result:
            idArtista = row[0]
            nombre = row[1]
            
        resultado = [idArtista, nombre]
        
        connection.commit()
        
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el artista.", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    return resultado

def buscarArtista(nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM artist WHERE name=%s;'''
        
        cursor.execute(create_table_query, (nombre,))

        result = cursor.fetchall()

        idArtista = ""
        nombre = ""
        
        for row in result:
            idArtista = row[0]
            nombre = row[1]
            
        resultado = [idArtista, nombre]
        
        connection.commit()
        
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el artista.", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    return resultado


def buscarAlbum(nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM album WHERE title=%s;'''
        
        cursor.execute(create_table_query, (nombre,))

        result = cursor.fetchall()

        albumid = ""
        title = ""
        artistid = ""
        
        for row in result:
            albumid = row[0]
            title = row[1]
            artistid = row[2]
            
        resultado = [albumid, title, artistid]
        connection.commit()
        
        mensaje = "Se encontro el album exitosamente."
        print(resultado)
        
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

    return albumid


def buscarAlbumNombre(idd):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM album WHERE albumid=%s;'''
        
        cursor.execute(create_table_query, (idd,))

        result = cursor.fetchall()

        albumid = 0
        title = ""
        artistid = ""
        
        for row in result:
            albumid = row[0]
            title = row[1]
            artistid = row[2]
            
        resultado = [albumid, title, artistid]
        connection.commit()
        
        mensaje = "Se encontro el album exitosamente."
        print(resultado)
        
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

    return title

def buscarAlbumMod(nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM album WHERE title=%s;'''
        
        cursor.execute(create_table_query, (nombre,))

        result = cursor.fetchall()

        albumid = ""
        title = ""
        artistid = ""
        
        for row in result:
            albumid = row[0]
            title = row[1]
            artistid = row[2]
            
        resultado = [albumid, title, artistid]
        connection.commit()
        
        mensaje = "Se encontro el album exitosamente."
        print(resultado)
        
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

    return resultado

def buscarCancion(nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
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
        modBy = ""
        modField = ""
        reproducciones = 0
        
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
            modBy = row[11]
            modField = row[12]
            reproducciones = row[13]

        resultado = [trackid, name, albumid, mediatypeid, genreid, composer, miliseconds, bytess, unitprice, estado, colaborador, modBy, modField, reproducciones]
        
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
    return resultado

##

def getSongInfo(idd):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM track WHERE trackid=%s;'''
        
        cursor.execute(create_table_query, (idd,))

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
        modBy = ""
        modField = ""
        reproducciones = 0
        
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
            modBy = row[11]
            modField = row[12]
            reproducciones = row[13]

        resultado = [trackid, name, unitprice]
        
        connection.commit()

        mensaje = "La cancion se encontro exitosamente."
        
        print(result)
    except (Exception, psycopg2.DatabaseError) as error :
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    return resultado

##

def buscarCancionPorID(idd):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM track WHERE trackid=%s;'''
        
        cursor.execute(create_table_query, (idd,))

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
        modBy = ""
        modField = ""
        reproducciones = 0
        
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
            modBy = row[11]
            modField = row[12]
            reproducciones = row[13]

        resultado = [trackid, name, albumid, mediatypeid, genreid, composer, miliseconds, bytess, unitprice, estado, colaborador, modBy, modField, reproducciones]
        
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
    return resultado
##
def buscarCancionID(idd):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM track WHERE trackid=%s;'''
        
        cursor.execute(create_table_query, (idd,))

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

        resultado = [trackid, name, albumid, mediatypeid, genreid, composer, miliseconds, bytess, unitprice, estado, colaborador]
        
        connection.commit()

        mensaje = "La cancion se encontro exitosamente."
        
        print(result)
    except (Exception, psycopg2.DatabaseError) as error :
    
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    return resultado[1]

def buscarGeneroID(idd):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM genre WHERE genreid=%s;'''
        
        cursor.execute(create_table_query, (idd,))

        result = cursor.fetchall()

        idGenero = 0
        nombre = ""
        
        for row in result:
            idGenero = row[0]
            nombre = row[1]
            
        resultado = [idGenero, nombre]
        
        connection.commit()
        
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el genero.", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    return nombre

def buscarGenero(nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM genre WHERE name=%s;'''
        
        cursor.execute(create_table_query, (nombre,))

        result = cursor.fetchall()

        idGenero = 0
        nombre = ""
        
        for row in result:
            idGenero = row[0]
            nombre = row[1]
            
        resultado = [idGenero, nombre]
        
        connection.commit()
        
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el genero.", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    return resultado[0]

################################################################################
#                                     MODIFICAR                                #
################################################################################
def modificarArtista(idd, nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''UPDATE artist SET name =%s WHERE artistid=%s;'''
        
        cursor.execute(create_table_query, (nombre, idd,))            
        
        connection.commit()
        
        mensaje = "Artista modificado con exito."
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo modificar el artista..", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def modificarAlbum(idd, nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''UPDATE album SET title =%s WHERE albumid=%s;'''
        
        cursor.execute(create_table_query, (nombre, idd,))            
        
        connection.commit()
        
        mensaje = "Album modificado con exito."
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo modificar el album..", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


def modificarCancion(idd, nombre, precio):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''UPDATE track SET name =%s, unitprice=%s WHERE trackid=%s;'''
        
        cursor.execute(create_table_query, (nombre, precio, idd,))            
        
        connection.commit()
        
        mensaje = "Cancion modificada con exito."
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo modificar la cancion..", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def modificarRepCancion(idd):
    resultado = buscarCancionPorID(idd)
    numRep = 0
    numRep = resultado[13] + 1
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''UPDATE track SET rep =%s WHERE trackid=%s;'''
        
        cursor.execute(create_table_query, (numRep, idd,))            
        
        connection.commit()
        
        mensaje = "Cancion modificada con exito."
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo modificar la cancion..", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    

def buscarGenero2(nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM genre WHERE name=%s;'''
        
        cursor.execute(create_table_query, (nombre,))

        result = cursor.fetchall()

        idGenero = ""
        nombre = ""
        
        for row in result:
            idGenero = str(row[0])
            nombre = row[1]
            
        resultado = [idGenero, nombre]
        
        connection.commit()
        
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el genero.", title="Consulta fallida")
        print ("No se encontro el genero.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    return resultado

################################################################################
#                                     ELIMINAR                                 #
################################################################################
def eliminarArtista(idd, nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()

    
        create_table_query = '''DELETE FROM artist WHERE artistid=%s;'''
        
        cursor.execute(create_table_query, (idd,))            
        
        connection.commit()

        cursor = connection.cursor()
        
        mensaje = "Artista eliminado con exito."
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo eliminar el artista..", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def eliminarAlbum(idd):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''DELETE FROM album WHERE albumid=%s;'''
        
        cursor.execute(create_table_query, (idd,))            
        
        connection.commit()
        
        mensaje = "Album eliminado con exito."
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo eliminar el album..", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


def eliminarCancion(idd):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''DELETE FROM track WHERE trackid=%s;'''
        
        cursor.execute(create_table_query, (idd,))            
        
        connection.commit()
        
        mensaje = "Cancion eliminada con exito."
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo eliminar la cancion..", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

################################################################################
#                                     INSERTAR                                 #
################################################################################
def insertarArtista(idd, nombre):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''INSERT INTO artist(artistid, name) VALUES(%s, %s);'''
        
        cursor.execute(create_table_query, (idd, nombre,))        
       
        
        connection.commit()
        
        mensaje = "Se registro el artista exitosamente."
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo registrar el artista.", title="Consulta fallida")
        print ("No se pudo registrar artista.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def insertarAlbum(idd, nombre, nombreArtista):
    try:
        bArtista = buscarArtista(nombreArtista)
        idArtista = bArtista[0]
        print(idArtista)
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''INSERT INTO album(albumid, title, artistid) VALUES(%s, %s, %s);'''
        
        cursor.execute(create_table_query, (idd, nombre, idArtista,))        
       
        
        connection.commit()
        
        mensaje = "Se registro el album exitosamente."
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo registrar el album.", title="Consulta fallida")
        print ("No se pudo registrar artista.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def insertarCancion(idd, nombre, nombreAlbum, nombreArtista, genero, precio):
    idAlbum = 1
    bAlbum = buscarAlbum(nombreAlbum)
    idAlbum = bAlbum

    idGenero = 1

    idGenero = buscarGenero(genero)

    print(idGenero)
    print(idAlbum)
        
    mediatypeid = 1
    estado = True
    colaborador = ""
    bytess = randint(100000, 9999999)
    milisegundos = randint(100000, 999999)
    modBy = ""
    modField = ""
    rep = 0
    try:
        
        
           
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''INSERT INTO track(trackid, name, albumid, mediatypeid, genreid, composer, milliseconds, bytes, unitprice, estado, colaborador, modified_by, modified_field, rep) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
        
        cursor.execute(create_table_query, (idd, nombre, idAlbum, mediatypeid, idGenero, nombreArtista, milisegundos, bytess, precio, estado, colaborador, modBy, modField, rep,))        
       
        
        connection.commit()
        
        mensaje = "Se registro la cancion exitosamente."
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo registrar la cancion.", title="Consulta fallida")
        print ("No se pudo registrar la cancion.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


################################################################################
#                                     INACTIVAR                                #
################################################################################
def inactivarCancion(nombre):
    try:
        estado = False
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto1")
        cursor = connection.cursor()
        
        create_table_query = '''UPDATE track SET estado =%s WHERE name=%s;'''
        
        cursor.execute(create_table_query, (estado, nombre,))            
        
        connection.commit()
        
        mensaje = "Cancion inactivar con exito."
        print(mensaje)
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo inactivar la cancion..", title="Consulta fallida")
        print (error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
