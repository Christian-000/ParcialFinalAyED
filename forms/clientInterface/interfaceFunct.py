import tkinter as tk
from tkinter import messagebox
import json

# FUNCIÓN PARA CARGAR EL ARCHIVO
def getClientData():
    with open("files/clienteData.json") as file:
        client = json.load(file)
        return client
cliente = getClientData() # EL ARCHIVO SE ALMACENA EN UN OBJETO (DICCIONARIO)

# FUNCIÓN PARA CONSULTAR EL CLIENTE
def crear_ventana(app):
    from ButtonClass.ButtonClass import ButtonClass
    # FUNCIÓN PARA MOSTRAR LOS DATOS: SE RECIBE EL OBJETO COMO PARÁMETRO Y SE ESCRIBEN SUS ARGUMENTOS EN LABELS
    def vista_cliente(obj):
        vista_cli = tk.Toplevel(app, bg="#030618")
        vista_cli.geometry("400x400")

        labelfrcli = tk.LabelFrame(vista_cli, text="Datos del Cliente", bg="#030618", fg="#fff")
        labelfrcli.pack(fill='both', expand='yes', padx=10, pady=5)

        nom_cli = tk.Label(labelfrcli, text=f"Nombre: {obj['nombre']}", font=('Arial', 12), bg="#030618", fg="#fff")
        nom_cli.place(x=10, y=10)

        ape_cli = tk.Label(labelfrcli, text=f"Apellido: {obj['apellido']}", font=('Arial', 12), bg="#030618", fg="#fff")
        ape_cli.place(x=10, y=40)

        cor_cli = tk.Label(labelfrcli, text=f"Correo: {obj['correo']}", font=('Arial', 12), bg="#030618", fg="#fff")
        cor_cli.place(x=10, y=70)

        loc_cli = tk.Label(labelfrcli, text=f"Localidad: {obj['localidad']}", font=('Arial', 12), bg="#030618", fg="#fff")
        loc_cli.place(x=10, y=100)

        num_cli = tk.Label(labelfrcli, text=f"Número: {obj['numero']}", font=('Arial', 12), bg="#030618", fg="#fff")
        num_cli.place(x=10, y=130)

        tel_cli = tk.Label(labelfrcli, text=f"Teléfono: {obj['telefono']}", font=('Arial', 12), bg="#030618", fg="#fff")
        tel_cli.place(x=10, y=160)

        dni_cli = tk.Label(labelfrcli, text=f"DNI: {obj['dni']}", font=('Arial', 12), bg="#030618", fg="#fff")
        dni_cli.place(x=10, y=190)

        btn_volver = tk.Button(labelfrcli, image=ButtonClass.btnVolver, borderwidth=0, bg="#030618", command=vista_cli.destroy, highlightthickness = 0, activebackground="#041E2D")
        btn_volver.place(x=100, y=225)

    # FUNCIÓN PARA CONSULTAR LA EXISTENCIA DEL CLIENTE
    def consultarCliente():
        num = entry.get()
        client = list(filter(lambda el: num == el['dni'], cliente)) # SE FILTRAN LOS REGISTROS CUYO DNI COINCIDA CON EL INGRESADO
        if len(client) > 0: # SI EXISTE UN CLIENTE, SE PASA COMO PARÁMETRO A LA FUNCIÓN
            vista_cliente(client[0])
        else: # SI NO EXISTE, SE MUESTRA UN MSJ DE ERROR
            messagebox.showerror(title="ERROR", message="No existe dicho cliente!")
        var.set('')

    # VENTANA DE CONSULTA
    ventana_ingreso = tk.Toplevel(app, bg="#030618")
    ventana_ingreso.geometry("540x250")
    ventana_ingreso.title("Consulta de Cliente")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="Documento del Cliente", bg="#030618", fg="#fff")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL DNI: ", font=('Arial', 18), bg="#030618", fg="#fff")
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18), bg="#34495E", fg="#fff")
    entry.place(x=225, y=10)

    boton = tk.Button(labelfr, image=ButtonClass.btnConsultar, command=consultarCliente, borderwidth=0, bg="#030618", highlightthickness = 0, activebackground="#041E2D")
    boton.place(x=185, y=65)