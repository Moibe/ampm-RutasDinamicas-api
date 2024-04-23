#Definir el TOP desde aquí.
#O puedo yo definirlo dinámicamente después de extraerlo de aquí.
avanceTotal = "SELECT Total, Avance, Pendiente, [%Avance], [%Pendiente] FROM vwGetGuiasImpresasAvance where OficinaId=2 and TipoRuta='FIJA' ORDER BY Total DESC"
avanceXCliente = "SELECT TOP (8) Cliente, Total, Avance, Pendiente, [%Avance], [%Pendiente] FROM vwGetGuiasImpresasXClienteAvance where OficinaId=2 and TipoRuta='FIJA' ORDER BY Total DESC"
avanceXRuta = "SELECT TOP (5) Ruta, Total, Avance, Pendiente, [%Avance], [%Pendiente] FROM vwGetGuiasImpresasXRutaAvance where OficinaId=2 and TipoRuta='FIJA' ORDER BY Total DESC"
