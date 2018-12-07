from random import choice
from faker import Faker
import time
from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()



fake = Faker()
sql="""select patente from autos;"""
cur.execute(sql)
posts  = cur.fetchall()

sql="""select id_evento from choques;"""
cur.execute(sql)
posts2  = cur.fetchall()




for x in posts:
    for y in posts2:
        sql = ("insert into involucrados (id_evento,patente,pasajeros_afectados) values ")
        sql = sql + ("({},'{}',{}),".format(x[0],y[0],choice([1,2,3,4,5,6])))
        cur.execute(sql)

conn.commit()
cur.close()
conn.close()
