import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pymysql

import json
from random import randint
from asyncio import sleep

from channels.generic.websocket import AsyncWebsocketConsumer


class HmiConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        self.test={}
        connection = pymysql.connect(
        #user = 'root',
        #password = '',
        #host = 'localhost',
        #db = 'hmi_data'
        #port = '3306'

        user = 'Rony',
        password = 'Hmi12345678',
        host = 'Rony.mysql.pythonanywhere-services.com',
        db = 'Rony$hmi_data'
        port = '3306'
    
        )

        #crear listas para almacenar datos hmi
        magnitudes=list()
        valores=list()

        magnitudes=['HORA','CORRIENTE','VOLTAJE','POTENCIA_KW','FRECUENCIA','POTENCIA','VELOCIDAD','TEMPERATURA','NIVEL','PRESION','CAUDAL','ACUMULADO']
        valores=[1,2,3,4,5,6,7,8,9,10,11,12]
        # obtener fecha y hora actual y convertir a formato timestamp 
        #now = datetime.now()
        #timestamp = datetime.timestamp(now)
        #print(now)
        #print(timestamp)
        while True:
            """
            #Enlace para accesder a moniytoreo web hmi
            url = "http://192.168.1.27/RemoteMon/Data/1.php?_="+str(timestamp)

            payload={}
            headers = {
            'Accept-Language': 'es-419,es;q=0.9,en;q=0.8',
            'Referer': 'http://192.168.1.27/RemoteMon/',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'Host': '192.168.1.27',
            'Accept': 'text/html, */*; q=0.01',
            #'Cookie': 'PHPSESSID=9ddf09b7126d8811e91d59c7dc0d5eaa'
            'Cookie': 'PHPSESSID=33d012ba0e43bc0d7328503de568b2c7'
            }

            #peticion get a hmi
            response = requests.request("GET", url, headers=headers, data=payload)
            #print(type(response.text))

            #devuelve texto html
            soup = BeautifulSoup(response.content, "html.parser")

            # buscar los tr de archivo html
            #nomb=soup.find_all("span")
            trs=soup.find_all("tr")

            #buscar y Encontrar las magnitudes y sus valores enviadas por hmi
            for tr in trs:
                try:
                    tds = tr.find_all("td")
                    magnitudes.append(tds[0].get_text())
                    valores.append(tds[1].get_text()[1:]) 
                except:
                    print("valores html no encontrados")
            """
            try:

                #convertir listas a diccionario
                dict_magnitudes_valores = dict(zip(magnitudes[1:], valores[1:]))
                #print(dict_magnitudes_valores)
                #print(dict_magnitudes_valores['HORA'])
                valor_hora = dict_magnitudes_valores['HORA']
                valor_corriente = dict_magnitudes_valores['CORRIENTE']
                valor_voltaje = dict_magnitudes_valores['VOLTAJE']
                valor_potencia_kw = dict_magnitudes_valores['POTENCIA_KW']
                valor_frecuencia = dict_magnitudes_valores['FRECUENCIA']
                valor_potencia = dict_magnitudes_valores['POTENCIA']
                valor_velocidad = dict_magnitudes_valores['VELOCIDAD']
                valor_temperatura = dict_magnitudes_valores['TEMPERATURA']
                valor_nivel = dict_magnitudes_valores['NIVEL']
                valor_presion = dict_magnitudes_valores['PRESION']
                valor_caudal = dict_magnitudes_valores['CAUDAL']
                valor_acumulado = dict_magnitudes_valores['ACUMULADO']

                cursor = connection.cursor()

                sql_update_query = """Update demohmi_valores set valor = %s where id = %s"""
                records_to_update = [(valor_hora, 1), (valor_corriente, 2), (valor_voltaje, 3), (valor_potencia_kw, 4)
                , (valor_frecuencia, 5), (valor_potencia, 6), (valor_velocidad, 7)
                , (valor_temperatura, 8), (valor_nivel, 9), (valor_presion, 10), (valor_caudal, 11), (valor_acumulado, 12)]
                cursor.executemany(sql_update_query, records_to_update)

                #sql = "UPDATE demohmi_valores SET valor = '{0}' WHERE parametros = 'voltaje'".format(valor)
                #cursor.execute(sql)
                connection.commit()
                #sleep(1)

                #await self.send(json.dumps({magnitudes : valor_hora}))
                await self.send(json.dumps(dict_magnitudes_valores))
                
            except:
                print("no hay datos")
                #await sleep(1)
            magnitudes.clear()
            valores.clear()
            await sleep(0.05)