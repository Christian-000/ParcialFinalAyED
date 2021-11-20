import tkinter as tk
from tkinter import messagebox
import json

def getClientData():
    with open("files/clienteData.json") as file:
        client = json.load(file)
        return client
cliente = getClientData()

def crear_ventana(app):

    def vista_cliente():
        vista_cli = tk.Toplevel(app)
        vista_cli.geometry("300x300")

        nom_cli = tk.Label(vista_cli, text=f"Nombre: {cliente['nombre']}")
        nom_cli.place(x=10, y=10)

        ape_cli = tk.Label(vista_cli, text=f"Apellido: {cliente['apellido']}")
        ape_cli.place(x=10, y=30)

        # edad_cli = tk.Label(vista_cli, text=f"Edad: {cliente['edad']}")
        # edad_cli.place(x=10, y=50)

        cor_cli = tk.Label(vista_cli, text=f"Correo: {cliente['correo']}")
        cor_cli.place(x=10, y=50)

        loc_cli = tk.Label(vista_cli, text=f"Localidad: {cliente['localidad']}")
        loc_cli.place(x=10, y=70)

        num_cli = tk.Label(vista_cli, text=f"Número: {cliente['numero']}")
        num_cli.place(x=10, y=90)

        tel_cli = tk.Label(vista_cli, text=f"Teléfono: {cliente['telefono']}")
        tel_cli.place(x=10, y=110)

        dni_cli = tk.Label(vista_cli, text=f"DNI: {cliente['dni']}")
        dni_cli.place(x=10, y=130)

    def consultar():
        num = entry.get()
        if num == cliente['dni']:
            vista_cliente()
        else:
            messagebox.showerror(title="ERROR", message="DNI Inválido!")
            
        var.set('')

    ventana_ingreso = tk.Toplevel(app)
    ventana_ingreso.geometry("500x500")

    var = tk.StringVar()

    label = tk.Label(ventana_ingreso, text="INGRESE EL DNI: ")
    label.place(x=10, y=10)

    entry = tk.Entry(ventana_ingreso, textvariable=var)
    entry.place(x=150, y=10)

    boton = tk.Button(ventana_ingreso, text="CONSULTAR", command=consultar)
    boton.place(x=40, y=80)

