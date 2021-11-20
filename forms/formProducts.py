import tkinter as tk
import json

f1 = open("/home/christian/Escritorio/main/ABM_UNI/ParcialFinalAyED/files/productoData.json", "r")
c = f1.read()

file = json.loads(c) #js

def formulario_producto(app):
    codigoData = tk.StringVar()
    nombreData = tk.StringVar()
    precioData = tk.StringVar()
    marcaData = tk.StringVar()
    descripcionData = tk.StringVar()
    cantidadData = tk.StringVar()
    stockMinData = tk.StringVar()
    stockMaxData = tk.StringVar()


    def getInfoProducts():
        nwObjc = {}
        nwObjc['codigo'] = codigoData.get()
        nwObjc['nombre'] = nombreData.get()
        nwObjc['precio'] = precioData.get()
        nwObjc['marca'] = precioData.get()
        nwObjc['descripcion'] = descripcionData.get()
        nwObjc['cantidad'] = cantidadData.get()
        nwObjc['stockMin'] = stockMinData.get()
        nwObjc['stockMax'] = stockMaxData.get()
        f = open("files/productoData.json", "w")
        
        file.append(nwObjc)
        newFile = json.dumps(file, indent=4, sort_keys=True)
        f.write(newFile)
        f.close()
        formulario_producto.destroy()



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