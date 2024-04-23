#Definir el TOP desde aquí.
#O puedo yo definirlo dinámicamente después de extraerlo de aquí.
avanceTotal = "SELECT Total, Avance, Pendiente, [%Avance], [%Pendiente] FROM vwGetGuiasImpresasAvance where OficinaId=2 and TipoRuta='DINAMICA' ORDER BY Total DESC"
avanceXCliente = "SELECT TOP (5) Cliente, Total, Avance, Pendiente, [%Avance], [%Pendiente] FROM vwGetGuiasImpresasXClienteAvance where OficinaId=2 and TipoRuta='DINAMICA' ORDER BY Total DESC"
avanceXRuta = "SELECT Ruta, Total, Avance, Pendiente, [%Avance], [%Pendiente] FROM vwGetGuiasImpresasXRutaAvance where OficinaId=2 and TipoRuta='DINAMICA' ORDER BY Total DESC"
