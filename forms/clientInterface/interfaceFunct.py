import tkinter as tk
from tkinter import messagebox
import json

def getClientData():
    with open("files/clienteData.json") as file:
        client = json.load(file)
        return client
cliente = getClientData()

def crear_ventana(app):

    def vista_cliente(obj):
        vista_cli = tk.Toplevel(app)
        vista_cli.geometry("300x300")

        labelfrcli = tk.LabelFrame(vista_cli, text="Datos del Cliente")
        labelfrcli.pack(fill='both', expand='yes', padx=10, pady=5)

        nom_cli = tk.Label(labelfrcli, text=f"Nombre: {obj['nombre']}", font=('Arial', 12))
        nom_cli.place(x=10, y=10)

        ape_cli = tk.Label(labelfrcli, text=f"Apellido: {obj['apellido']}", font=('Arial', 12))
        ape_cli.place(x=10, y=40)

        cor_cli = tk.Label(labelfrcli, text=f"Correo: {obj['correo']}", font=('Arial', 12))
        cor_cli.place(x=10, y=70)

        loc_cli = tk.Label(labelfrcli, text=f"Localidad: {obj['localidad']}", font=('Arial', 12))
        loc_cli.place(x=10, y=100)

        num_cli = tk.Label(labelfrcli, text=f"Número: {obj['numero']}", font=('Arial', 12))
        num_cli.place(x=10, y=130)

        tel_cli = tk.Label(labelfrcli, text=f"Teléfono: {obj['telefono']}", font=('Arial', 12))
        tel_cli.place(x=10, y=160)

        dni_cli = tk.Label(labelfrcli, text=f"DNI: {obj['dni']}", font=('Arial', 12))
        dni_cli.place(x=10, y=190)

        btn_volver = tk.Button(labelfrcli, text="VOLVER", font=('Arial', 12), command=vista_cli.destroy)
        btn_volver.place(x=100, y=225)

    def consultarCliente():
        num = entry.get()
        client = list(filter(lambda el: num == el['dni'], cliente))
        if len(client) > 0:
            vista_cliente(client[0])
        else:
            messagebox.showerror(title="ERROR", message="No existe dicho cliente!")
        var.set('')

    ventana_ingreso = tk.Toplevel(app)
    ventana_ingreso.geometry("540x150")
    ventana_ingreso.title("Consulta de Cliente")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="Documento del Cliente")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL DNI: ", font=('Arial', 18))
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18))
    entry.place(x=225, y=10)

    boton = tk.Button(labelfr, text="CONSULTAR", command=consultarCliente, font=('Arial', 15))
    boton.place(x=185, y=65)