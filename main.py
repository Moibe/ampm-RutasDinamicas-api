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
    return {"AMPM": "API Etiquetado de Rutas Dinámicas."}


#Avance Total.
@app.get("/getAvanceTotal")
def getAvanceTotal(campo: str = "Pendiente", orden: str = "ASC"):
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doAvanceTotal(campo, orden)
   return resultado

#Avance por Ruta.
@app.get("/getAvanceXRuta")
def getAvancexRuta(campo: str = "Pendiente", orden: str = "ASC"):
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doAvanceXRuta(campo, orden)
   return resultado

#Avance por Cliente.
@app.get("/getAvanceXCliente")
def getAvancexCliente(campo: str = "Pendiente", orden: str = "ASC"):
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doAvanceXCliente(campo, orden)
   return resultado

#Total de la Información.
@app.get("/getTodo")
def getTodo(campo: str = "[%Avance]", orden: str = "DESC"):
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doTodo(campo, orden)
   return resultado

#Respaldo para pruebas.
@app.get("/fallback")
def fallback():
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.fallback()
   return resultado