import json
import tkinter as tk

# FUNCIÓN PARA CARGAR EL ARCHIVO
def getProductData():
    with open("files/productoData.json") as file:
        product = json.load(file)
        return product
producto = getProductData() # EL ARCHIVO SE ALMACENA EN UN OBJETO

def crear_ventana(app):
    from ButtonClass.ButtonClass import ButtonClass
    # FUNCIÓN PARA ACTUALIZAR ARCHIVO: LA FUNCIÓN RECIBE EL ELEMENTO FILTRADO COMO PARÁMETRO
    # GUARDA SU CÓDIGO, Y ABRE UN FORMULARIO PARA QUE SE INGRESEN LOS DEMÁS DATOS.
    def formulario_producto(app, arrProdu):
        nombreData = tk.StringVar()
        precioData = tk.StringVar()
        marcaData = tk.StringVar()
        descripcionData = tk.StringVar()
        cantidadData = tk.StringVar()
        stockMinData = tk.StringVar()
        stockMaxData = tk.StringVar()
            
        # FUNCIÓN PARA OBTENER LOS DATOS DE LOS CAMPOS DE TEXTO Y ALMACENARLOS EN EL ARCHIVO.     
        def getInfoProducts(arrProdu):
            arrProdu[0]['nombre'] = nombreData.get()
            arrProdu[0]['precio'] = precioData.get()
            arrProdu[0]['marca'] = marcaData.get()
            arrProdu[0]['descripcion'] = descripcionData.get()
            arrProdu[0]['cantidad'] = cantidadData.get()
            arrProdu[0]['stockMin'] = stockMinData.get()
            arrProdu[0]['stockMax'] = stockMaxData.get()
            f = open("files/productoData.json", "w")
            
            newFile = json.dumps(producto, indent=4, sort_keys=True)
            
            f.write(newFile)
            f.close()
            formulario_producto.destroy()


        formulario_producto = tk.Toplevel(app, bg="#030618")
        formulario_producto.geometry("500x550")

        label_formulario_producto = tk.Label(formulario_producto, text="Información del Producto:", font=('Arial', 18), bg="#030618", fg="#fff")
        label_formulario_producto.grid(row=0, column=0, columnspan=2, pady=10)

        nombre_producto = tk.Label(formulario_producto, text="Nombre:", font=('Arial', 14), bg="#030618", fg="#fff")
        nombre_producto.grid(row=2, column=0, pady=10, padx=10)

        precio_producto = tk.Label(formulario_producto, text="Precio:", font=('Arial', 14), bg="#030618", fg="#fff")
        precio_producto.grid(row=3, column=0, pady=10, padx=10)

        marca_producto = tk.Label(formulario_producto, text="Marca:", font=('Arial', 14), bg="#030618", fg="#fff")
        marca_producto.grid(row=4, column=0, pady=10, padx=10)

        desc_producto = tk.Label(formulario_producto, text="Descripción:", font=('Arial', 14), bg="#030618", fg="#fff")
        desc_producto.grid(row=5, column=0, pady=10, padx=10)

        cant_producto = tk.Label(formulario_producto, text="Cantidad:", font=('Arial', 14), bg="#030618", fg="#fff")
        cant_producto.grid(row=6, column=0, pady=10, padx=10)

        stock_min = tk.Label(formulario_producto, text="Stock mínimo:", font=('Arial', 14), bg="#030618", fg="#fff")
        stock_min.grid(row=7, column=0, pady=10, padx=10)

        stock_max = tk.Label(formulario_producto, text="Stock máximo:", font=('Arial', 14), bg="#030618", fg="#fff")
        stock_max.grid(row=8, column=0, pady=10, padx=10)


        entry_nombre = tk.Entry(formulario_producto, font=('Arial', 14), textvariable=nombreData)
        entry_nombre.grid(row=2, column=1)

        entry_precio = tk.Entry(formulario_producto, font=('Arial', 14), textvariable=precioData)
        entry_precio.grid(row=3, column=1)

        entry_marca = tk.Entry(formulario_producto, font=('Arial', 14), textvariable=marcaData)
        entry_marca.grid(row=4, column=1)

        entry_desc = tk.Entry(formulario_producto, font=('Arial', 14), textvariable=descripcionData)
        entry_desc.grid(row=5, column=1)

        entry_cant = tk.Entry(formulario_producto, font=('Arial', 14), textvariable=cantidadData)
        entry_cant.grid(row=6, column=1)

        entry_stockmin = tk.Entry(formulario_producto, font=('Arial', 14), textvariable=stockMinData)
        entry_stockmin.grid(row=7, column=1)

        entry_stockmax = tk.Entry(formulario_producto, font=('Arial', 14), textvariable=stockMaxData)
        entry_stockmax.grid(row=8, column=1)

        boton_hecho = tk.Button(formulario_producto, image=ButtonClass.btnConfirmar, bg="#030618", command=lambda: getInfoProducts(arrProdu), highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
        boton_hecho.grid(row=9, column=1, pady=10)

        boton_volver = tk.Button(formulario_producto, image=ButtonClass.btnVolver, bg="#030618", command=formulario_producto.destroy, highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
        boton_volver.grid(row=9, column=0, pady=10)

    # FUNCIÓN PARA CONSULTAR LA EXISTENCIA DEL PRODUCTO
    def consultarProducto(app):
        num = entry.get()
        product = list(filter(lambda el: num == el['codigo'], producto)) # SE FILTRAN LOS ELEMENTOS CUYO CÓDIGO COINCIDA CON EL INGRESADO
        if len(product) > 0: # SI EXISTE EL PRODUCTO, SE ENVÍA EL REGISTRO COMO PARÁMETRO A LA FUNCIÓN
            formulario_producto(app, product)
        else: # SI NO EXISTE, SE MUESTRA UN MSJ. DE ERROR
            tk.messagebox.showerror(title="ERROR", message="No existe dicho Producto!")
        var.set('')

    # CREACIÓN DE LA VENTANA Y SUS WIDGETS
    ventana_ingreso = tk.Toplevel(app, bg="#030618")
    ventana_ingreso.geometry("590x250")
    ventana_ingreso.title("Actualización de Producto")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="Código del Producto", bg="#030618", fg="#fff")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL CÓDIGO: ", font=('Arial', 18), bg="#030618", fg="#fff")
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18), bg="#34495E", fg="#fff")
    entry.place(x=280, y=10)

    boton = tk.Button(labelfr, image=ButtonClass.btnConsultar, command=lambda: consultarProducto(app), bg="#030618", highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
    boton.place(x=195, y=65)

