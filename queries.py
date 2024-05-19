avanceTotal = """
SELECT Total, Avance, Pendiente, [%Avance], [%Pendiente] 
FROM vwGetGuiasImpresasAvance 
WHERE OficinaId=2 and TipoRuta='DINAMICA' 
ORDER BY Total DESC
"""

avanceXCliente = """
SELECT LEFT(Cliente, 9) AS Cliente, Total, Avance, Pendiente, [%Avance], [%Pendiente] 
FROM vwGetGuiasImpresasXClienteAvance 
WHERE OficinaId=2 and TipoRuta='DINAMICA'
ORDER BY Total ASC
"""

avanceXRuta = """
SELECT Ruta, Total, Avance, Pendiente, [%Avance], [%Pendiente], FPrimero, FUltimo, [Tiempo(min)]
FROM vwGetGuiasImpresasXRutaAvance 
WHERE OficinaId=2 and TipoRuta='DINAMICA' 
ORDER BY Pendiente ASC
"""
