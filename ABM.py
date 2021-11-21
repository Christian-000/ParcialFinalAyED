import tkinter as tk
from tkinter import ttk
from forms import formClient, formProducts, formProviders 
from forms.clientInterface import interfaceFunct
from forms.prodInterface import interfaceProd
from forms.provInterface import interfaceProv


def interfaz_principal():
    frame = tk.Frame(app)
    frame.pack()

    label = tk.Label(frame, text="¡Bienvenido a nuestro Sistema!", font=('Arial', 18))
    label.grid(row=1, column=0, pady=10, columnspan=6)

    boton_registrar = tk.Button(frame, text="Registrar", font=('Arial', 18), command=ventana_registro)
    boton_registrar.grid(row=10, column=2, padx=10, pady=250)

    boton_consultar = tk.Button(frame, text="Consultar", font=('Arial', 18), command=ventana_consulta)
    boton_consultar.grid(row=10, column=3, padx=10, pady=250)

    boton_actualizar = tk.Button(frame, text="Actualizar", font=('Arial', 18))
    boton_actualizar.grid(row=10, column=4, padx=10, pady=250)

    boton_eliminar = tk.Button(frame, text="Eliminar", font=('Arial', 18))
    boton_eliminar.grid(row=10, column=5, padx=10, pady=250)

def ventana_registro():
    nueva_ventana = tk.Toplevel(app)
    nueva_ventana.geometry("630x300")

    label_registro = tk.Label(nueva_ventana, text="Opciones de Registro", font=('Arial', 18))
    label_registro.grid(row=1, column=0, pady=10, columnspan=5, padx=10)

    boton_proveedores = tk.Button(nueva_ventana, text="REGISTRAR\nPROVEEDOR", font=('Arial', 18), command=lambda: formProviders.formulario_proveedor(app))
    boton_proveedores.grid(row=4, column=2, padx=30, pady=25)

    boton_productos = tk.Button(nueva_ventana, text="REGISTRAR\nPRODUCTO", font=('Arial', 18), command=lambda: formProducts.formulario_producto(app))
    boton_productos.grid(row=4, column=3, padx=10, pady=25)

    boton_cliente = tk.Button(nueva_ventana, text="REGISTRAR\nCLIENTE", font=('Arial', 18), command=lambda: formClient.formulario_cliente(app))
    boton_cliente.grid(row=4, column=4, padx=30, pady=25)

    boton_volver = tk.Button(nueva_ventana, text="VOLVER", font=('Arial', 20), command=nueva_ventana.destroy)
    boton_volver.grid(row=6, column=0, padx=10, columnspan=5, pady=5)

def ventana_eliminacion():
    nueva_ventana = tk.Toplevel(app)
    nueva_ventana.geometry("630x300")

    label_registro = tk.Label(nueva_ventana, text="Opciones de Eliminación", font=('Arial', 18))
    label_registro.grid(row=1, column=0, pady=10, columnspan=5, padx=10)

    boton_proveedores = tk.Button(nueva_ventana, text="ELIMINAR\nPROVEEDOR", font=('Arial', 18))
    boton_proveedores.grid(row=4, column=2, padx=30, pady=25)

    boton_productos = tk.Button(nueva_ventana, text="ELIMINAR\n PRODUCTO ", font=('Arial', 18))
    boton_productos.grid(row=4, column=3, padx=10, pady=25)

    boton_cliente = tk.Button(nueva_ventana, text="ELIMINAR\n CLIENTE ", font=('Arial', 18))
    boton_cliente.grid(row=4, column=4, padx=30, pady=25)

    boton_volver = tk.Button(nueva_ventana, text="VOLVER", font=('Arial', 20), command=nueva_ventana.destroy)
    boton_volver.grid(row=6, column=0, padx=5, columnspan=5, pady=5)

def ventana_consulta():
    nueva_ventana = tk.Toplevel(app)
    nueva_ventana.geometry("630x300")

    label_registro = tk.Label(nueva_ventana, text="Opciones de Consulta", font=('Arial', 18))
    label_registro.grid(row=1, column=0, pady=10, columnspan=5, padx=10)

    boton_proveedores = tk.Button(nueva_ventana, text="CONSULTAR\nPROVEEDOR", font=('Arial', 18), command=lambda:interfaceProv.crear_ventana(app))
    boton_proveedores.grid(row=4, column=2, padx=30, pady=25)

    boton_productos = tk.Button(nueva_ventana, text="CONSULTAR\nPRODUCTO", font=('Arial', 18), command=lambda:interfaceProd.crear_ventana(app))
    boton_productos.grid(row=4, column=3, padx=10, pady=25)

    boton_cliente = tk.Button(nueva_ventana, text="CONSULTAR\nCLIENTE", font=('Arial', 18), command=lambda:interfaceFunct.crear_ventana(app))
    boton_cliente.grid(row=4, column=4, padx=30, pady=25)

    boton_volver = tk.Button(nueva_ventana, text="VOLVER", font=('Arial', 20), command=nueva_ventana.destroy)
    boton_volver.grid(row=6, column=0, padx=10, columnspan=5, pady=5)

app = tk.Tk()
app.title('ABM - Clientes, Productos y Proveedores')
app.geometry("600x400")
interfaz_principal()
app.mainloop()