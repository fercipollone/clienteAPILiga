use b4_Country 
 
CREATE VIEW vw_ApiCliente
 AS
 SELECT 
	s.soc_documento AS dni, case when Cant <= 2 then 1 else 0 end AS Habilitado,  dbo.fn_UltimaFechaPago(cp.soc_idsocio) AS UltimaFechaPago
 FROM 
	vw_CuotasPendientesCantidad cp
		INNER JOIN Socio s 
			ON s.soc_idsocio = cp.soc_idsocio 
 WHERE 
	s.cat_idcategoriaporsocio IN (1, 2, 6, 17,18) 
    AND cp.ses_tipoBaja = 0 
    
    
