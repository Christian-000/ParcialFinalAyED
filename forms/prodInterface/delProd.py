import tkinter as tk
from tkinter import messagebox
import json

# FUNCIÓN PARA CARGAR EL ARCHIVO
def getProductData():
    with open("files/productoData.json") as file:
        product = json.load(file)
        return product
producto = getProductData() # SE ALMACENA EL ARCHIVO EN UN OBJETO

def crear_ventana(app):
    from ButtonClass.ButtonClass import ButtonClass
    # SE RECIBE EL CÓDIGO COMO PARÁMETRO Y SE FILTRAN LOS REGISTROS CUYO DATO NO COINCIDA.
    # SI EXISTE EL PRODUCTO, SE SOBREESCRIBE EL ARCHIVO SIN EL REGISTRO DEL PRODUCTO INGRESADO.
    # SI NO EXISTE, SE MUESTRA UN MSJ. DE ERROR
    def eliminar_producto(array_producto, codigo_producto):
        lst = list(filter(lambda el: el['codigo'] != codigo_producto, array_producto))
        with open("files/productoData.json", "w") as file:
            var = json.dumps(lst, indent=4, sort_keys=True)
            file.write(var)
            file.close()
            messagebox.showinfo(title="Eliminación", message="Producto eliminado correctamente!")
            ventana_ingreso.destroy()

    # FUNCIÓN PARA CONSULTAR LA EXISTENCIA DEL PRODUCTO.
    def elimProducto():
        cod = entry.get()
        client = list(filter(lambda el: cod == el['codigo'], producto))
        if len(client) > 0:
            eliminar_producto(producto, cod)
        else:
            messagebox.showerror(title="ERROR", message="No existe dicho producto!")
        var.set('')

    # CREACIÓN DE LA VENTANA Y LOS WIDGETS
    ventana_ingreso = tk.Toplevel(app, bg="#030618")
    ventana_ingreso.geometry("600x250")
    ventana_ingreso.title("Eliminación de Producto")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="Código del Producto", bg="#030618", fg="#fff")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL CÓDIGO: ", font=('Arial', 18), bg="#030618", fg="#fff")
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18), bg="#34495E", fg="#fff")
    entry.place(x=280, y=10)

    boton = tk.Button(labelfr, image=ButtonClass.btnEliminar, command=elimProducto, bg="#030618", highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
    boton.place(x=173, y=65)