import connAMPM
from fastapi import FastAPI
import queries
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get("/")
def read_root():
    return {"AMPM": "Moisés Briseño Estrello."}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

#AMPM#
#Avance por Ruta.
@app.get("/getAvanceTotal")
def getAvanceTotal():
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doAvanceTotal(queries.avanceTotal)
   return resultado

#Avance por Ruta.
@app.get("/getAvanceXRuta")
def getAvancexRuta():
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doAvanceXRuta(queries.avanceXRuta)
   return resultado

#Avance por Cliente.
@app.get("/getAvanceXCliente")
def getAvancexCliente():
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doAvanceXCliente(queries.avanceXCliente)
   return resultado

#Total de la Información.
@app.get("/getTodo")
def getTodo():
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doTodo()
   return resultado