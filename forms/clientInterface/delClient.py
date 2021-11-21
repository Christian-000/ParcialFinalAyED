import tkinter as tk
from tkinter import messagebox
import json

def getClientData():
    with open("files/clienteData.json") as file:
        client = json.load(file)
        return client
cliente = getClientData()

def crear_ventana(app):

    def eliminar_cliente(array_cliente, numero_dni):
        lst = list(filter(lambda el: el['dni'] != numero_dni, array_cliente))
        with open("files/clienteData.json", "w") as file:
            var = json.dumps(lst, indent=4, sort_keys=True)
            file.write(var)
            file.close()
            messagebox.showinfo(title="Eliminación", message="¡Cliente eliminado correctamente!")
            ventana_ingreso.destroy()

    def elimCliente():
        num = entry.get()
        client = list(filter(lambda el: num == el['dni'], cliente))
        if len(client) > 0:
            eliminar_cliente(cliente, num)
        else:
            messagebox.showerror(title="ERROR", message="No existe dicho cliente!")
        var.set('')

    ventana_ingreso = tk.Toplevel(app)
    ventana_ingreso.geometry("540x150")
    ventana_ingreso.title("Eliminación de Cliente")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="Documento del Cliente")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL DNI: ", font=('Arial', 18))
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18))
    entry.place(x=225, y=10)

    boton = tk.Button(labelfr, text="ELIMINAR", command=elimCliente, font=('Arial', 15))
    boton.place(x=185, y=65)