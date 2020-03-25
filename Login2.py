import tkinter as tk
from tkinter import messagebox
from random import randint
from tkinter import Entry
import psycopg2
from psycopg2 import Error

def Login():

    Email = entry2.get()
    password = entry3.get()
    
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto1")
        cursor = connection.cursor()

        create_table_query = '''SELECT * FROM Customer WHERE Email=%s;'''

        cursor.execute(create_table_query, (Email,))

        result = cursor.fetchall()

        contrasena = ""

        for row in result:
            contrasena = row[13]

        if password == contrasena:
            print("Usuario y contraseña correcta")
            
        else:
            print("El email o contraseña es invalido")
            messagebox.showerror(message="Email o contraseña erronea", title="Error")

        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="Email no registrado", title="Consulta fallida")
        print ("Email no registrado", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                messagebox.showerror(message="Email o contraseña erronea", title="Consulta fallida")
                print("PostgreSQL connection is closed")
    
      
def crearUsuario(customerid, firstname, lastname, company, address, city, state, country, postalcode, phone, fax, email, supportrepid, password):
    try:
    
        connection = psycopg2.connect(user = "postgres",
                                      password = "123456",
                                      host = "127.0.0.1",
                                      port = "5433",
                                      database = "proyecto1")
        cursor = connection.cursor()

        create_table_query = '''INSERT INTO Customer(customerid, firstname, lastname, company, address, city, state, country, postalcode, phone, fax, email, supportrepid, password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
            
        cursor.execute(create_table_query, (customerid, firstname, lastname, company, address, city, state, country, postalcode, phone, fax, email, supportrepid, password,))

        connection.commit()
            
        messagebox.showinfo(message="Se ha registrado el cliente exitosamente.", title="Registro")

    
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo registrar cliente.", title="Consulta fallida")
        print ("No se pudo registrar cliente.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def Signup():

    signup = tk.Tk()
    signup.title("Sign Up")
    signup.geometry("800x600")
    signup.configure(background="LightGreen")

    label4= tk.Label(signup, text="Nuevo Usuario", font=("Century", 44), pady=40, bg="LightGreen", fg="black")
    label4.pack()


    #NOMBRE

    nombre = tk.Frame(signup, bg="LightGreen")
    label5 = tk.Label(nombre, text="Nombre: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label5.pack(side=tk.LEFT)

    entry5 = Entry(nombre)
    entry5.pack(side=tk.LEFT)
    nombre.pack(side=tk.TOP, anchor=tk.NW)

    #APELLIDO

    apellido = tk.Frame(signup, bg="LightGreen")
    label6 = tk.Label(apellido, text="Apellido: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label6.pack(side=tk.LEFT)

    entry6 = Entry(apellido)
    entry6.pack(side=tk.LEFT)
    apellido.pack(side=tk.TOP, anchor=tk.NW)

    #COMPAÑIA

    compania = tk.Frame(signup, bg="LightGreen")
    label7 = tk.Label(compania, text="Compañia: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label7.pack(side=tk.LEFT)

    entry7 = Entry(compania)
    entry7.pack(side=tk.LEFT)
    compania.pack(side=tk.TOP, anchor=tk.NW)

    #DIRECCION

    direccion = tk.Frame(signup, bg="LightGreen")
    label8 = tk.Label(direccion, text="Direccion: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label8.pack(side=tk.LEFT)

    entry8 = Entry(direccion)
    entry8.pack(side=tk.LEFT)
    direccion.pack(side=tk.TOP, anchor=tk.NW)

    #CIUDAD

    ciudad = tk.Frame(signup, bg="LightGreen")
    label9 = tk.Label(ciudad, text="Ciudad: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label9.pack(side=tk.LEFT)

    entry9 = Entry(ciudad)
    entry9.pack(side=tk.LEFT)
    ciudad.pack(side=tk.TOP, anchor=tk.NW)

    #ESTADO

    estado = tk.Frame(signup, bg="LightGreen")
    label10 = tk.Label(estado, text="Estado: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label10.pack(side=tk.LEFT)

    entry10 = Entry(estado)
    entry10.pack(side=tk.LEFT)
    estado.pack(side=tk.TOP, anchor=tk.NW)

    #COUNTRY

    pais = tk.Frame(signup, bg="LightGreen")
    label11 = tk.Label(pais, text="Pais: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label11.pack(side=tk.LEFT)

    entry11 = Entry(pais)
    entry11.pack(side=tk.LEFT)
    pais.pack(side=tk.TOP, anchor=tk.NW)

    #CODIGO POSTAL

    codigoPostal = tk.Frame(signup, bg="LightGreen")
    label12 = tk.Label(codigoPostal, text="Codigo Postal: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label12.pack(side=tk.LEFT)

    entry12 = Entry(codigoPostal)
    entry12.pack(side=tk.LEFT)
    codigoPostal.pack(side=tk.TOP, anchor=tk.NW)

    #TELEFONO

    telefono = tk.Frame(signup, bg="LightGreen")
    label13 = tk.Label(telefono, text="Telefono: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label13.pack(side=tk.LEFT)

    entry13 = Entry(telefono)
    entry13.pack(side=tk.LEFT)
    telefono.pack(side=tk.TOP, anchor=tk.NW)

    #FAX

    fac = tk.Frame(signup, bg="LightGreen")
    label14 = tk.Label(fac, text="Fax: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label14.pack(side=tk.LEFT)

    entry14 = Entry(fac)
    entry14.pack(side=tk.LEFT)
    fac.pack(side=tk.TOP, anchor=tk.NW)

    #EMAIL

    correo = tk.Frame(signup, bg="LightGreen")
    label15 = tk.Label(correo, text="Email: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label15.pack(side=tk.LEFT)

    entry15 = Entry(correo)
    entry15.pack(side=tk.LEFT)
    correo.pack(side=tk.TOP, anchor=tk.NW)

    #CONTRASEÑA

    con = tk.Frame(signup, bg="LightGreen")
    label16 = tk.Label(con, text="Contraseña: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label16.pack(side=tk.LEFT)

    entry16 = Entry(con, show = "*")
    entry16.pack(side=tk.LEFT)
    con.pack(side=tk.TOP, anchor=tk.NW)

    #CustumerId

    usuarioId = tk.Frame(signup, bg="LightGreen")
    label17 = tk.Label(usuarioId, text="usuarioId: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label17.pack(side=tk.LEFT)

    entry17 = Entry(usuarioId)
    entry17.pack(side=tk.LEFT)
    usuarioId.pack(side=tk.TOP, anchor=tk.NW)

    #supportrepid

    otroId = tk.Frame(signup, bg="LightGreen")
    label18 = tk.Label(otroId, text="supportrepid: ", font=("Courier", 15), bg="LightGreen", fg="black")
    label18.pack(side=tk.LEFT)

    entry18 = Entry(otroId)
    entry18.pack(side=tk.LEFT)
    otroId.pack(side=tk.TOP, anchor=tk.NW)

    def registrarUsuario():
        fName = entry5.get()
        lName = entry6.get()
        company = entry7.get()
        address = entry8.get()
        city = entry9.get()
        state = entry10.get()
        country = entry11.get()
        postalCode = entry12.get()
        phone = entry13.get()
        fax = entry14.get()
        email = entry15.get()
        password = entry16.get()
        custumerId = entry17.get()
        supportrepid = entry18.get()



        crearUsuario(custumerId, fName, lName, company, address, city, state, country, postalCode, phone, fax, email, supportrepid, password)

    #BOTON REGISTRAR
    
    registrarFrame = tk.Frame(signup, bg = "LightGreen")
    button3 = tk.Button(registrarFrame, text = "SIGN UP", font = ("Courier", 15), command = registrarUsuario)
    button3.pack()
    registrarFrame.pack()



######
# MAIN 
######

gui = tk.Tk()
gui.title("ESPLORIFY")
gui.geometry("800x600")
gui.configure(background = "LightGreen")

label1= tk.Label(gui, text="EXPLORIFY", font=("Century", 44), pady=40, bg="LightGreen", fg="black")
label1.pack()

label2 = tk.Label(gui, text="Email:", font=("Courier", 15), bg="LightGreen")
entry2 = Entry(gui)
label2.pack()
entry2.pack()

label3 = tk.Label(gui, text = "Constraseña:", font=("Courier", 15), bg="LightGreen")
entry3 = Entry(gui, show="*")
label3.pack()
entry3.pack()

button1 = tk.Button(gui, text = "Log In", font=("Courier", 15), command=Login)
button1.pack(pady=10, ipadx=5)

button2 = tk.Button(gui, text="Sing Up", font=("Courier", 15), command=Signup)
button2.pack(pady=10)

gui.mainloop()