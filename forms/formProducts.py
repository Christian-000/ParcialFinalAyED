import tkinter as tk
from tkinter import messagebox
import json

f1 = open("files/productoData.json", "r")
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

    def validate(obj):
        count = 0
        stockMin = 0;
        stockMax = stockMin + 1
        if(obj["cantidad"].isdigit()):
            pass
        else:
            messagebox.showerror("Cantidad Invalida", "Debes poner un valor numerico")
            count += 1

        if(obj["codigo"].isdigit()):
            pass
        else:
            messagebox.showerror("Codigo Invalido", "Debes poner un valor numerico.")
            count += 1


        if(obj["marca"].isalpha()):
            pass
        else:
            messagebox.showerror("Marca Invalida", "No se puede incluir Simbolos o Numeros en la Marca.")
            count += 1

        if(obj["nombre"].isalpha()):
            pass
        else:
            messagebox.showerror("Nombre Invalido", "El nombre no puede contener Numeros o Simbolos.")
            count += 1

        if(obj["precio"].isdigit()):
            pass
        else:
            if(obj["precio"]): 
                if(int(obj["precio"]) < 0):
                    messagebox.showerror("Precio Invalido", "El precio no puede ser menor a 0")
                    count += 1
            else:
                messagebox.showerror("Precio Invalido", "El precio debe estar compuesto unicamente por numeros.")
                count += 1

        if(obj["stockMin"].isdigit()):
            stockMin = int(obj["stockMin"])
        else:
            messagebox.showerror("Stock Minimo Invalido", "El Stock Minimo debe ser numerico.")
            count += 1

        if(obj["stockMax"].isdigit()):
            stockMax = int(obj["stockMax"])
            if(stockMin > stockMax):
                messagebox.showerror("Stock Maximo Invalido", "El Stock Maximo debe ser Mayor o Igual al Stock Minimo.")
                count += 1
        else:
            messagebox.showerror("Stock Maximo Invalido", "El Stock Maximo debe ser numerico.")
            count += 1

        if(count > 0):
            messagebox.showerror("ERROR", "Hay datos invalidos en el formulario.")
            formulario_producto.destroy()


        else:
            f = open("files/productoData.json", "w")
            
            file.append(obj)
            newFile = json.dumps(file, indent=4, sort_keys=True)
            f.write(newFile)
            f.close()
            formulario_producto.destroy()


    def getInfoProducts():
        nwObjc = {}
        nwObjc['codigo'] = codigoData.get()
        nwObjc['nombre'] = nombreData.get()
        nwObjc['precio'] = precioData.get()
        nwObjc['marca'] = marcaData.get()
        nwObjc['descripcion'] = descripcionData.get()
        nwObjc['cantidad'] = cantidadData.get()
        nwObjc['stockMin'] = stockMinData.get()
        nwObjc['stockMax'] = stockMaxData.get()
        validate(nwObjc)
        



    formulario_producto = tk.Toplevel(app, bg="#030618")
    formulario_producto.geometry("500x550")

    from ButtonClass.ButtonClass import ButtonClass

    label_formulario_producto = tk.Label(formulario_producto, text="Información del Producto:", font=('Arial', 18), bg="#030618", fg="#fff")
    label_formulario_producto.grid(row=0, column=0, columnspan=2, pady=10)

    codigo_producto = tk.Label(formulario_producto, text="Código:", font=('Arial', 14), bg="#030618", fg="#fff")
    codigo_producto.grid(row=1, column=0, pady=10, padx=10)

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

    boton_hecho = tk.Button(formulario_producto, image=ButtonClass.btnConfirmar, bg="#030618", command=getInfoProducts, highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
    boton_hecho.grid(row=9, column=1, pady=10)

    boton_volver = tk.Button(formulario_producto, image=ButtonClass.btnVolver, bg="#030618", command=formulario_producto.destroy, highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
    boton_volver.grid(row=9, column=0, pady=10)