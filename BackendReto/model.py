from datetime import datetime
import tzlocal
import conexion
import mysql.connector


def getIsAnswered(data):
        isResponse = 0
        isNotResponse = 0
        for value in data.get("items"):
                if value.get("is_answered"):
                        isResponse += 1
                elif not value.get("is_answered"):
                        isNotResponse += 1
        return {"Answered": isResponse,
                "NotAnswered": isNotResponse}

def getMoreOwners(data):
        maxValue = 0
        lista = []
        for value in data.get("items"):
                lista.append(value.get("owner").get("reputation")) 
                maxValue = max(lista)
                if value.get("owner").get("reputation") == maxValue:
                        respuesta = value        
        return {
                "La respuesta con mayor owners es":respuesta,
                "Con un total de ": f"{maxValue} de owners"
        }

def getLessCountView(data):
        minValue = 0
        lista = []
        for value in data.get("items"):
                lista.append(value.get("view_count"))
                minValue = min(lista)
                if value.get("view_count") == minValue:
                        respuesta = value   
        return {
                "La respuesta con menos vistas es ":respuesta,
                "Con un total de vistas de ":minValue
        }


def getMinAndMaxDate(data):
        lista = []
        for value in data.get("items"):
                fechaUnix = float(value.get("creation_date"))
                local_timezone = tzlocal.get_localzone() 
                fechaLegible = datetime.fromtimestamp(fechaUnix, local_timezone)
                lista.append(fechaLegible)
                minDate = min(lista)
                maxDate = max(lista)
                if fechaLegible == minDate:
                        respuesta1 = value  
                if fechaLegible == maxDate:
                        respuesta2 = value
        return {
                "La respuesta con la fecha más antigua es ":respuesta1,
                "La fecha más antigua es ":minDate,
                "La respuesta con la fecha más reciente es ":respuesta2,
                "La fecha más reciente es ":maxDate
        } 

def getNameAerportMaxMove(data):
        cursor1=data.cursor()
        cursor1.execute("SELECT a.NOMBRE_AEROLINEA AS AEROPUERTO, count(*) AS total from vuelos v inner join aeropuertos a ON v.ID_AEROPUERTO=a.ID_AEROPUERTO GROUP by v.ID_AEROPUERTO ORDER by total DESC LIMIT 1;")
        base = cursor1.fetchall()
        return {"El aeropuerto con mayor numero de movimientos es: ": base}
        data.close()

def getNameAirlineMaxMove(data):
        cursor1=data.cursor()
        cursor1.execute("SELECT a.NOMBRE_AEROLINEA AS AEROLINEA, count(*)AS total from vuelos v inner join aerolineas a ON v.ID_AEROLINEA=a.ID_AEROLINEAS GROUP by v.ID_AEROLINEA ORDER by total DESC LIMIT 1;")
        base = cursor1.fetchall()
        return {"La aerolinea con mayor numero de movimientos es: ": base}
        data.close()

def getDayMaxFly(data):
        cursor1=data.cursor()
        cursor1.execute("select DAY(DIA) AS DIA, count(*) AS total from vuelos group by  DIA ORDER BY total DESC LIMIT 1;")
        base = cursor1.fetchall()
        return {"El día con mayor numero de vuelos es: ": base}
        data.close() 

def getAirlineMoreThanTwo(data):
        cursor1 = data.cursor()
        cursor1.execute("SELECT a.ID_AEROLINEAS AS AEROLINEA, count(*) AS TOTAL from vuelos v inner join aerolineas a ON v.ID_AEROLINEA=a.ID_AEROLINEAS group by v.ID_AEROLINEA HAVING COUNT(DAY(DIA)) > 2 ORDER BY DATE('2021-05-02');")
        base = cursor1.fetchall()
        return {"Las aeroineas que tienen más de  dos vuelos son: ": base}
        data.close() 
