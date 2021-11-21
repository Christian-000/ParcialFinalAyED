import tkinter as tk
from tkinter import messagebox
import json

def getProviderData():
    with open("files/proveedorData.json") as file:
        provider = json.load(file)
        return provider
proveedor = getProviderData()

def crear_ventana(app):

    def eliminar_producto(array_proveedor, cuil_proveedor):
        lst = list(filter(lambda el: el['cuil'] != cuil_proveedor, array_proveedor))
        with open("files/proveedorData.json", "w") as file:
            var = json.dumps(lst, indent=4, sort_keys=True)
            file.write(var)
            file.close()
            messagebox.showinfo(title="Eliminación", message="Proveedor eliminado correctamente!")
            ventana_ingreso.destroy()

    def elimCliente():
        cuil = entry.get()
        client = list(filter(lambda el: cuil == el['cuil'], proveedor))
        if len(client) > 0:
            eliminar_producto(proveedor, cuil)
        else:
            messagebox.showerror(title="ERROR", message="No existe dicho proveedor!")
        var.set('')

    ventana_ingreso = tk.Toplevel(app)
    ventana_ingreso.geometry("600x150")
    ventana_ingreso.title("Eliminación de Proveedor")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="CUIL del Proveedor")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL CUIL: ", font=('Arial', 18))
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18))
    entry.place(x=280, y=10)

    boton = tk.Button(labelfr, text="ELIMINAR", command=elimCliente, font=('Arial', 15))
    boton.place(x=225, y=65)