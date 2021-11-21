import tkinter as tk
from tkinter import messagebox
import json

def getProviderData():
    with open("files/proveedorData.json") as file:
        provider = json.load(file)
        return provider
proveedor = getProviderData()

def crear_ventana(app):

    def vista_Proveedor(obj):
        vista_prov = tk.Toplevel(app)
        vista_prov.geometry("280x250")

        labelfrprov = tk.LabelFrame(vista_prov, text="Datos del Proveedor")
        labelfrprov.pack(fill='both', expand='yes', padx=10, pady=5)

        codigo_prov = tk.Label(labelfrprov, text=f"Codigo: {obj['codigo']}", font=('Arial', 12))
        codigo_prov.place(x=10, y=10)

        cuil_prov = tk.Label(labelfrprov, text=f"CUIL: {obj['cuil']}", font=('Arial', 12))
        cuil_prov.place(x=10, y=40)

        dom_prov = tk.Label(labelfrprov, text=f"Domicilio: {obj['domicilio']}", font=('Arial', 12))
        dom_prov.place(x=10, y=70)

        rz_prov = tk.Label(labelfrprov, text=f"Razon Social: {obj['razonSocial']}", font=('Arial', 12))
        rz_prov.place(x=10, y=100)

        tel_prov = tk.Label(labelfrprov, text=f"Telefono: {obj['telefono']}", font=('Arial', 12))
        tel_prov.place(x=10, y=130)

        btn_volver = tk.Button(labelfrprov, text="VOLVER", font=('Arial', 12), command=vista_prov.destroy)
        btn_volver.place(x=85, y=170)

    def consultarProveedor():
        num = entry.get()
        provider = list(filter(lambda el: num == el['cuil'], proveedor))
        if len(provider) > 0:
            vista_Proveedor(provider[0])
        else:
            messagebox.showerror(title="ERROR", message="No existe dicho Proveedor!")
        var.set('')

    ventana_ingreso = tk.Toplevel(app)
    ventana_ingreso.geometry("570x150")
    ventana_ingreso.title("Consulta de Proveedor")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="CUIL del Proveedor")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL CUIL: ", font=('Arial', 18))
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18))
    entry.place(x=240, y=10)

    boton = tk.Button(labelfr, text="CONSULTAR", command=consultarProveedor, font=('Arial', 15))
    boton.place(x=195, y=65)