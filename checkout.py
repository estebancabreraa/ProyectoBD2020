import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from querys_mongo import *

def ventanaCheckout():
    
    checko = tk.Tk()
    checko.title("Check Out")
    checko.geometry("650x300")
    checko.configure(background="LightGreen")

    checkOutFrame = tk.Frame(checko, bg="LightGreen")
    
    label30 = tk.Label(checkOutFrame, text="CHECK OUT", bg="LightGreen", fg="black")
    label30.config(font=("Courier", 24))
    label30.pack(side=tk.TOP, anchor=tk.NW)
    
    titulo = tk.Label(checkOutFrame, text="Carrito:", bg="LightGreen", fg="black")
    titulo.config(font=("Courier", 12))
    titulo.pack(side=tk.LEFT)


    listbox = tk.Listbox(checkOutFrame,  width = 40)
    listbox.pack()


    listado = []
    listado = getCarrito(1)
    items = ""
    for i in range(0, len(listado)):
        item = listado[i]
        listbox.insert("end", item)

    def pagar():
        checkOut(1)
        listbox.delete(0,'end')
    
    def limpiarCarrito():
        listbox.delete(0,'end')
        eliminarCarrito(1)

    button1 = tk.Button(checkOutFrame, text="Pagar", bg="green", command=pagar)
    button1.config(font=("Courier", 20))
    button1.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button2 = tk.Button(checkOutFrame, text="Limpiar Carrito", bg="red", command=limpiarCarrito)
    button2.config(font=("Courier", 20))
    button2.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    checkOutFrame.pack(side=tk.TOP, anchor=tk.NW)

