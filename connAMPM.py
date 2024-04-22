import time
import json
import pyodbc
import queries
import configuracion

#Conexión a Base
cadena_conexion = configuracion.conn
conexion = pyodbc.connect(cadena_conexion)
print(conexion)
cursor = conexion.cursor()

def doAvanceTotal(consulta):

    cursor.execute(consulta)
    filas = cursor.fetchall()

    json_data = []

    for fila in filas:

        row_data = {
            "Total": fila[0],
            "Avance": fila[1],
            "Pendiente": fila[2],
            "[%Avance]": str(round(fila[3],2)),
            "[%Pendiente]": str(round(fila[4],2))
        }

        json_data.append(row_data)
        
    print("jsondata:")
    print(json_data)

    return json_data

def doAvanceXRuta(consulta):

    cursor.execute(consulta)
    filas = cursor.fetchall()

    json_data = []

    for fila in filas:

        row_data = {
            "Cliente": fila[0],
            "Total": fila[1],
            "Avance": fila[2],
            "Pendiente": fila[3],
            "[%Avance]": str(round(fila[4],2)),
            "[%Pendiente]": str(round(fila[5],2))
        }

        json_data.append(row_data)
        
    print("jsondata:")
    print(json_data)

    return json_data

def doAvanceXCliente(consulta):

    cursor.execute(consulta)
    filas = cursor.fetchall()

    json_data = []

    for fila in filas:

        row_data = {
            "Cliente": fila[0],
            "Total": fila[1],
            "Avance": fila[2],
            "Pendiente": fila[3],
            "[%Avance]": str(round(fila[4],2)),
            "[%Pendiente]": str(round(fila[5],2))
        }

        json_data.append(row_data)
        
    print("jsondata:")
    print(json_data)

    return json_data
