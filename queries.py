avanceTotal = """
SELECT Total, Avance, Pendiente, [%Avance], [%Pendiente], HPrimero, FPrimero, FUltimo, [Tiempo(min)], Tiempo, Rutas, Clientes 
FROM vwGetGuiasImpresasAvance 
WHERE OficinaId=2 and TipoRuta='DINAMICA' 
ORDER BY Total DESC
"""

avanceXCliente = """
SELECT LEFT(Cliente, 9) AS Cliente, Total, Avance, Pendiente, [%Avance], [%Pendiente], FPrimero, FUltimo, [Tiempo(min)], Tiempo 
FROM vwGetGuiasImpresasXClienteAvance 
WHERE OficinaId=2 and TipoRuta='DINAMICA'
ORDER BY Total ASC
"""

avanceXRuta = """
SELECT Ruta, Total, Avance, Pendiente, [%Avance], [%Pendiente], FPrimero, FUltimo, [Tiempo(min)], Tiempo
FROM vwGetGuiasImpresasXRutaAvance 
WHERE OficinaId=2 and TipoRuta='DINAMICA' 
ORDER BY Pendiente ASC
"""
