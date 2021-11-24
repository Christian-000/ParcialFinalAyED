import tkinter as tk
from forms import formClient, formProducts, formProviders 
from forms.clientInterface import interfaceFunct, updClient, delClient 
from forms.prodInterface import interfaceProd, updProdu, delProd
from forms.provInterface import interfaceProv, updProv, delProv



def interfaz_principal():
    frame = tk.Frame(app, bg="#27B7CB")
    frame.pack()

    label = tk.Label(frame, text="¡Bienvenido a nuestro Sistema!", font=('Arial', 18), bg="#0A3B58")
    label.grid(row=1, column=0, pady=10, columnspan=6)

    boton_registrar = tk.Button(frame, image=ButtonClass.btnRegistrar, font=('Arial', 18), command=ventana_registro, bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_registrar.grid(row=10, column=2, padx=10, pady=250)

    boton_consultar = tk.Button(frame, image=ButtonClass.btnConsultar, font=('Arial', 18), command=ventana_consulta, bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_consultar.grid(row=10, column=3, padx=10, pady=250)

    boton_actualizar = tk.Button(frame, image=ButtonClass.btnActualizar, font=('Arial', 18), command=ventana_actualizar, bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_actualizar.grid(row=10, column=4, padx=10, pady=250)

    boton_eliminar = tk.Button(frame, image=ButtonClass.btnEliminar, font=('Arial', 18), command=ventana_eliminacion , bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_eliminar.grid(row=10, column=5, padx=10, pady=250)

def ventana_registro():
    nueva_ventana = tk.Toplevel(app)
    nueva_ventana.geometry("630x300")

    label_registro = tk.Label(nueva_ventana, text="Opciones de Registro", font=('Arial', 18), bg="#0A3B58")
    label_registro.grid(row=1, column=0, pady=10, columnspan=5, padx=10)

    boton_proveedores = tk.Button(nueva_ventana, text="REGISTRAR\nPROVEEDOR", font=('Arial', 18), command=lambda: formProviders.formulario_proveedor(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_proveedores.grid(row=4, column=2, padx=30, pady=25)

    boton_productos = tk.Button(nueva_ventana, text="REGISTRAR\nPRODUCTO", font=('Arial', 18), command=lambda: formProducts.formulario_producto(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_productos.grid(row=4, column=3, padx=10, pady=25)

    boton_cliente = tk.Button(nueva_ventana, text="REGISTRAR\nCLIENTE", font=('Arial', 18), command=lambda: formClient.formulario_cliente(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_cliente.grid(row=4, column=4, padx=30, pady=25)

    boton_volver = tk.Button(nueva_ventana, image=ButtonClass.btnVolver, font=('Arial', 20), command=nueva_ventana.destroy, bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_volver.grid(row=6, column=0, padx=10, columnspan=5, pady=5)

def ventana_eliminacion():
    nueva_ventana = tk.Toplevel(app)
    nueva_ventana.geometry("630x300")

    label_registro = tk.Label(nueva_ventana, text="Opciones de Eliminación", font=('Arial', 18), bg="#0A3B58")
    label_registro.grid(row=1, column=0, pady=10, columnspan=5, padx=10)

    boton_proveedores = tk.Button(nueva_ventana, text="ELIMINAR\nPROVEEDOR", font=('Arial', 18), command=lambda:delProv.crear_ventana(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_proveedores.grid(row=4, column=2, padx=30, pady=25)

    boton_productos = tk.Button(nueva_ventana, text="ELIMINAR\n PRODUCTO ", font=('Arial', 18), command=lambda:delProd.crear_ventana(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_productos.grid(row=4, column=3, padx=10, pady=25)

    boton_cliente = tk.Button(nueva_ventana, text="ELIMINAR\n CLIENTE ", font=('Arial', 18), command=lambda:delClient.crear_ventana(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_cliente.grid(row=4, column=4, padx=30, pady=25)

    boton_volver = tk.Button(nueva_ventana, image=ButtonClass.btnVolver, font=('Arial', 20), command=nueva_ventana.destroy, bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_volver.grid(row=6, column=0, padx=5, columnspan=5, pady=5)

def ventana_consulta():
    nueva_ventana = tk.Toplevel(app)
    nueva_ventana.geometry("630x300")

    label_registro = tk.Label(nueva_ventana, text="Opciones de Consulta", font=('Arial', 18), bg="#0A3B58")
    label_registro.grid(row=1, column=0, pady=10, columnspan=5, padx=10)

    boton_proveedores = tk.Button(nueva_ventana, text="CONSULTAR\nPROVEEDOR", font=('Arial', 18), command=lambda:interfaceProv.crear_ventana(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_proveedores.grid(row=4, column=2, padx=30, pady=25)

    boton_productos = tk.Button(nueva_ventana, text="CONSULTAR\nPRODUCTO", font=('Arial', 18), command=lambda:interfaceProd.crear_ventana(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_productos.grid(row=4, column=3, padx=10, pady=25)

    boton_cliente = tk.Button(nueva_ventana, text="CONSULTAR\nCLIENTE", font=('Arial', 18), command=lambda:interfaceFunct.crear_ventana(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_cliente.grid(row=4, column=4, padx=30, pady=25)

    boton_volver = tk.Button(nueva_ventana, image=ButtonClass.btnVolver, font=('Arial', 20), command=nueva_ventana.destroy, bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_volver.grid(row=6, column=0, padx=10, columnspan=5, pady=5)

def ventana_actualizar():
    nueva_ventana = tk.Toplevel(app, bg="#0A3B58")
    nueva_ventana.geometry("630x300")

    label_registro = tk.Label(nueva_ventana, text="Opciones de Actualización", font=('Arial', 18), bg="#0A3B58")
    label_registro.grid(row=1, column=0, pady=10, columnspan=5, padx=10)

    boton_proveedores = tk.Button(nueva_ventana, image=ButtonClass.btnActualizarProveedor, borderwidth=0, command=lambda: updProv.crear_ventana(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness = 0)
    boton_proveedores.grid(row=4, column=2, padx=30, pady=25)

    boton_productos = tk.Button(nueva_ventana, image=ButtonClass.btnActualizarProducto, borderwidth=0, command=lambda: updProdu.crear_ventana(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness=0)
    boton_productos.grid(row=4, column=3, padx=10, pady=25)

    boton_cliente = tk.Button(nueva_ventana, image=ButtonClass.btnActualizarCliente, borderwidth=0, command=lambda: updClient.crear_ventana(app), bg="#0A3B58", activebackground="#041E2D", highlightthickness=0)
    boton_cliente.grid(row=4, column=4, padx=30, pady=25)

    boton_volver = tk.Button(nueva_ventana, borderwidth=0, image=ButtonClass.btnVolver, command=nueva_ventana.destroy, bg="#0A3B58", activebackground="#041E2D", highlightthickness=0)
    boton_volver.grid(row=6, column=0, padx=10, columnspan=5, pady=5)


app = tk.Tk()
app.title('ABM - Clientes, Productos y Proveedores')
app.geometry("600x400")

# btn_one = tk.PhotoImage(file="assets/botonrecortado1.png")
# btn_two = tk.PhotoImage(file="assets/Boton2.png")
from ButtonClass.ButtonClass import ButtonClass
interfaz_principal()


app.mainloop()