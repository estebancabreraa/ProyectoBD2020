import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
from random import randint
from regArtista import *
from regAlbum import *
from regCancion import *
from inactivar import *
from buscar import *
from reporteria import *

################################################################################
#                                    Comprar                                   #
################################################################################
def ventanaComprar():
    
    compra = tk.Tk()
    compra.title("Comprar")
    compra.geometry("800x700")
    compra.configure(background="LightGreen")



        
   

