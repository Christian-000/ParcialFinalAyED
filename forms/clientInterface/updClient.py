import json
import tkinter as tk

# FUNCIÓN PARA CARGAR EL ARCHIVO
def getClientData():
    with open("files/clienteData.json") as file:
        client = json.load(file)
        return client
client = getClientData() # EL ARCHIVO SE ALMACENA EN UN OBJETO

def crear_ventana(app):
    from ButtonClass.ButtonClass import ButtonClass
    # FUNCIÓN PARA ACTUALIZAR ARCHIVO: LA FUNCIÓN RECIBE EL ELEMENTO FILTRADO COMO PARÁMETRO
    # GUARDA SU DNI, Y ABRE UN FORMULARIO PARA QUE SE INGRESEN LOS DEMÁS DATOS.
    def formulario_cliente(app, arrCli):
        numClienteData = tk.StringVar()
        nombreData = tk.StringVar()
        apellidoData= tk.StringVar()
        localidadData= tk.StringVar()
        correoData= tk.StringVar()
        domicilioData= tk.StringVar()
        telefonoData = tk.StringVar()

        # FUNCIÓN PARA OBTENER LOS DATOS DE LOS CAMPOS DE TEXTO Y ALMACENARLOS EN EL ARCHIVO.    
        def getInfoCliente(arrClient):
            arrClient[0]['numero'] = numClienteData.get()
            arrClient[0]['nombre'] = nombreData.get()
            arrClient[0]['apellido'] = apellidoData.get()
            arrClient[0]['localidad'] = localidadData.get()
            arrClient[0]['correo'] = correoData.get()
            arrClient[0]['domicilio'] = domicilioData.get()
            arrClient[0]['telefono'] = telefonoData.get()
            f = open("files/clienteData.json", "w")
            
            newFile = json.dumps(client, indent=4, sort_keys=True)
            
            f.write(newFile)
            f.close()
            formulario_cliente.destroy()


        formulario_cliente = tk.Toplevel(app, bg="#030618")
        formulario_cliente.geometry("500x550")

        label_formulario_cliente = tk.Label(formulario_cliente, text="Información del Cliente:", font=('Arial', 18), bg="#030618", fg="#fff")
        label_formulario_cliente.grid(row=0, column=0, columnspan=2, pady=10)

        numero_cliente = tk.Label(formulario_cliente, text="Número:", font=('Arial', 14), bg="#030618", fg="#fff")
        numero_cliente.grid(row=1, column=0, pady=10, padx=10)

        nombre_cliente = tk.Label(formulario_cliente, text="Nombre:", font=('Arial', 14), bg="#030618", fg="#fff")
        nombre_cliente.grid(row=2, column=0, pady=10, padx=10)

        apellido_cliente = tk.Label(formulario_cliente, text="Apellido:", font=('Arial', 14), bg="#030618", fg="#fff")
        apellido_cliente.grid(row=3, column=0, pady=10, padx=10)

        localidad_cliente = tk.Label(formulario_cliente, text="Localidad:", font=('Arial', 14), bg="#030618", fg="#fff")
        localidad_cliente.grid(row=4, column=0, pady=10, padx=10)

        correo_cliente = tk.Label(formulario_cliente, text="Correo:", font=('Arial', 14), bg="#030618", fg="#fff")
        correo_cliente.grid(row=5, column=0, pady=10, padx=10)

        domicilio_cliente = tk.Label(formulario_cliente, text="Domicilio:", font=('Arial', 14), bg="#030618", fg="#fff")
        domicilio_cliente.grid(row=6, column=0, pady=10, padx=10)

        telefono_cliente = tk.Label(formulario_cliente, text="Teléfono:", font=('Arial', 14), bg="#030618", fg="#fff")
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

        entry_tel = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=telefonoData)
        entry_tel.grid(row=8, column=1)

        boton_hecho = tk.Button(formulario_cliente, image=ButtonClass.btnConfirmar, bg="#030618", command=lambda: getInfoCliente(arrCli), highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
        boton_hecho.grid(row=9, column=1, pady=10)

        boton_volver = tk.Button(formulario_cliente, image=ButtonClass.btnVolver, bg="#030618", command=formulario_cliente.destroy, highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
        boton_volver.grid(row=9, column=0, pady=10)

    # FUNCIÓN PARA CONSULTAR LA EXISTENCIA DEL CLIENTE
    def consultarCliente(app):
        num = entry.get()
        cliente = list(filter(lambda el: num == el['dni'], client)) # SE FILTRAN LOS REGISTROS CUYO DNI COINCIDA CON EL INGRESADO
        if len(cliente) > 0: # SI EXISTE EL CLIENTE, SE PASA COMO PARÁMETRO A LA FUNCIÓN
            formulario_cliente(app, cliente)
        else: # SI NO EXISTE, SE MUESTRA UN MSJ. DE ERROR
            tk.messagebox.showerror(title="ERROR", message="No existe dicho cliente!")
        var.set('')

    # CREACIÓN DE LAS VENTANAS
    ventana_ingreso = tk.Toplevel(app, bg="#030618")
    ventana_ingreso.geometry("540x250")
    ventana_ingreso.title("Actualización de Cliente")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="Documento del Cliente", bg="#030618", fg="#fff")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL DNI: ", font=('Arial', 18), bg="#030618", fg="#fff")
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18), bg="#34495E", fg="#fff")
    entry.place(x=225, y=10)

    boton = tk.Button(labelfr, image=ButtonClass.btnConsultar, command=lambda: consultarCliente(app), bg="#030618", highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
    boton.place(x=185, y=65)

