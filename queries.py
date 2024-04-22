#Se llama a la vista directamente pero lo puedo cambiar a llamar a un stored procedura y que el top se defina desde allá.
#O puedo yo definirlo dinámicamente después de extraerlo de aquí.
avanceTotal = "SELECT TOP (5) Total, Avance, Pendiente, [%Avance], [%Pendiente] FROM vwGetGuiasImpresasAvance where OficinaId=2 and TipoRuta='FIJA' ORDER BY Total DESC"
avanceXcliente = "SELECT TOP (8) Cliente, Total, Avance, Pendiente, [%Avance], [%Pendiente] FROM vwGetGuiasImpresasXClienteAvance where OficinaId=2 and TipoRuta='FIJA' ORDER BY Total DESC"
avanceXRuta = "SELECT TOP (5) Ruta, Total, Avance, Pendiente, [%Avance], [%Pendiente] FROM vwGetGuiasImpresasXRutaAvance where OficinaId=2 and TipoRuta='FIJA' ORDER BY Total DESC"
