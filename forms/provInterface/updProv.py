import json
import tkinter as tk

# FUNCIÓN PARA CARGAR EL ARCHIVO
def getProviderData():
    with open("files/proveedorData.json") as file:
        provider = json.load(file)
        return provider
proveedor = getProviderData() # SE GUARDA EL ARCHIVO EN UN OBJETO

def crear_ventana(app):
    from ButtonClass.ButtonClass import ButtonClass
    # FUNCIÓN PARA ACTUALIZAR ARCHIVO: LA FUNCIÓN RECIBE EL ELEMENTO FILTRADO COMO PARÁMETRO
    # GUARDA SU CUIL, Y ABRE UN FORMULARIO PARA QUE SE INGRESEN LOS DEMÁS DATOS.
    def formulario_producto(app, arrProv):
        codigoP = tk.StringVar()
        razonSocialData = tk.StringVar()
        domicilioData = tk.StringVar()
        telefonoData = tk.StringVar()

        # FUNCIÓN PARA OBTENER LOS DATOS DE LOS CAMPOS Y ALMACENARLOS EN EL ARCHIVO
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

        formulario_proveedor = tk.Toplevel(app, bg="#030618")
        formulario_proveedor.geometry("500x400")

        label_formulario_proveedor = tk.Label(formulario_proveedor, text="Información del Proveedor:", font=('Arial', 18), bg="#030618", fg="#fff")
        label_formulario_proveedor.grid(row=0, column=0, columnspan=2, pady=10)

        codigo_p = tk.Label(formulario_proveedor, text="Código: ", font=('Arial', 14), bg="#030618", fg="#fff")
        codigo_p.grid(row=1, column=0, pady=10, padx=10)

        razon_social = tk.Label(formulario_proveedor, text="Razón social:", font=('Arial', 14), bg="#030618", fg="#fff")
        razon_social.grid(row=3, column=0, pady=10, padx=10)

        domicilio = tk.Label(formulario_proveedor, text="Domicilio:", font=('Arial', 14), bg="#030618", fg="#fff")
        domicilio.grid(row=4, column=0, pady=10, padx=10)

        telefono = tk.Label(formulario_proveedor, text="Teléfono:", font=('Arial', 14), bg="#030618", fg="#fff")
        telefono.grid(row=5, column=0, pady=10, padx=10)

        entry_codigop = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=codigoP)
        entry_codigop.grid(row=1, column=1)

        entry_rs = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=razonSocialData)
        entry_rs.grid(row=3, column=1)

        entry_dom = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=domicilioData)
        entry_dom.grid(row=4, column=1)

        entry_tel = tk.Entry(formulario_proveedor, font=('Arial', 14), textvariable=telefonoData)
        entry_tel.grid(row=5, column=1)

        boton_hecho = tk.Button(formulario_proveedor, image=ButtonClass.btnConfirmar, bg="#030618", command=lambda: getInfoProducts(arrProv), highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
        boton_hecho.grid(row=6, column=1, pady=10)

        boton_volver = tk.Button(formulario_proveedor, image=ButtonClass.btnVolver, bg="#030618", command=formulario_proveedor.destroy, highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
        boton_volver.grid(row=6, column=0, pady=10)

    # FUNCIÓN PARA CONSULTAR LA EXISTENCIA DEL PROVEEDOR
    def consultarProveedor(app):
        num = entry.get()
        provider = list(filter(lambda el: num == el['cuil'], proveedor)) # SE FILTRAN LOS ELEMENTOS CUYO CUIL COINCIDE CON EL DATO INGRESADO.

        if len(provider) > 0: # SI EXISTE EL PROVEEDOR, SE PASA EL REGISTRO A LA FUNCIÓN COMO PARÁMETRO
            formulario_producto(app, provider)
        else: # SI NO, SE MUESTRA UN MSJ. DE ERROR
            tk.messagebox.showerror(title="ERROR", message="No existe dicho Proveedor!")
        var.set('')

    # CREACIÓN DE LA VENTANA
    ventana_ingreso = tk.Toplevel(app, bg="#030618")
    ventana_ingreso.geometry("590x250")
    ventana_ingreso.title("Actualización de Proveedor")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="CUIL del Proveedor", bg="#030618", fg="#fff")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL CUIL: ", font=('Arial', 18), bg="#030618", fg="#fff")
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18), bg="#34495E", fg="#fff")
    entry.place(x=280, y=10)

    boton = tk.Button(labelfr, image=ButtonClass.btnConsultar, command=lambda: consultarProveedor(app), bg="#030618", highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
    boton.place(x=195, y=65)

