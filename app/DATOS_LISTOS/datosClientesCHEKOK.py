from faker import Faker
from time import time 
import random
from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()




fake = Faker()
tiempo = time()

list1=[1000000,2000000,3000000,5000000,6000000,10000000, 9000000]
list2=[10000,20000,30000,60000,0,200, 100500,20302,212121,343434, random.randrange(1111,99999,100)]
list3=['1','2','3','6','8','k','0']

list5=[]
for x in range(0,10):       
    y = fake.name()
    sql="""insert into clientes (rut,digito,nombre,apellido,email,telefono,direccion) values """
    rut=9020677+random.choice(list1)+random.choice(list2)+x*100
    
    sql=sql+("({},'{}','{}','{}','{}','{}','{}');".format(rut,
    (random.choice(list3)),
    (y.split()[0]),
    (y.split()[1]),
    (fake.email()),
    (fake.phone_number()),
    (fake.address()),
    (int(random.choice(range(18,70))))))
    #print(sql)
    if rut in list5:
        
        x=x-1
    else:
        list5.append(rut)
        cur.execute(sql)

        

conn.commit()
cur.close()
conn.close()
