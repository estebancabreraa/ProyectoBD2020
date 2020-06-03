import pymongo
import datetime
from tkinter import messagebox
from pprint import pprint
from random import randint
from factura import *
from querys import *

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["proyecto"]

shopping = mydb["shopping-cart"]

compra = mydb["compra"]

tracks = mydb["tracks"]

def insertarCarrito(idCliente, idTrack, subtotal):
    date = datetime.datetime.today()
    mydict = {"idCart": idCliente, "idCliente": idCliente, "date":  date, "idTrack": idTrack, "subtotal": subtotal}
    shopping.insert_one(mydict)
    mensaje = "Cancion insertada en carrito con exito!"
    messagebox.showinfo(message=mensaje, title="Compra")

def insertarCompra(idCliente, tracks, subtotales, total, trackNames):
    date = datetime.datetime.today()
    idCompra = randint(99999, 999999)

    trackList = tracks
    subtotalList = subtotales
    
    for i in range(0, len(tracks)):
        mydict = {"idCompra": idCompra, "idCliente": idCliente, "date": date, "idTrack": tracks[i], "total": str(subtotales[i])}
        compra.insert_one(mydict)

    crearFactura(idCompra, idCliente, trackList, subtotalList, total, trackNames)


def buscarCarrito(idCliente):
    myquery = {"idCliente": idCliente}
    resultado = list(shopping.find(myquery))
    return resultado

def buscarCarritoG():
    resultado = list(shopping.find())
    return resultado

def buscarComprasG():
    resultado = list(compra.find())
    return resultado

def eliminarCarrito(idCliente):
    myquery = {"idCart": idCliente}
    shopping.delete_many(myquery)

def eliminarCompra(idCliente):
    myquery = {"idCliente": idCliente}
    compra.delete_many(myquery)


def queryToList(idCliente):
    myquery = {"idCart": idCliente}
    resultado = shopping.find().pretty()
    return resultado

def checkOut(idCliente):
    trackNames = []
    tracks = []
    subtotals = []
    total = 0

    items = buscarCarrito(idCliente)

    i = 0
    for item in items:
        tracks.append('{0}'.format(item['idTrack']))

        trackName = buscarCancionID(tracks[i])
        
        trackNames.append(trackName)
        print(trackNames[0])

        i = i + 1

    for item in items:
        subtotals.append('{0}'.format(item['subtotal']))
        total = total + float(subtotals[-1])

    insertarCompra(idCliente, tracks, subtotals, total, trackNames)
    
    eliminarCarrito(idCliente)

def verificarCompra(track):
    respuesta = False
    trackInfo = buscarCancion(track)
    idTrack = trackInfo[0]
    myquery = {"idCliente": 1, "idTrack": idTrack} 
    registro = list(compra.find({},{"idCliente": 1, "idTrack": idTrack}))
    pprint(len(registro))
    if len(registro) > 0:
        modificarRepCancion(idTrack)
        respuesta = True
    return respuesta

    
