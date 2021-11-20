import json

class Consultar:

    
    def getProductData(self):
        with open("files/productoData.json") as file:
            product = json.load(file)
            print(product)

    def getProviderData(self):
        with open("files/proveedorData.json") as file:
            provider = json.load(file)
            print(provider)    

# a = Consultar()
# a.getClientData()