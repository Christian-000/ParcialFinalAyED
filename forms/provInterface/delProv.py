import tkinter as tk
from tkinter import messagebox
import json

# FUNCIÓN PARA CARGAR EL ARCHIVO
def getProviderData():
    with open("files/proveedorData.json") as file:
        provider = json.load(file)
        return provider
proveedor = getProviderData() # SE ALMACENA EL ARCHIVO EN UN OBJETO.

def crear_ventana(app):
    from ButtonClass.ButtonClass import ButtonClass
    # SE RECIBE EL CUIL COMO PARÁMETRO Y SE FILTRAN LOS REGISTROS CUYO DATO NO COINCIDA.
    # SI EXISTE EL PROVEEDOR, SE SOBREESCRIBE EL ARCHIVO SIN EL REGISTRO DEL PROVEEDOR INGRESADO.
    # SI NO EXISTE, SE MUESTRA UN MSJ. DE ERROR
    def eliminar_producto(array_proveedor, cuil_proveedor):
        lst = list(filter(lambda el: el['cuil'] != cuil_proveedor, array_proveedor))
        with open("files/proveedorData.json", "w") as file:
            var = json.dumps(lst, indent=4, sort_keys=True)
            file.write(var)
            file.close()
            messagebox.showinfo(title="Eliminación", message="Proveedor eliminado correctamente!")
            ventana_ingreso.destroy()

    # FUNCIÓN PARA CONSULTAR LA EXISTENCIA DEL PROVEEDOR
    def elimCliente():
        cuil = entry.get()
        client = list(filter(lambda el: cuil == el['cuil'], proveedor))
        if len(client) > 0:
            eliminar_producto(proveedor, cuil)
        else:
            messagebox.showerror(title="ERROR", message="No existe dicho proveedor!")
        var.set('')

    # CREACIÓN DE LA VENTANA Y SUS WIDGETS
    ventana_ingreso = tk.Toplevel(app, bg="#030618")
    ventana_ingreso.geometry("600x250")
    ventana_ingreso.title("Eliminación de Proveedor")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="CUIL del Proveedor", bg="#030618", fg="#fff")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL CUIL: ", font=('Arial', 18), bg="#030618", fg="#fff")
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18), bg="#34495E", fg="#fff")
    entry.place(x=280, y=10)

    boton = tk.Button(labelfr, image=ButtonClass.btnEliminar, command=elimCliente, bg="#030618", highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
    boton.place(x=173, y=65)