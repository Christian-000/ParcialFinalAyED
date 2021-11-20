import tkinter as tk
import json

f1 = open("/home/christian/Escritorio/main/ABM_UNI/ParcialFinalAyED/files/proveedorData.json", "r")
c = f1.read()

file = json.loads(c) #js

def formulario_proveedor(app):

    codigoP = tk.StringVar()
    cuilData = tk.StringVar()
    razonSocialData = tk.StringVar()
    domicilioData = tk.StringVar()
    telefonoData = tk.StringVar()
    def getInfoProveedor():
        nwObjc = {}

        nwObjc["codigo"] = codigoP.get()
        nwObjc["cuil"] = cuilData.get() 
        nwObjc["razonSocial"] = razonSocialData.get() 
        nwObjc["domicilio"] = domicilioData.get() 
        nwObjc["telefono"] = telefonoData.get() 
        f = open("files/proveedorData.json", "w")
        file.append(nwObjc)

        newFile = json.dumps(file, indent=4, sort_keys=True)
        f.write(newFile)
        f.close()
        formulario_proveedor.destroy()

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
