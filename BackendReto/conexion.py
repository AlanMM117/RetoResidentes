import requests
import json
import mysql.connector


def conexionJson():
    body = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = json.loads(body.text)
    return (data)

def conexionMySQL():
    conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",database="vuelosmexico")
    return (conexion1)