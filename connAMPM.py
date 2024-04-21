import time
import json
import pyodbc
import queries
import configuracion

def do():

    cadena_conexion = configuracion.conn

    conexion = pyodbc.connect(cadena_conexion)
    print(conexion)
    time.sleep(1)

    cursor = conexion.cursor()
    cursor.execute(queries.avanceXcliente)

    filas = cursor.fetchall()

    count_filas = len(filas)
    print(f"Hay {count_filas} filas.")
    time.sleep(1)

    #Impresión Normal

    # for fila in filas:
    #     # Imprimir cada campo por separado
    #     print("Cliente:", fila[0])
    #     print("Total:", fila[1])
    #     print("Avance:", fila[2])
    #     print("Pendiente:", fila[3])
    #     print("[%Avance]:", fila[4])
    #     print("[%Pendiente]:", fila[5])

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

    json_string = json.dumps(json_data, indent=4)

    # Print the JSON string
    print(json_string)

    return json_data