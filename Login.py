import tkinter as tk
from tkinter import messagebox
from random import randint
from tkinter import Entry

def Login():

    Email = entry2.get()
    password = entry3.get()
    
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "esteban1998",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "tiendaFinal")
        cursor = connection.cursor()

        create_table_query = '''SELECT * FROM Customer WHERE Email=%s;'''

        cursor.execute(create_table_query, (Email,))

        result = cursor.fetchall()

        contrasena = ""

        for row in result:
            contrasena = row[13]

        if password == contrasena:
            print("igual")

        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el Email.", title="Consulta fallida")
        print ("No se encontro el Email.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    
      
def crearUsuario(fName, lName, company, address, city, state, country, postalCode, phone, fax, email, support):
    try:
    
        connection = psycopg2.connect(user = "postgres",
                                      password = "esteban1998",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "tiendaFinal")
        cursor = connection.cursor()

        create_table_query = '''INSERT INTO Cliente(fName, lName, company, address, city, state, country, postalCode, phone, fax, email, support) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
            
        cursor.execute(create_table_query, (fName, lName, company, address, city, state, country, postalCode, phone, fax, email, support))
            
        connection.commit()
            
        messagebox.showinfo(message="Se ha registrado el cliente exitosamente.", title="Registro")
    
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo registrar el usuario..", title="Registro fallido")
        print ("No se pudo registrar el usuario.", error)
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
    signup.configure(background="cyan")

    label4 = tk.Label(signup, text="Nuevo Usuario:", font=("Courier", 25), bg="cyan", fg="black")
    label4.pack()

    #NOMBRE

    fName = tk.Frame(signup, bg="cyan")
    label5 = tk.Label(fName, text="Nombre: ", font=("Courier", 15), bg="cyan", fg="black")
    label5.pack(side=tk.LEFT)

    entry5 = Entry(fName)
    entry5.pack(side=tk.LEFT)
    fName.pack(side=tk.TOP, anchor=tk.NW)

    #APELLIDO

    lName = tk.Frame(signup, bg="cyan")
    label6 = tk.Label(lName, text="Apellido: ", font=("Courier", 15), bg="cyan", fg="black")
    label6.pack(side=tk.LEFT)

    entry6 = Entry(lName)
    entry6.pack(side=tk.LEFT)
    lName.pack(side=tk.TOP, anchor=tk.NW)

    #COMPAÑIA

    company = tk.Frame(signup, bg="cyan")
    label7 = tk.Label(company, text="Compañia: ", font=("Courier", 15), bg="cyan", fg="black")
    label7.pack(side=tk.LEFT)

    entry7 = Entry(company)
    entry7.pack(side=tk.LEFT)
    company.pack(side=tk.TOP, anchor=tk.NW)

    #DIRECCION

    direction = tk.Frame(signup, bg="cyan")
    label8 = tk.Label(direction, text="Direccion: ", font=("Courier", 15), bg="cyan", fg="black")
    label8.pack(side=tk.LEFT)

    entry8 = Entry(direction)
    entry8.pack(side=tk.LEFT)
    direction.pack(side=tk.TOP, anchor=tk.NW)

    #CIUDAD

    city = tk.Frame(signup, bg="cyan")
    label9 = tk.Label(city, text="Ciudad: ", font=("Courier", 15), bg="cyan", fg="black")
    label9.pack(side=tk.LEFT)

    entry9 = Entry(city)
    entry9.pack(side=tk.LEFT)
    city.pack(side=tk.TOP, anchor=tk.NW)

    #ESTADO

    state = tk.Frame(signup, bg="cyan")
    label10 = tk.Label(state, text="Estado: ", font=("Courier", 15), bg="cyan", fg="black")
    label10.pack(side=tk.LEFT)

    entry10 = Entry(state)
    entry10.pack(side=tk.LEFT)
    state.pack(side=tk.TOP, anchor=tk.NW)

    #COUNTRY

    country = tk.Frame(signup, bg="cyan")
    label11 = tk.Label(country, text="Pais: ", font=("Courier", 15), bg="cyan", fg="black")
    label11.pack(side=tk.LEFT)

    entry11 = Entry(country)
    entry11.pack(side=tk.LEFT)
    country.pack(side=tk.TOP, anchor=tk.NW)

    #CODIGO POSTAL

    postalCode = tk.Frame(signup, bg="cyan")
    label12 = tk.Label(postalCode, text="Codigo Postal: ", font=("Courier", 15), bg="cyan", fg="black")
    label12.pack(side=tk.LEFT)

    entry12 = Entry(postalCode)
    entry12.pack(side=tk.LEFT)
    postalCode.pack(side=tk.TOP, anchor=tk.NW)

    #TELEFONO

    phone = tk.Frame(signup, bg="cyan")
    label13 = tk.Label(phone, text="Telefono: ", font=("Courier", 15), bg="cyan", fg="black")
    label13.pack(side=tk.LEFT)

    entry13 = Entry(phone)
    entry13.pack(side=tk.LEFT)
    phone.pack(side=tk.TOP, anchor=tk.NW)

    #FAX

    fax = tk.Frame(signup, bg="cyan")
    label14 = tk.Label(fax, text="Fax: ", font=("Courier", 15), bg="cyan", fg="black")
    label14.pack(side=tk.LEFT)

    entry14 = Entry(fax)
    entry14.pack(side=tk.LEFT)
    fax.pack(side=tk.TOP, anchor=tk.NW)

    #EMAIL

    email = tk.Frame(signup, bg="cyan")
    label15 = tk.Label(email, text="Email: ", font=("Courier", 15), bg="cyan", fg="black")
    label15.pack(side=tk.LEFT)

    entry15 = Entry(email)
    entry15.pack(side=tk.LEFT)
    email.pack(side=tk.TOP, anchor=tk.NW)

    #CONTRASEÑA

    supportRepId = tk.Frame(signup, bg="cyan")
    label16 = tk.Label(supportRepId, text="Contraseña: ", font=("Courier", 15), bg="cyan", fg="black")
    label16.pack(side=tk.LEFT)

    entry16 = Entry(supportRepId, show = "*")
    entry16.pack(side=tk.LEFT)
    supportRepId.pack(side=tk.TOP, anchor=tk.NW)
    
    def borrarcampos():
        entry5.delete('1.0', 'end-1c')
        entry6.delete('1.0', 'end-1c')
        entry7.delete('1.0', 'end-1c')
        entry8.delete('1.0', 'end-1c')
        entry9.delete('1.0', 'end-1c')
        entry10.delete('1.0', 'end-1c')
        entry11.delete('1.0', 'end-1c')
        entry12.delete('1.0', 'end-1c')
        entry13.delete('1.0', 'end-1c')
        entry14.delete('1.0', 'end-1c')
        entry15.delete('1.0', 'end-1c')
        entry16.delete('1.0', 'end-1c')

    def registrarUsuario():
        fName = entry5.get("1.0",'end-1c')
        lName = entry6.get("1.0",'end-1c')
        company = entry7.get("1.0",'end-1c')
        address = entry8.get("1.0",'end-1c')
        city = entry9.get("1.0",'end-1c')
        state = entry10.get("1.0",'end-1c')
        country = entry11.get("1.0",'end-1c')
        postalCode = entry12.get("1.0",'end-1c')
        phone = entry13.get("1.0",'end-1c')
        fax = entry14.get("1.0",'end-1c')
        email = entry15.get("1.0",'end-1c')
        support = entry16.get("1.0",'end-1c')

        crearUsuario(fName, lName, company, address, city, state, country, postalCode, phone, fax, email, support)

        borrarCampos()
        print(fName)
    #BOTON REGISTRAR
    
    registrarFrame = tk.Frame(signup, bg = "cyan")
    button3 = tk.Button(registrarFrame, text = "SIGN UP", font = ("Courier", 15), command = registrarUsuario)
    button3.pack()
    registrarFrame.pack()



######
# MAIN 
######

gui = tk.Tk()
gui.title("EXPLORIFY")
gui.geometry("800x600")
gui.configure(background = "cyan")

label1= tk.Label(gui, text="EXPLORIFY", bg="cyan", fg="black")
label1.config(font=("Courier", 44), pady=40)
label1.pack()

label2 = tk.Label(gui, text="Email:", font=("Courier", 15), bg="cyan")
entry2 = Entry(gui)
label2.pack()
entry2.pack()

label3 = tk.Label(gui, text = "Constraseña:", font=("Courier", 15), bg="cyan")
entry3 = Entry(gui, show="*")
label3.pack()
entry3.pack()

button1 = tk.Button(gui, text = "Log In", command=Login)
button1.config(font=("courier", 15))
button1.pack(pady=10, ipadx=5)

button2 = tk.Button(gui, text="Sing Up", command=Signup)
button2.config(font=("Courier", 15))
button2.pack(pady=10)

gui.mainloop()