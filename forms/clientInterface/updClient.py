import json
import tkinter as tk

def getClientData():
    with open("files/clienteData.json") as file:
        client = json.load(file)
        return client
client = getClientData()

def crear_ventana(app):
    def formulario_cliente(app, arrCli):
        numClienteData = tk.StringVar()
        nombreData = tk.StringVar()
        apellidoData= tk.StringVar()
        localidadData= tk.StringVar()
        correoData= tk.StringVar()
        domicilioData= tk.StringVar()
        telefonoData = tk.StringVar()
            
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

        entry_tel = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=telefonoData)
        entry_tel.grid(row=8, column=1)

        boton_hecho = tk.Button(formulario_cliente, text="Hecho", font=('Arial', 18), command=lambda: getInfoCliente(arrCli))
        boton_hecho.grid(row=9, column=1, pady=10)

        boton_volver = tk.Button(formulario_cliente, text="Volver", font=('Arial', 18), command=formulario_cliente.destroy)
        boton_volver.grid(row=9, column=0, pady=10)

    def consultarCliente(app):
        num = entry.get()
        cliente = list(filter(lambda el: num == el['dni'], client))
        if len(client) > 0:
            formulario_cliente(app, cliente)
        else:
            tk.messagebox.showerror(title="ERROR", message="No existe dicho cliente!")
        var.set('')

    ventana_ingreso = tk.Toplevel(app)
    ventana_ingreso.geometry("540x150")
    ventana_ingreso.title("Consulta de Cliente")
    ventana_ingreso.resizable(0, 0)

    labelfr = tk.LabelFrame(ventana_ingreso, text="Documento del Cliente")
    labelfr.pack(fill='both', expand='yes', padx=10, pady=5)

    var = tk.StringVar()

    label = tk.Label(labelfr, text="INGRESE EL DNI: ", font=('Arial', 18))
    label.place(x=10, y=10)

    entry = tk.Entry(labelfr, textvariable=var, font=('Arial', 18))
    entry.place(x=225, y=10)

    boton = tk.Button(labelfr, text="CONSULTAR", command=lambda: consultarCliente(app), font=('Arial', 15))
    boton.place(x=185, y=65)

