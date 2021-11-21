import tkinter as tk
from tkinter import messagebox
import json

def getProductData():
    with open("files/productoData.json") as file:
        product = json.load(file)
        return product
producto = getProductData()

def crear_ventana(app):

    def eliminar_producto(array_producto, codigo_producto):
        lst = list(filter(lambda el: el['codigo'] != codigo_producto, array_producto))
        with open("files/productoData.json", "w") as file:
            var = json.dumps(lst, indent=4, sort_keys=True)
            file.write(var)
            file.close()
            messagebox.showinfo(title="Eliminación", message="Producto eliminado correctamente!")
            ventana_ingreso.destroy()

    def elimCliente():
        cod = entry.get()
        client = list(filter(lambda el: cod == el['codigo'], producto))
        if len(client) > 0:
            eliminar_producto(producto, cod)
        else:
            messagebox.showerror(title="ERROR", message="No existe dicho producto!")
        var.set('')

    ventana_ingreso = tk.Toplevel(app)
    ventana_ingreso.geometry("600x150")
    ventana_ingreso.title("Eliminación de Producto")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="Código del Producto")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL CÓDIGO: ", font=('Arial', 18))
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18))
    entry.place(x=280, y=10)

    boton = tk.Button(labelfr, text="ELIMINAR", command=elimCliente, font=('Arial', 15))
    boton.place(x=225, y=65)