import pymssql
from datetime import date
from datetime import datetime
import decimal

def conecta():
    conn = pymssql.connect(server='SERVER', user='sa', password='Pass@movilsol', database='b4_Country')
    return conn

def recuperaJugadores():
    conn = conecta()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT TOP 10 * FROM vw_ApiCliente')
    row = cursor.fetchone()
    resp = '"jugadores": ['
    while row:
        resp = resp + makePayLoad(row) + ','
        row = cursor.fetchone()
    resp = resp[:-1] + ']'
    #print (resp)
    conn.close()
    return resp

def makePayLoad(row):
    resp = '{"dni":%s,"habilitado":%s,"fecha_ultimo_cobro":"%s"}' 
    if (row['UltimaFechaPago'] is None):
        ufep = "null" 
    else:   
        ufep = "{:02d}-{:02d}-{}".format(row['UltimaFechaPago'].day, row['UltimaFechaPago'].month, row['UltimaFechaPago'].year)
    resp = resp % (row['dni'],row['Habilitado'],ufep)
    return resp