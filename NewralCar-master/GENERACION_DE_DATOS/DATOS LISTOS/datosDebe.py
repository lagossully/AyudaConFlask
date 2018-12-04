from faker import Faker
from time import time
import SQL

fake = Faker()
tiempo = time()
print("DEBE")
print("insert into choques (id_usuario,id_penalizacion, comentario) values")

database=SQL.SQLMAGIC()
"""
CREATE TABLE DEBE
            (RUT integer references CLIENTES(RUT),
            id_penalizacion integer references FALTAS(id_penalizacion),
            creado timestamp);
"""

for x in range(0,10):
    for y in range(0,10):
        print("({},'{}','{}'),".format(x,y,fake.text()))
print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)