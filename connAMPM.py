import os
import json
import time 
import pyodbc
import queries
import compiler
import configuracion

#Conexión a Base
#PRUEBAS
#cadena_conexion = compiler.do(configuracion.connF)

#!!!!!Producción
cadena_conexion = compiler.do(configuracion.connP)

try: 
    print("Conectando a base de datos...")
    conexion = pyodbc.connect(cadena_conexion)
    print(conexion)
    cursor = conexion.cursor()

except Exception as e: 
    print("No fue posible conectar a la base de datos.")
    time.sleep(7)


def doAvanceTotal(campo, orden):

    ordenamiento = "ORDER BY " + campo + " " + orden

    query = queries.avanceTotal + ordenamiento
    cursor.execute(query)
    filas = cursor.fetchall()

    data_global = {}

    totales_data = []

    for fila in filas:

        row_data = {
            "Total": fila[0],
            "Avance": fila[1],
            "Pendiente": fila[2],
            "[%Avance]": str(round(fila[3],2)),
            "[%Pendiente]": str(round(fila[4],2)),
            "HoraInicio": fila[5],
            "Inicio": fila[6],
            "Ultimo": fila[7],
            "Tiempo(min)": fila[8],
            "Tiempo": fila[9],
            "TotalRutas": fila[10],
            "TotalClientes": fila[11]
        }

        totales_data.append(row_data)
    
    data_global["TOTALES"] = totales_data

    print("Entrega Final:")
    print(data_global)

    return data_global

def doAvanceXRuta(campo, orden):

    ordenamiento = "ORDER BY " + campo + " " + orden

    query = queries.avanceXRuta + ordenamiento
    cursor.execute(query)
    filas = cursor.fetchall()

    data_global = {}

    ruta_data = []

    for fila in filas:

        row_data = {
            "Ruta": fila[0],
            "Total": fila[1],
            "Avance": fila[2],
            "Pendiente": fila[3],
            "[%Avance]": str(round(fila[4],2)),
            "[%Pendiente]": str(round(fila[5],2)),
            "Inicio": fila[6],
            "Ultimo": fila[7],
            "Tiempo(min)": fila[8],
            "Tiempo": fila[9]
        }

        ruta_data.append(row_data)
    
    data_global["RUTAS"] = ruta_data
        
    print("Entrega Final:")
    print(data_global)

    return data_global

def doAvanceXCliente(campo, orden):

    ordenamiento = "ORDER BY " + campo + " " + orden

    query = queries.avanceXCliente + ordenamiento
    cursor.execute(query)
    filas = cursor.fetchall()

    data_global = {}

    client_data = []

    for fila in filas:

        row_data = {
            "Cliente": fila[0],
            "Total": fila[1],
            "Avance": fila[2],
            "Pendiente": fila[3],
            "[%Avance]": str(round(fila[4],2)),
            "[%Pendiente]": str(round(fila[5],2)),
            "Inicio": fila[6],
            "Ultimo": fila[7],
            "Tiempo(min)": fila[8],
            "Tiempo": fila[9]
        }

        client_data.append(row_data)
        
    data_global["CLIENTES"] = client_data
    
    print("Entrega Final:")
    print(data_global)

    return data_global

def doTodo(campo, orden):

    #El ordenamiento aplica al mismo tiempo para Avance Total, Rutas y Clientes.
    ordenamiento = "ORDER BY " + campo + " " + orden
    print("Ordenamiento: ", ordenamiento)

    data_global = {}

    #RUN ZERO 
    query_avanceTotal = queries.avanceTotal + ordenamiento
    print("QUERY AVANCE TOTAL: ", query_avanceTotal)
    cursor.execute(query_avanceTotal)
    filas = cursor.fetchall()

    totales_data = []

    for fila in filas:

        row_data = {
            "Total": fila[0],
            "Avance": fila[1],
            "Pendiente": fila[2],
            "[%Avance]": str(round(fila[3],2)),
            "[%Pendiente]": str(round(fila[4],2)),
            "HoraInicio": fila[5],
            "Inicio": fila[6],
            "Ultimo": fila[7],
            "Tiempo(min)": fila[8],
            "Tiempo": fila[9],
            "TotalRutas": fila[10],
            "TotalClientes": fila[11]
        }

        totales_data.append(row_data)
    
    data_global["TOTALES"] = totales_data

    #PRIMER RUN
    query_avanceXRuta = queries.avanceXRuta + ordenamiento
    cursor.execute(query_avanceXRuta)
    print("Query Ruta:", queries.avanceXRuta)
    filas = cursor.fetchall()
    

    ruta_data = []

    for fila in filas:

        row_data = {
            "Ruta": fila[0],
            "Total": fila[1],
            "Avance": fila[2],
            "Pendiente": fila[3],
            "[%Avance]": str(round(fila[4],2)),
            "[%Pendiente]": str(round(fila[5],2)),
            "Inicio": fila[6],
            "Ultimo": fila[7],
            "Tiempo(min)": fila[8],
            "Tiempo": fila[9]
        }

        ruta_data.append(row_data)
    
    data_global["RUTAS"] = ruta_data
        
    #SEGUNDO RUN
    ordenamiento_clientes = "ORDER BY [%Avance] ASC"
    query_avanceXCliente = queries.avanceXCliente + ordenamiento_clientes
    cursor.execute(query_avanceXCliente)
    filas = cursor.fetchall()

    client_data = []

    for fila in filas:

        row_data = {
            "Cliente": fila[0],
            "Total": fila[1],
            "Avance": fila[2],
            "Pendiente": fila[3],
            "[%Avance]": str(round(fila[4],2)),
            "[%Pendiente]": str(round(fila[5],2)),
            "Inicio": fila[6],
            "Ultimo": fila[7],
            "Tiempo(min)": fila[8],
            "Tiempo": fila[9]
        }

        client_data.append(row_data)
        
    data_global["CLIENTES"] = client_data    

    return data_global

def fallback():
    # Obtener la ruta del archivo
    ruta_archivo = os.path.join(os.path.dirname(__file__), "getTodo.json")
    print("Ésta es la ruta del archivo json de fallback: ", ruta_archivo)
    time.sleep(6)

    # Abrir y leer el archivo
    with open(ruta_archivo, "r") as archivo:
        contenido_archivo = archivo.read()
        
    # Cargar el contenido como JSON
    datos_json = json.loads(contenido_archivo)

    # Devolver los datos cargados
    return datos_json