from faker import Faker
from time import time
from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()

fake = Faker()

sql="""select rut from clientes;"""
cur.execute(sql)
posts  = cur.fetchall()

sql="""select id_penalizacion from faltas;"""
cur.execute(sql)
posts2  = cur.fetchall()


for x in posts:
    for y in  posts2:
        sql= ("insert into choques (id_usuario,id_penalizacion) values")
<<<<<<< HEAD
        sql = sql + ("({},{});".format(x[0],y[0]))
=======
        sql = sql + ("({},{})".format(x[0],y[0]))
>>>>>>> 6bb6178b212bca745457a5bd0b725e917379b076


conn.commit()
cur.close()
conn.close()
