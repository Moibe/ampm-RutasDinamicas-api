import connAMPM
from fastapi import FastAPI, Query, HTTPException
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

#def getAvanceTotal(campo: str = "Pendiente", orden: str = "ASC"):
#Avance Total.
@app.get("/getAvanceTotal")
def getAvanceTotal(campo: str = "Pendiente", orden: str = "ASC"):
   
   if campo in ["Total", "Avance", "Pendiente", "[%Avance]", "[%Pendiente]", "FPrimero", "FUltimo", "[Tiempo(min)]", "Tiempo", "Rutas", "Clientes"]:
      if orden in ["ASC", "DESC"]:
         
         #Validados ambos campos realiza query.
         resultado = connAMPM.doAvanceTotal(campo, orden)
         return resultado
      else:
         raise HTTPException(status_code=403, detail="Valor para variable 'orden' inválido. Solo puedes usar los valores 'DESC' y 'ASC' para ordenamiento.")
   else:
      raise HTTPException(status_code=403, detail="Valor para variable 'campo' inválido. Valores válidos: 'Total', 'Avance', 'Pendiente', '[%Avance]', '[%Pendiente]', 'FPrimero', 'FUltimo', '[Tiempo(min)]', 'Tiempo', 'Rutas', 'Clientes' ")

#Avance por Ruta.
@app.get("/getAvanceXRuta")
def getAvancexRuta(campo: str = "Pendiente", orden: str = "ASC"):

   if campo in ["Ruta", "Total", "Avance", "Pendiente", "[%Avance]", "[%Pendiente]", "FPrimero", "FUltimo", "[Tiempo(min)]", "Tiempo"]:
      if orden in ["ASC", "DESC"]:
   
         #Validados ambos campos realiza query.
         resultado = connAMPM.doAvanceXRuta(campo, orden)
         return resultado
      else:
         raise HTTPException(status_code=403, detail="Valor para variable 'orden' inválido. Solo puedes usar los valores 'DESC' y 'ASC' para ordenamiento.")
   else:
      raise HTTPException(status_code=403, detail="Valor para variable 'campo' inválido. Valores válidos: 'Total', 'Avance', 'Pendiente', '[%Avance]', '[%Pendiente]', 'FPrimero', 'FUltimo', '[Tiempo(min)]', 'Tiempo'")


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