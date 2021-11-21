import tkinter as tk
from tkinter import messagebox
import json

def getProductData():
    with open("files/productoData.json") as file:
        product = json.load(file)
        return product
producto = getProductData()

def crear_ventana(app):
    def vista_Producto(obj):
        vista_produ = tk.Toplevel(app)
        vista_produ.geometry("300x340")

        labelfrprod = tk.LabelFrame(vista_produ, text="Datos del Producto")
        labelfrprod.pack(fill='both', expand='yes', padx=10, pady=5)

        cant_pro = tk.Label(labelfrprod, text=f"Cantidad: {obj['cantidad']}", font=('Arial', 12))
        cant_pro.place(x=10, y=10)

        codigo_produ = tk.Label(labelfrprod, text=f"Codigo: {obj['codigo']}", font=('Arial', 12))
        codigo_produ.place(x=10, y=40)

        desc_produ = tk.Label(labelfrprod, text=f"Descripcion: {obj['descripcion']}", font=('Arial', 12))
        desc_produ.place(x=10, y=70)

        marca = tk.Label(labelfrprod, text=f"Marca: {obj['marca']}", font=('Arial', 12))
        marca.place(x=10, y=100)

        nom_produ = tk.Label(labelfrprod, text=f"Nombre: {obj['nombre']}", font=('Arial', 12))
        nom_produ.place(x=10, y=130)

        prec_produ = tk.Label(labelfrprod, text=f"Precio: {obj['precio']}", font=('Arial', 12))
        prec_produ.place(x=10, y=160)

        stockMax = tk.Label(labelfrprod, text=f"Stock Max: {obj['stockMax']}", font=('Arial', 12))
        stockMax.place(x=10, y=190)

        stockMin = tk.Label(labelfrprod, text=f"Stock Min: {obj['stockMin']}", font=('Arial', 12))
        stockMin.place(x=10, y=220)

        btn_volver = tk.Button(labelfrprod, text="VOLVER", font=('Arial', 12), command=vista_produ.destroy)
        btn_volver.place(x=100, y=260)

    def consultarProducto():
        num = entry.get()
        product = list(filter(lambda el: num == el['codigo'], producto))
        if len(product) > 0:
            vista_Producto(product[0])
        else:
            messagebox.showerror(title="ERROR", message="No existe dicho Producto!")
        var.set('')

    ventana_ingreso = tk.Toplevel(app)
    ventana_ingreso.geometry("590x150")
    ventana_ingreso.title("Consulta de Producto")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="Código del Producto")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL CÓDIGO: ", font=('Arial', 18))
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18))
    entry.place(x=280, y=10)

    boton = tk.Button(labelfr, text="CONSULTAR", command=consultarProducto, font=('Arial', 15))
    boton.place(x=195, y=65)