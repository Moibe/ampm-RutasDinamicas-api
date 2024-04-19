import time
import json
import pyodbc
import queries
import configuracion

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

print("Primero impreso normal:")
time.sleep(8)

for fila in filas:
    # Imprimir cada campo por separado
    print("Cliente:", fila[0])
    print("Total:", fila[1])
    print("Avance:", fila[2])
    print("Pendiente:", fila[3])
    print("[%Avance]:", fila[4])
    print("[%Pendiente]:", fila[5])

print("Fin impresión normal...")
time.sleep(1)

print("Ahora impresión json:")
time.sleep(1)

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

# Convert the list of dictionaries to a JSON string
json_string = json.dumps(json_data, indent=4)  # Add 'indent=4' for better readability

# Print the JSON string
print(json_string)