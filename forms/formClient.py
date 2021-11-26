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

    # VALIDACIÓN DE DATOS
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

        if(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', obj["correo"])):
            pass
        else:
            messagebox.showerror("Email Invalido", "La estructura del email debe ser del tipo 'email@email.com'.")
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

        else:
            f = open("files/clienteData.json", "w")
            
            file.append(obj)
            newFile = json.dumps(file, indent=4, sort_keys=True)
            
            f.write(newFile)
            f.close()
            formulario_cliente.destroy()

    # FUNCIÓN PARA OBTENER LOS DATOS DE LOS CAMPOS Y ALMACENARLOS EN EL ARCHIVO.        
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
        
    formulario_cliente = tk.Toplevel(app, bg="#030618")
    formulario_cliente.geometry("500x550")

    from ButtonClass import ButtonClass

    # CREACIÓN DEL FORMULARIO

    label_formulario_cliente = tk.Label(formulario_cliente, text="Información del Cliente:", font=('Arial', 18), bg="#030618", fg="#fff")
    label_formulario_cliente.grid(row=0, column=0, columnspan=2, pady=10)

    numero_cliente = tk.Label(formulario_cliente, text="Código:", font=('Arial', 14), bg="#030618", fg="#fff")
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

    DNI_cliente = tk.Label(formulario_cliente, text="Documento:", font=('Arial', 14), bg="#030618", fg="#fff")
    DNI_cliente.grid(row=7, column=0, pady=10, padx=10)

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

    entry_dni = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=dniData)
    entry_dni.grid(row=7, column=1)

    entry_tel = tk.Entry(formulario_cliente, font=('Arial', 14), textvariable=telefonoData)
    entry_tel.grid(row=8, column=1)

    boton_hecho = tk.Button(formulario_cliente, image=ButtonClass.ButtonClass.btnConfirmar, bg="#030618", command=getInfoCliente, highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
    boton_hecho.grid(row=9, column=1, pady=10)

    boton_volver = tk.Button(formulario_cliente, image=ButtonClass.ButtonClass.btnVolver, bg="#030618", command=formulario_cliente.destroy, highlightthickness = 0, borderwidth=0, activebackground="#041E2D")
    boton_volver.grid(row=9, column=0, pady=10)
