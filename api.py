import requests
import hashlib
from datetime import date
from datetime import datetime
from hashlib import md5
from log import *

def hash():
    today = date.today()
    periodo = "vef-{:02d}{:02d}{}".format(today.day, today.month, today.year)
    m = hashlib.md5()
    m.update(periodo.encode('utf-8'))
    return m.hexdigest()

def ultimoCobro(jugadores):
    payload = '{"data": {"hash": "%s", %s }}'
    payload = payload % (hash(), jugadores)
    UltimoCobroPost(payload)

def UltimoCobroPost(payload):
    url = 'https://ligacountry.com.ar/api/ultimocobro'
    headers = {'Content-type': 'application/json'}

    response = requests.post(url, headers=headers, data=payload.encode('utf-8'))

    logAPI(url,'POST',headers,'', payload,response)

    print(payload)   
    print("Status code Ultimo Cobro POST: " + str(response.status_code))

    
