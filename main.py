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
def getAvanceTotal():
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doAvanceTotal()
   return resultado

#Avance por Ruta.
@app.get("/getAvanceXRuta")
def getAvancexRuta():
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doAvanceXRuta()
   return resultado

#Avance por Cliente.
@app.get("/getAvanceXCliente")
def getAvancexCliente():
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doAvanceXCliente()
   return resultado

#Total de la Información.
@app.get("/getTodo")
def getTodo(campo: str = "Pendiente", orden: str = "ASC"):
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.doTodo(campo, orden)
   return resultado

#Respaldo para pruebas.
@app.get("/fallback")
def fallback():
   #Después: Agregar parámetro para cuantos resultados.
   resultado = connAMPM.fallback()
   return resultado