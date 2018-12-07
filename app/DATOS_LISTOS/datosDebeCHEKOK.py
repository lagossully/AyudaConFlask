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
<<<<<<< HEAD
        sql= ("insert into debe (id_usuario,id_penalizacion) values")
        sql = sql + ("({},{});".format(x[0],y[0]))
        cur.execute(sql)
=======
        sql= """insert INTO debe VALUES"""
        sql = sql + ("({},{});".format(x[0],y[0]))
        cur.execute(sql)
        
>>>>>>> 0f032a3abe51812695f4c12e109f35925c6ed8ba


conn.commit()
cur.close()
conn.close()
