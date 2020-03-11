import logging
from datetime import date
from datetime import datetime

def configLog(name, log_file, level=logging.DEBUG):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def today():
    today = date.today()
    return "{}{:02d}{:02d}".format(today.year, today.month, today.day)

def logAPI(purl,pverbo,pheader,pbodyType,pbody,presponse):
    name = "C:\\Log\\API_%s.log" % (today())

    logger = configLog("API",name)

    log = "\n                                             -*LOG API*-                                        \n"
    log += "REQUEST: " + "\n"
    log += "URL: " + purl + "\n"
    log += "Method: " + pverbo + "\n"
    log += "Headers:" + pheader['Content-type'] + "\n"
    log += "BodyType:" + pbodyType + "\n"
    log += "Body:" + pbody + "\n" + "\n"
    log += "RESPONSE:" + "\n"
    log += "ResultCode: " + str(presponse.status_code) + "\n"
    log += "Content: " + str(presponse.text) + "\n"
    log += "\n**********************************************************************************************\n"
    logger.debug(log)

def logMSSQL(pqry,pdef):
    name = "C:\\Log\\SQL_%s.log" % (today())

    logger = configLog("SQL",name)
    log = "\n                                             -*LOG MSSQL*-                                     \n"
    log += "Def:" + pdef + "\n"
    log += "QRY: " + "\n"
    log += pqry + "\n"
    
    log += "\n**********************************************************************************************\n"
    logger.debug(log)