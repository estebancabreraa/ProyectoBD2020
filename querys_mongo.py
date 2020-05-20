import pymongo
from tkinter import messagebox

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["proyecto"]

shopping = mydb["shopping-cart"]

compra = mydb["compra"]

def insertarCarrito(idCliente, idTrack, subtotal):
    mydict = {"idCart": idCliente, "idCliente": idCliente, "idTrack": idTrack, "subtotal": subtotal}
    shopping.insert_one(mydict)
    mensaje = "Cancion insertada en carrito con exito!"
    messagebox.showinfo(message=mensaje, title="Consulta")

def buscarCarrito(idCliente):
    myquery = {"idClient": idCliente}
    resultado = shopping.find(myquery)
    return resultado

def buscarCarritoG():
    resultado = shopping.find()
    return resultado

def eliminarCarrito(idCliente):
    myquery = {"idCart": idCliente}
    shopping.delete_many(myquery)
