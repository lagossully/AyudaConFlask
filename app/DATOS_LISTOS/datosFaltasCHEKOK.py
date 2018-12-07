from faker import Faker
from time import time
from random import choice, random, randint
from configuraciones import *
from datetime import datetime, timedelta
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql="""select fecha from choques;"""

cur.execute(sql)
posts  = cur.fetchall()

fechasChoques = []
for x in posts:
    fechasChoques.append(x[1])

fake = Faker()

for x in range(0,10):
    fechaIncidente = choice(fechasChoques)
    fechaPago = fake.date()
    while fechaIncidente > fechaPago:
        fechaPago = fake.date()

    sql="""insert into choques (id_penalizacion, monto, fecha_incidente, fecha_vencimiento) values"""
    sql = sql + ("({},{},'{}','{}','{}'),".format(x,
    randint(40000,300000),
    fake.text(),
    fechaIncidente,
    fechaPago))
    cur.execute(sql)

conn.commit()
cur.close()
conn.close()