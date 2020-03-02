use b4_Country 
 
 SELECT 
	*  
 FROM 
	vw_CuotasPendientesCantidad cp
		INNER JOIN Socio s 
			ON s.soc_idsocio = cp.soc_idsocio 
 WHERE 
	s.cat_idcategoriaporsocio IN (1, 2, 6, 17,18) 
    AND cp.ses_tipoBaja = 0 
    AND 