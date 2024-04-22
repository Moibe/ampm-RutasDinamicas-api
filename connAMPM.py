import time
import json
import pyodbc
import queries
import configuracion

def do(consulta):
     
    cadena_conexion = configuracion.conn

    conexion = pyodbc.connect(cadena_conexion)
    print(conexion)
    time.sleep(1)

    cursor = conexion.cursor()
    cursor.execute(consulta)

    filas = cursor.fetchall()

    count_filas = len(filas)
    print(f"Hay {count_filas} filas.")
    time.sleep(1)

    json_data = []

    for fila in filas:
        
        row_data = {
            # "Cliente": fila[0],
            "Total": fila[0],
            "Avance": fila[1],
            "Pendiente": fila[2],
            "[%Avance]": str(round(fila[3],2)),
            "[%Pendiente]": str(round(fila[4],2))
        }

        json_data.append(row_data)
        
    print("jsondata:")
    print(json_data)

    json_string = json.dumps(json_data, indent=4)

    # Print the JSON string
    print(json_string)

    return json_data