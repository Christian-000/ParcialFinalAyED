import tkinter as tk
import json

f1 = open("/home/christian/Escritorio/main/ABM_UNI/ParcialFinalAyED/clienteData.json", "r")
c = f1.read()

file = json.loads(c) #js


def formulario_cliente(app):
    numClienteData = tk.StringVar()
    nombreData = tk.StringVar()
    apellidoData= tk.StringVar()
    localidadData= tk.StringVar()
    correoData= tk.StringVar()
    domicilioData= tk.StringVar()
    dniData= tk.StringVar()
    telefonoData = tk.StringVar()
        
    def getInfoCliente():
        file['numero'] = numClienteData.get()
        file['nombre'] = nombreData.get()
        file['apellido'] = apellidoData.get()
        file['localidad'] = localidadData.get()
        file['correo'] = correoData.get()
        file['domicilio'] = domicilioData.get()
        file['dni'] = dniData.get()
        file['telefono'] = telefonoData.get()
        f = open("/home/christian/Escritorio/main/ABM_UNI/ParcialFinalAyED/clienteData.json", "w")
        newFile = json.dumps(file, indent=4, sort_keys=True)
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