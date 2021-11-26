import tkinter as tk
from tkinter import messagebox
import json

# FUNCIÓN PARA CARGAR EL ARCHIVO
def getProductData():
    with open("files/productoData.json") as file:
        product = json.load(file)
        return product
producto = getProductData() # EL ARCHIVO SE ALMACENA EN UN OBJETO (DICCIONARIO)

# FUNCIÓN PARA CONSULTAR EL PRODUCTO
def crear_ventana(app):
    from ButtonClass.ButtonClass import ButtonClass
    # FUNCIÓN PARA MOSTRAR LOS DATOS: SE RECIBE EL OBJETO COMO PARÁMETRO Y SE ESCRIBEN SUS ARGUMENTOS EN LABELS
    def vista_Producto(obj):
        vista_produ = tk.Toplevel(app, bg="#030618")
        vista_produ.geometry("400x400")

        labelfrprod = tk.LabelFrame(vista_produ, text="Datos del Producto", bg="#030618", fg="#fff")
        labelfrprod.pack(fill='both', expand='yes', padx=10, pady=5)

        cant_pro = tk.Label(labelfrprod, text=f"Cantidad: {obj['cantidad']}", font=('Arial', 12), bg="#030618", fg="#fff")
        cant_pro.place(x=10, y=10)

        codigo_produ = tk.Label(labelfrprod, text=f"Codigo: {obj['codigo']}", font=('Arial', 12), bg="#030618", fg="#fff")
        codigo_produ.place(x=10, y=40)

        desc_produ = tk.Label(labelfrprod, text=f"Descripcion: {obj['descripcion']}", font=('Arial', 12), bg="#030618", fg="#fff")
        desc_produ.place(x=10, y=70)

        marca = tk.Label(labelfrprod, text=f"Marca: {obj['marca']}", font=('Arial', 12), bg="#030618", fg="#fff")
        marca.place(x=10, y=100)

        nom_produ = tk.Label(labelfrprod, text=f"Nombre: {obj['nombre']}", font=('Arial', 12), bg="#030618", fg="#fff")
        nom_produ.place(x=10, y=130)

        prec_produ = tk.Label(labelfrprod, text=f"Precio: {obj['precio']}", font=('Arial', 12), bg="#030618", fg="#fff")
        prec_produ.place(x=10, y=160)

        stockMax = tk.Label(labelfrprod, text=f"Stock Max: {obj['stockMax']}", font=('Arial', 12), bg="#030618", fg="#fff")
        stockMax.place(x=10, y=190)

        stockMin = tk.Label(labelfrprod, text=f"Stock Min: {obj['stockMin']}", font=('Arial', 12), bg="#030618", fg="#fff")
        stockMin.place(x=10, y=220)

        btn_volver = tk.Button(labelfrprod, image=ButtonClass.btnVolver, borderwidth=0, bg="#030618", command=vista_produ.destroy, highlightthickness = 0, activebackground="#041E2D")
        btn_volver.place(x=100, y=260)

    # FUNCIÓN PARA CONSULTAR LA EXISTENCIA DEL PRODUCTO
    def consultarProducto():
        num = entry.get()
        product = list(filter(lambda el: num == el['codigo'], producto)) # SE FILTRAN LOS REGISTROS CUYO CÓDIGO COINCIDA CON EL INGRESAD
        if len(product) > 0: # SI EXISTE EL PRODUCTO, SE PASA COMO PARÁMETRO A LA FUNCIÓN.
            vista_Producto(product[0])
        else: # SI NO EXISTE, SE MUESTRA UN MSJ. DE ERROR
            messagebox.showerror(title="ERROR", message="No existe dicho Producto!")
        var.set('')

    ventana_ingreso = tk.Toplevel(app, bg="#030618")
    ventana_ingreso.geometry("590x250")
    ventana_ingreso.title("Consulta de Producto")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="Código del Producto", bg="#030618", fg="#fff")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL CÓDIGO: ", font=('Arial', 18), bg="#030618", fg="#fff")
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18), bg="#34495E", fg="#fff")
    entry.place(x=280, y=10)

    boton = tk.Button(labelfr, image=ButtonClass.btnConsultar, command=consultarProducto, bg="#030618", highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
    boton.place(x=195, y=65)