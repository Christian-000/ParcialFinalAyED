import tkinter as tk
from tkinter import messagebox
import json
import re

f1 = open("files/clienteData.json", "r")
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
 
    def validate(obj):
        count = 0
        if(obj["numero"].isdigit()):
            pass
        else:
            messagebox.showerror("Numero Invalido", "Debes poner un valor numerico")
            count += 1

        if(obj["nombre"].isalpha()):
            pass
        else:
            messagebox.showerror("Nombre Invalido", "No se puede incluir Simbolos o Numeros en el nombre.")
            count += 1

        if(obj["apellido"].isalpha()):
            pass
        else:
            messagebox.showerror("Apellido Invalido", "No se puede incluir Simbolos o Numeros en el Apellido.")
            count += 1

        if(obj["localidad"].isalpha()):
            pass
        else:
            messagebox.showerror("Localidad Invalida", "No se puede incluir Simbolos o Numeros en la Localidad.")
            count += 1

        if(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', obj["correo"])):
            pass
        else:
            messagebox.showerror("Email Invalido", "La estructura del email debe ser del tipo 'email@email.com'.")
            count += 1

        if(obj["domicilio"].isalnum()):
            pass
        else:
            messagebox.showerror("Domicilio Invalido", "El domicilio debe contener Letras y Numero solamente.")
            count += 1

        if(obj["telefono"].isdigit()):
            pass
        else:
            messagebox.showerror("Telefono Invalido", "El telefono debe estar compuesto unicamente por numeros.")
            count += 1

        if(obj["dni"].isdigit()):
            pass
        else:
            messagebox.showerror("Dni Invalido", "El dni debe ser numerico.")
            count += 1
            if(len(obj["dni"]) != 8):
                messagebox.showerror("Dni Invalido", "El dni debe ser de 8 digitos.")
                count += 1
        if(count > 0):
            messagebox.showerror("ERROR", "Hay datos invalidos en el formulario.")
            formulario_cliente.destroy()

        else:
            f = open("files/clienteData.json", "w")
            
            file.append(obj)
            newFile = json.dumps(file, indent=4, sort_keys=True)
            
            f.write(newFile)
            f.close()
            formulario_cliente.destroy()
    def getInfoCliente():
        nwObjc = {}
        nwObjc['numero'] = numClienteData.get()
        nwObjc['nombre'] = nombreData.get()
        nwObjc['apellido'] = apellidoData.get()
        nwObjc['localidad'] = localidadData.get()
        nwObjc['correo'] = correoData.get()
        nwObjc['domicilio'] = domicilioData.get()
        nwObjc['dni'] = dniData.get()
        nwObjc['telefono'] = telefonoData.get()
        validate(nwObjc)
        


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