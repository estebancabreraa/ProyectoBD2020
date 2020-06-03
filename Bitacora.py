import csv
import psycopg2
from psycopg2 import Error
from random import randint
from tkinter import messagebox


def createCSV(filename):
    nombreArchivo = open(filename, "w")
    nombreArchivo.close()
    
def listFile(lista, filename,lista2):
    with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerow(lista2) 
            writer.writerows(lista)

try:  
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto2")
        cursor = connection.cursor()
        
        create_table_query = '''select * from bitacora'''
        
        cursor.execute(create_table_query)

        result = cursor.fetchall()

        createCSV("bitacora.csv")
        listFile(result, "bitacora.csv", ["date", "hour", "usuario", "tipo modificacion", "campo", "tabla"])
        
        for row in result:
            print("date =", row[0],)
            print("hour =" , row[1], )
            print("user =" , row[2], )
            print("type =" , row[3], )
            print("field =" , row[4], )
            print("table =" , row[5], )
        
        connection.commit()                 
        
       
finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")




def createCSV(filename):
    nombreArchivo = open(filename, "w")
    nombreArchivo.close()
