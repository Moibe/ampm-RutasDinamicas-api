import time
import pyodbc
import queries
import compiler
import configuracion

#Conexión a Base
cadena_conexion = compiler.do(configuracion.connF)
conexion = pyodbc.connect(cadena_conexion)
print(conexion)
cursor = conexion.cursor()

def doAvanceTotal(consulta):

    cursor.execute(consulta)
    filas = cursor.fetchall()

    data_global = {}

    totales_data = []

    for fila in filas:

        row_data = {
            "Total": fila[0],
            "Avance": fila[1],
            "Pendiente": fila[2],
            "[%Avance]": str(round(fila[3],2)),
            "[%Pendiente]": str(round(fila[4],2))
        }

        totales_data.append(row_data)
    
    data_global["TOTALES"] = totales_data

    print("Entrega Final:")
    print(data_global)

    return data_global

def doAvanceXRuta(consulta):

    cursor.execute(consulta)
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
            "[%Pendiente]": str(round(fila[5],2))
        }

        ruta_data.append(row_data)
    
    data_global["RUTAS"] = ruta_data
        
    print("Entrega Final:")
    print(data_global)

    return data_global

def doAvanceXCliente(consulta):

    cursor.execute(consulta)
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
            "[%Pendiente]": str(round(fila[5],2))
        }

        client_data.append(row_data)
        
    data_global["CLIENTES"] = client_data
    
    print("Entrega Final:")
    print(data_global)

    return data_global

#def doTodo():
