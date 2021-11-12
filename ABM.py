import tkinter as tk
from tkinter import ttk


# JSON DEL PROVEEDOR
proveedorData = {
    "codigo": "",
    "cuil": "",
    "razonSocial": "",
    "domicilio": "",
    "telefono": ""
}


#JSON DEL CLIENTE
clienteData = {
    "numero": "",
    "nombre": "",
    "apellido": "",
    "localidad": "",
    "correo": "",
    "domicilio": "",
    "dni": "",
    "telefono": "",
}


#JSON DEL PRODUCTO
productoData = {
    'codigo': '',
    'nombre': '',
    'precio': '',
    'marca': '',
    'descripcion': '',
    'cantidad': '',
    'stockMin': '',
    'stockMax': ''
}





def interfaz_principal():
    frame = tk.Frame(app)
    frame.pack()

    label = tk.Label(frame, text="¡Bienvenido a nuestro Sistema!", font=('Arial', 18))
    label.grid(row=1, column=0, pady=10, columnspan=6)

    boton_registrar = tk.Button(frame, text="Registrar", font=('Arial', 18), command=ventana_registro)
    boton_registrar.grid(row=10, column=2, padx=10, pady=250)

    boton_consultar = tk.Button(frame, text="Consultar", font=('Arial', 18))
    boton_consultar.grid(row=10, column=3, padx=10, pady=250)

    boton_actualizar = tk.Button(frame, text="Actualizar", font=('Arial', 18))
    boton_actualizar.grid(row=10, column=4, padx=10, pady=250)

    boton_eliminar = tk.Button(frame, text="Eliminar", font=('Arial', 18))
    boton_eliminar.grid(row=10, column=5, padx=10, pady=250)


def ventana_registro():
    nueva_ventana = tk.Toplevel(app)
    nueva_ventana.geometry("600x400")

    label_registro = tk.Label(nueva_ventana, text="Opciones de Registro", font=('Arial', 18))
    label_registro.grid(row=1, column=0, pady=10, columnspan=5, padx=10)

    boton_proveedores = tk.Button(nueva_ventana, text="REGISTRAR\nPROVEEDOR", font=('Arial', 18), command=formulario_proveedor)
    boton_proveedores.grid(row=10, column=2, padx=10, pady=250)

    boton_productos = tk.Button(nueva_ventana, text="REGISTRAR \n PRODUCTO", font=('Arial', 18), command=formulario_producto)
    boton_productos.grid(row=10, column=3, padx=10, pady=250)

    boton_cliente = tk.Button(nueva_ventana, text="REGISTRAR\nCLIENTE", font=('Arial', 18), command=formulario_cliente)
    boton_cliente.grid(row=10, column=4, padx=10, pady=250)


def formulario_proveedor():

    codigoP = tk.StringVar()
    cuilData = tk.StringVar()
    razonSocialData = tk.StringVar()
    domicilioData = tk.StringVar()
    telefonoData = tk.IntVar()
    def getInfoProveedor():
        proveedorData["codigo"] = codigoP.get()
        proveedorData["cuil"] = cuilData.get() 
        proveedorData["razonSocial"] = razonSocialData.get() 
        proveedorData["domicilio"] = domicilioData.get() 
        proveedorData["telefono"] = telefonoData.get() 


    formulario_proveedor = tk.Toplevel(app)
    formulario_proveedor.geometry("475x400")

    label_formulario_proveedor = tk.Label(formulario_proveedor, text="Información del Proveedor:", font=('Arial', 18))
    label_formulario_proveedor.grid(row=0, column=0, columnspan=2, pady=10)

    codigo_p = tk.Label(formulario_proveedor, text="Código: ", font=('Arial', 14))
    codigo_p.grid(row=1, column=0, pady=10, padx=10)

    cuil_p = tk.Label(formulario_proveedor, text="CUIl:", font=('Arial', 14))
    cuil_p.grid(row=2, column=0, pady=10, padx=10)

    razon_social = tk.Label(formulario_proveedor, text="Razón social:", font=('Arial', 14))
    razon_social.grid(row=3, column=0, pady=10, padx=10)

    domicilio = tk.Label(formulario_proveedor, text="Domicilio:", font=('Arial', 14))
    domicilio.grid(row=4, column=0, pady=10, padx=10)

    telefono = tk.Label(formulario_proveedor, text="Teléfono:", font=('Arial', 14))
    telefono.grid(row=5, column=0, pady=10, padx=10)

    entry_codigop = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=codigoP)
    entry_codigop.grid(row=1, column=1)

    entry_cuil = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=cuilData)
    entry_cuil.grid(row=2, column=1)

    entry_rs = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=razonSocialData)
    entry_rs.grid(row=3, column=1)

    entry_dom = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=domicilioData)
    entry_dom.grid(row=4, column=1)

    entry_tel = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=telefonoData)
    entry_tel.grid(row=5, column=1)

    boton_hecho = tk.Button(formulario_proveedor, text="Hecho", font=('Arial', 18), command=getInfoProveedor)
    boton_hecho.grid(row=6, column=1, pady=10)

    boton_volver = tk.Button(formulario_proveedor, text="Volver", font=('Arial', 18), command=formulario_proveedor.destroy)
    boton_volver.grid(row=6, column=0, pady=10)



def formulario_cliente():
    numClienteData = tk.StringVar()
    nombreData = tk.StringVar()
    apellidoData= tk.StringVar()
    localidadData= tk.StringVar()
    correoData= tk.StringVar()
    domicilioData= tk.StringVar()
    dniData= tk.StringVar()
    telefonoData = tk.StringVar()
        
    def getInfoCliente():
        clienteData['numero'] = numClienteData.get()
        clienteData['nombre'] = nombreData.get()
        clienteData['apellido'] = apellidoData.get()
        clienteData['localidad'] = localidadData.get()
        clienteData['correo'] = correoData.get()
        clienteData['domicilio'] = domicilioData.get()
        clienteData['dni'] = dniData.get()
        clienteData['telefono'] = telefonoData.get()
        print(clienteData)
        


    formulario_cliente = tk.Toplevel(app)
    formulario_cliente.geometry("475x550")

    label_formulario_cliente = tk.Label(formulario_cliente, text="Información del Cliente:", font=('Arial', 18))
    label_formulario_cliente.grid(row=0, column=0, columnspan=2, pady=10)

    numero_cliente = tk.Label(formulario_cliente, text="Número:", font=('Arial', 14))
    numero_cliente.grid(row=1, column=0, pady=10, padx=10)

    nombre_cliente = tk.Label(formulario_cliente, text="Nombre:", font=('Arial', 14))
    nombre_cliente.grid(row=2, column=0, pady=10, padx=10)

    apellido_cliente = tk.Label(formulario_cliente, text="Apellido:", font=('Arial', 14))
    apellido_cliente.grid(row=3, column=0, pady=10, padx=10)

    localidad_cliente = tk.Label(formulario_cliente, text="Localidad:", font=('Arial', 14))
    localidad_cliente.grid(row=4, column=0, pady=10, padx=10)

    correo_cliente = tk.Label(formulario_cliente, text="Correo:", font=('Arial', 14))
    correo_cliente.grid(row=5, column=0, pady=10, padx=10)

    domicilio_cliente = tk.Label(formulario_cliente, text="Domicilio:", font=('Arial', 14))
    domicilio_cliente.grid(row=6, column=0, pady=10, padx=10)

    DNI_cliente = tk.Label(formulario_cliente, text="Documento:", font=('Arial', 14))
    DNI_cliente.grid(row=7, column=0, pady=10, padx=10)

    telefono_cliente = tk.Label(formulario_cliente, text="Teléfono:", font=('Arial', 14))
    telefono_cliente.grid(row=8, column=0, pady=10, padx=10)

    entry_numero = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=numClienteData)
    entry_numero.grid(row=1, column=1)

    entry_nombre = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=nombreData)
    entry_nombre.grid(row=2, column=1)

    entry_apellido = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=apellidoData)
    entry_apellido.grid(row=3, column=1)

    entry_localidad = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=localidadData)
    entry_localidad.grid(row=4, column=1)

    entry_correo = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=correoData)
    entry_correo.grid(row=5, column=1)

    entry_domicilio = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=domicilioData)
    entry_domicilio.grid(row=6, column=1)

    entry_dni = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=dniData)
    entry_dni.grid(row=7, column=1)

    entry_tel = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=telefonoData)
    entry_tel.grid(row=8, column=1)

    boton_hecho = tk.Button(formulario_cliente, text="Hecho", font=('Arial', 18), command=getInfoCliente)
    boton_hecho.grid(row=9, column=1, pady=10)

    boton_volver = tk.Button(formulario_cliente, text="Volver", font=('Arial', 18), command=formulario_cliente.destroy)
    boton_volver.grid(row=9, column=0, pady=10)




def formulario_producto():
    codigoData = tk.StringVar()
    nombreData = tk.StringVar()
    precioData = tk.StringVar()
    marcaData = tk.StringVar()
    descripcionData = tk.StringVar()
    cantidadData = tk.StringVar()
    stockMinData = tk.StringVar()
    stockMaxData = tk.StringVar()


    def getInfoProducts():
        productoData['codigo'] = codigoData.get()
        productoData['nombre'] = nombreData.get()
        productoData['precio'] = precioData.get()
        productoData['marca'] = precioData.get()
        productoData['descripcion'] = descripcionData.get()
        productoData['cantidad'] = cantidadData.get()
        productoData['stockMin'] = stockMinData.get()
        productoData['stockMax'] = stockMaxData.get()
        print(productoData)



    formulario_producto = tk.Toplevel(app)
    formulario_producto.geometry("475x550")

    label_formulario_producto = tk.Label(formulario_producto, text="Información del Producto:", font=('Arial', 18))
    label_formulario_producto.grid(row=0, column=0, columnspan=2, pady=10)

    codigo_producto = tk.Label(formulario_producto, text="Código:", font=('Arial', 14))
    codigo_producto.grid(row=1, column=0, pady=10, padx=10)

    nombre_producto = tk.Label(formulario_producto, text="Nombre:", font=('Arial', 14))
    nombre_producto.grid(row=2, column=0, pady=10, padx=10)

    precio_producto = tk.Label(formulario_producto, text="Precio:", font=('Arial', 14))
    precio_producto.grid(row=3, column=0, pady=10, padx=10)

    marca_producto = tk.Label(formulario_producto, text="Marca:", font=('Arial', 14))
    marca_producto.grid(row=4, column=0, pady=10, padx=10)

    desc_producto = tk.Label(formulario_producto, text="Descripción:", font=('Arial', 14))
    desc_producto.grid(row=5, column=0, pady=10, padx=10)

    cant_producto = tk.Label(formulario_producto, text="Cantidad:", font=('Arial', 14))
    cant_producto.grid(row=6, column=0, pady=10, padx=10)

    stock_min = tk.Label(formulario_producto, text="Stock mínimo:", font=('Arial', 14))
    stock_min.grid(row=7, column=0, pady=10, padx=10)

    stock_max = tk.Label(formulario_producto, text="Stock máximo:", font=('Arial', 14))
    stock_max.grid(row=8, column=0, pady=10, padx=10)

    entry_codigo = tk.Entry(formulario_producto, font=('Arial', 14), textvariable=codigoData)
    entry_codigo.grid(row=1, column=1)

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

    boton_hecho = tk.Button(formulario_producto, text="Hecho", font=('Arial', 18), command=getInfoProducts)
    boton_hecho.grid(row=9, column=1, pady=10)

    boton_volver = tk.Button(formulario_producto, text="Volver", font=('Arial', 18), command=formulario_producto.destroy)
    boton_volver.grid(row=9, column=0, pady=10)

app = tk.Tk()
app.title('ABM - Clientes, Productos y Proveedores')
app.geometry("600x400")
interfaz_principal()
app.mainloop()