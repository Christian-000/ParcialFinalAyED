import tkinter as tk
from tkinter import messagebox
import json

def getProviderData():
    with open("files/proveedorData.json") as file:
        provider = json.load(file)
        return provider
proveedor = getProviderData()

def crear_ventana(app):
    from ButtonClass.ButtonClass import ButtonClass
    def vista_Proveedor(obj):
        vista_prov = tk.Toplevel(app, bg="#030618")
        vista_prov.geometry("400x360")

        labelfrprov = tk.LabelFrame(vista_prov, text="Datos del Proveedor", bg="#030618", fg="#fff")
        labelfrprov.pack(fill='both', expand='yes', padx=10, pady=5)

        codigo_prov = tk.Label(labelfrprov, text=f"Codigo: {obj['codigo']}", font=('Arial', 12), bg="#030618", fg="#fff")
        codigo_prov.place(x=10, y=10)

        cuil_prov = tk.Label(labelfrprov, text=f"CUIL: {obj['cuil']}", font=('Arial', 12), bg="#030618", fg="#fff")
        cuil_prov.place(x=10, y=40)

        dom_prov = tk.Label(labelfrprov, text=f"Domicilio: {obj['domicilio']}", font=('Arial', 12), bg="#030618", fg="#fff")
        dom_prov.place(x=10, y=70)

        rz_prov = tk.Label(labelfrprov, text=f"Razon Social: {obj['razonSocial']}", font=('Arial', 12), bg="#030618", fg="#fff")
        rz_prov.place(x=10, y=100)

        tel_prov = tk.Label(labelfrprov, text=f"Telefono: {obj['telefono']}", font=('Arial', 12), bg="#030618", fg="#fff")
        tel_prov.place(x=10, y=130)

        btn_volver = tk.Button(labelfrprov, image=ButtonClass.btnVolver, bg="#030618", command=vista_prov.destroy, borderwidth=0, highlightthickness = 0, activebackground="#041E2D")
        btn_volver.place(x=85, y=170)

    def consultarProveedor():
        num = entry.get()
        provider = list(filter(lambda el: num == el['cuil'], proveedor))
        if len(provider) > 0:
            vista_Proveedor(provider[0])
        else:
            messagebox.showerror(title="ERROR", message="No existe dicho Proveedor!")
        var.set('')

    ventana_ingreso = tk.Toplevel(app, bg="#030618")
    ventana_ingreso.geometry("570x250")
    ventana_ingreso.title("Consulta de Proveedor")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="CUIL del Proveedor", bg="#030618", fg="#fff")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL CUIL: ", font=('Arial', 18), bg="#030618", fg="#fff")
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18), bg="#34495E", fg="#fff")
    entry.place(x=240, y=10)

    boton = tk.Button(labelfr, image=ButtonClass.btnConsultar, command=consultarProveedor, borderwidth=0, highlightthickness=0, bg="#030618", activebackground="#041E2D")
    boton.place(x=195, y=65)