from faker import Faker
import SQL
from time import time 
from random import random, choice, randint

from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


database=SQL.SQLMAGIC()
"""
CREATE TABLE GPS'S
            id_auto interger referenes AUTOS(id_auto),
            fecha varchar(100),
            hora varchar(100),
            latitud integer, 
            longitud integer,
            PRIMARY KEY(id_auto, fecha, hora);
"""

fake = Faker()
tiempo = time()

print("GPS'S")
print("insert into choques (id_auto, fecha, hora, latitud, longitud) values")

x = 0
while (x<10):
    print("({},'{}','{}','{}','{}'),".format(x,fake.date(),fake.time(), randint(-53000000,-18000000), randint(-73000000,-68000000)))
    x = x + 1
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)
