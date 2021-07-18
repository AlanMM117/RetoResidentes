CREATE DATABASE VuelosMexico;
use VuelosMexico;

CREATE TABLE aerolineas (ID_AEROLINEAS INT NOT NULL AUTO_INCREMENT UNIQUE, 
NOMBRE_AEROLINEA VARCHAR(45) NOT NULL, PRIMARY KEY(ID_AEROLINEAS) );

INSERT INTO aerolineas (NOMBRE_AEROLINEA)VALUES ('Volaris');
INSERT INTO aerolineas (NOMBRE_AEROLINEA)VALUES ('Aeromar');
INSERT INTO aerolineas (NOMBRE_AEROLINEA)VALUES ('Interjet');
INSERT INTO aerolineas (NOMBRE_AEROLINEA)VALUES ('Aeromexico');

SELECT * FROM aerolineas;

CREATE TABLE aeropuertos (ID_AEROPUERTO INT NOT NULL AUTO_INCREMENT UNIQUE,
 NOMBRE_AEROLINEA VARCHAR(45), PRIMARY KEY (ID_AEROPUERTO) );
 
 INSERT INTO aeropuertos (NOMBRE_AEROLINEA)VALUES('Benito Juarez');
 INSERT INTO aeropuertos (NOMBRE_AEROLINEA)VALUES('Guanajuato');
 INSERT INTO aeropuertos (NOMBRE_AEROLINEA)VALUES('La Paz');
 INSERT INTO aeropuertos (NOMBRE_AEROLINEA)VALUES('Oaxaca');
 
 SELECT * FROM aeropuertos;
 
 
 CREATE TABLE movimientos (ID_MOVIMIENTO INT NOT NULL AUTO_INCREMENT UNIQUE, 
 DESCRIPCION VARCHAR(45), PRIMARY KEY (ID_MOVIMIENTO)); 
 
 INSERT INTO movimientos (DESCRIPCION) VALUES ('Salida');
 INSERT INTO movimientos (DESCRIPCION) VALUES ('Llegada');
 
 SELECT * FROM movimientos;
 
 
 CREATE TABLE vuelos 
 (ID_AEROLINEA INT, 
 ID_AEROPUERTO INT, 
 ID_MOVIMIENTO INT,
 DIA DATE NOT NULL,
 CONSTRAINT FK_AEROLINEA FOREIGN KEY (ID_AEROLINEA) REFERENCES aerolineas(ID_AEROLINEAS),
 CONSTRAINT FK_AEROPUERTO FOREIGN KEY (ID_AEROPUERTO) REFERENCES aeropuertos(ID_AEROPUERTO),
 CONSTRAINT FK_MOVIMIENTO FOREIGN KEY (ID_MOVIMIENTO) REFERENCES movimientos(ID_MOVIMIENTO));
 
 INSERT INTO vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, DIA) VALUES 
 (1,1,1,'2021-05-02'),
 (2,1,1,'2021-05-02'),
 (3,2,2,'2021-05-02'),
 (4,3,2,'2021-05-02'),
 (1,3,2,'2021-05-02'),
 (2,1,1,'2021-05-02'),
 (2,3,1,'2021-05-04'),
 (3,4,1,'2021-05-04'),
 (3,4,1,'2021-05-04');
 
select * from vuelos;

/*1. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?*/
SELECT a.NOMBRE_AEROLINEA AS AEROPUERTO, count(*) AS total from vuelos v inner join aeropuertos a ON v.ID_AEROPUERTO=a.ID_AEROPUERTO GROUP by v.ID_AEROPUERTO ORDER by total DESC LIMIT 1;
/*2. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año?*/
SELECT a.NOMBRE_AEROLINEA AS AEROLINEA, count(*)AS total from vuelos v inner join aerolineas a ON v.ID_AEROLINEA=a.ID_AEROLINEAS GROUP by v.ID_AEROLINEA ORDER by total DESC LIMIT 1;
/*3. ¿En qué día se han tenido mayor número de vuelos?*/
select DAY(DIA) AS DIA, count(*) AS total from vuelos group by  DIA ORDER BY total DESC LIMIT 1;
/*4. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?*/
SELECT a.ID_AEROLINEAS AS AEROLINEA, count(*) AS TOTAL from vuelos v inner join aerolineas a ON v.ID_AEROLINEA=a.ID_AEROLINEAS group by v.ID_AEROLINEA HAVING COUNT(DAY(DIA)) > 2 ORDER BY DATE('2021-05-02');

