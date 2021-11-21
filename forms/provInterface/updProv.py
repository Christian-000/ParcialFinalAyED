import json
import tkinter as tk

def getProviderData():
    with open("files/proveedorData.json") as file:
        provider = json.load(file)
        return provider
proveedor = getProviderData()

def crear_ventana(app):
    def formulario_producto(app, arrProv):
        codigoP = tk.StringVar()
        razonSocialData = tk.StringVar()
        domicilioData = tk.StringVar()
        telefonoData = tk.StringVar()
            
        def getInfoProducts(arrProv):
            arrProv[0]["codigo"] = codigoP.get()
            arrProv[0]["razonSocial"] = razonSocialData.get() 
            arrProv[0]["domicilio"] = domicilioData.get() 
            arrProv[0]["telefono"] = telefonoData.get()
            f = open("files/proveedorData.json", "w")

            
            newFile = json.dumps(proveedor, indent=4, sort_keys=True)
            
            f.write(newFile)
            f.close()
            formulario_producto.destroy()


        formulario_proveedor = tk.Toplevel(app)
        formulario_proveedor.geometry("475x400")

        label_formulario_proveedor = tk.Label(formulario_proveedor, text="Información del Proveedor:", font=('Arial', 18))
        label_formulario_proveedor.grid(row=0, column=0, columnspan=2, pady=10)

        codigo_p = tk.Label(formulario_proveedor, text="Código: ", font=('Arial', 14))
        codigo_p.grid(row=1, column=0, pady=10, padx=10)


        razon_social = tk.Label(formulario_proveedor, text="Razón social:", font=('Arial', 14))
        razon_social.grid(row=3, column=0, pady=10, padx=10)

        domicilio = tk.Label(formulario_proveedor, text="Domicilio:", font=('Arial', 14))
        domicilio.grid(row=4, column=0, pady=10, padx=10)

        telefono = tk.Label(formulario_proveedor, text="Teléfono:", font=('Arial', 14))
        telefono.grid(row=5, column=0, pady=10, padx=10)

        entry_codigop = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=codigoP)
        entry_codigop.grid(row=1, column=1)



        entry_rs = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=razonSocialData)
        entry_rs.grid(row=3, column=1)

        entry_dom = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=domicilioData)
        entry_dom.grid(row=4, column=1)

        entry_tel = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=telefonoData)
        entry_tel.grid(row=5, column=1)


        boton_hecho = tk.Button(formulario_proveedor, text="Hecho", font=('Arial', 18), command=lambda: getInfoProducts(arrProv))
        boton_hecho.grid(row=6, column=1, pady=10)

        boton_volver = tk.Button(formulario_proveedor, text="Volver", font=('Arial', 18), command=formulario_proveedor.destroy)
        boton_volver.grid(row=6, column=0, pady=10)

    def consultarProveedor(app):
        num = entry.get()
        provider = list(filter(lambda el: num == el['cuil'], proveedor))

        if len(provider) > 0:
            formulario_producto(app, provider)
        else:
            tk.messagebox.showerror(title="ERROR", message="No existe dicho Proveedor!")
        var.set('')

    ventana_ingreso = tk.Toplevel(app)
    ventana_ingreso.geometry("590x150")
    ventana_ingreso.title("Consulta de Producto")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="CUIL del Proveedor")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL CUIL: ", font=('Arial', 18))
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18))
    entry.place(x=280, y=10)

    boton = tk.Button(labelfr, text="CONSULTAR", command=lambda: consultarProveedor(app), font=('Arial', 15))
    boton.place(x=195, y=65)

