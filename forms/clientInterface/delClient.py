import tkinter as tk
from tkinter import messagebox
import json

def getClientData():
    with open("files/clienteData.json") as file:
        client = json.load(file)
        return client
cliente = getClientData()

def crear_ventana(app):
    from ButtonClass.ButtonClass import ButtonClass
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

    ventana_ingreso = tk.Toplevel(app, bg="#030618")
    ventana_ingreso.geometry("540x250")
    ventana_ingreso.title("Eliminación de Cliente")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="Documento del Cliente", bg="#030618", fg="#fff")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL DNI: ", font=('Arial', 18), bg="#030618", fg="#fff")
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18), bg="#34495E", fg="#fff")
    entry.place(x=225, y=10)

    boton = tk.Button(labelfr, image=ButtonClass.btnEliminar, command=elimCliente, bg="#030618", highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
    boton.place(x=140, y=65)