import pymssql
import decimal
from datetime import date
from datetime import datetime
from log import *

def conecta():
    conn = pymssql.connect(server='SERVER', user='sa', password='Pass@movilsol', database='b4_Country')
    #conn = pymssql.connect(server='192.168.1.100', user='sa', password='Pass@pccfunes', database='b4_ClubCountry')
    return conn

def recuperaJugadores():
    conn = conecta()
    cursor = conn.cursor(as_dict=True)
    qry = 'SELECT TOP 1 * FROM vw_ApiCliente'
    logMSSQL(qry,'recuperaJugadores')
    cursor.execute(qry)
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
    if (row['UltimaFechaPago'] is None):
        ufep = "null" 
        resp = '{"dni":%s,"habilitado":%s,"fecha_ultimo_cobro":%s}'
    else:   
        ufep = "{:02d}-{:02d}-{}".format(row['UltimaFechaPago'].day, row['UltimaFechaPago'].month, row['UltimaFechaPago'].year)
        resp = '{"dni":%s,"habilitado":%s,"fecha_ultimo_cobro":"%s"}'
    resp = resp % (row['dni'],row['Habilitado'],ufep)
    return resp