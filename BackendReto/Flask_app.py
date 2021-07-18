from flask import Flask, request, jsonify
import model
import conexion
import mysql.connector

app = Flask(__name__)

@app.route("/get-Is-Answered-get", methods=["GET"])
def getIsAnsweredGet():
    con = conexion.conexionJson()
    response = model.getIsAnswered(con)
    return jsonify(response)

@app.route("/get-More-Owners-get", methods=["GET"])
def getMoreOwnersget():
    con = conexion.conexionJson()
    response = model.getMoreOwners(con)
    return jsonify(response)

@app.route("/get-Less-Count-View-get", methods=["GET"])
def getLessCountViewget():
    con = conexion.conexionJson()
    response = model.getLessCountView(con)
    return jsonify(response)

@app.route("/get-Min-And-Max-Date-get", methods=["GET"])
def getMinAndMaxDateget():
    con = conexion.conexionJson()
    response = model.getMinAndMaxDate(con)
    return jsonify(response)  

@app.route("/get-Name-Airport-Max-Move-get", methods=["GET"])
def getNameAirportMaxMoveget():
    con = conexion.conexionMySQL()
    response = model.getNameAerportMaxMove(con)
    return jsonify(response) 

@app.route("/get-Name-Airline-Max-Move-get", methods=["GET"])
def getNameAirlineMaxMoveget():
    con = conexion.conexionMySQL()
    response = model.getNameAirlineMaxMove(con)
    return jsonify(response)

@app.route("/get-Day-Max-Fly-get", methods=["GET"])
def getDayMaxFlyget():
    con = conexion.conexionMySQL()
    response = model.getDayMaxFly(con)
    return jsonify(response)

@app.route("/get-Airline-More-Than-Two-get", methods=["GET"])
def getAirlineMoreThanTwoget():
    con = conexion.conexionMySQL()
    response = model.getAirlineMoreThanTwo(con)
    return jsonify(response)


if __name__ == '__main__':
   app.run(debug = True)
