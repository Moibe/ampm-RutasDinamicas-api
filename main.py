from fastapi import FastAPI
import requests
from configuracion import API_KEY


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Moisés Briseño Estrello."}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/validar/{numero}")
def validar_capicua(numero:str):
    respuesta = "Nó es capicúa"

    if numero == numero[::-1]:
        respuesta = "Es capicúa"
    return {
        "numero": numero,
        "validacion": respuesta
    }

@app.get("/obtenEstado")
def obten_estado():

    url = "https://onlinesim.io/api/getState.php"

    querystring = {"apikey": API_KEY}

    payload = ""
    response = requests.request("GET", url, data=payload, params=querystring)

           
    return {
        response.text
    }
@app.get("/getAvanceXClientes")
def getAvancexClientes():
         
   return {"Hello": "Moisés Briseño Estrello."}
