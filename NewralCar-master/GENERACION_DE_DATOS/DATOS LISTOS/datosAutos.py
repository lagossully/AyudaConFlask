from faker import Faker
from time import time
from random import random, choice, randint
import SQL
from configuraciones import *
import psycopg2

database=SQL.SQLMAGIC()
"""
CREATE TABLE AUTOS
           (PATENTE varchar(6) PRIMARY KEY,
            rut integer references clientes(rut),
            largo integer, 
            ancho integer, 
            alto integer, 
            peso_neto integer,
            tipo_combustible varchar, 
            tipo_auto varchar, 
            maximo_pasajeros integer,
            num_aro varchar, 
            creado timestamp);
"""

fake = Faker()
tiempo = time()
combustible = ["gasolina98", "gasolina95", "gasolina93", "Diesel"]
tautos = ["Sedan", "Station Wagon", "Doble Cabina", "Hatchback","SUV", "Furgon"]

print("AUTOS")
print("insert into autos (id_auto, largo, ancho, alto, peso_neto, peso_max, tipo_combustible, tipo_auto, cant_pasajero, numeroAro) values")

for x in range(0,10):
    peso_neto = randint(2700, 3860)
    "({},'{}[mm]' ,'{}[mm]','{}[mm]','{}[mm]', '{}[mm]','{}','{}','{}' pasajeros, '{}' ),".format(x,
    randint(3500, 5000),
    randint(1700, 1900), 
    randint(1300, 1800),,
    peso_neto + randint(500, 1000), 
    choice(combustible), 
    choice(tautos), 
    choice([2,4,6]), 
    choice(['Aro 24','Aro 26','Aro 28']))


print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)

