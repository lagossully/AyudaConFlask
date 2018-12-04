from faker import Faker
from time import time
import SQL

fake = Faker()
tiempo = time()

x = 1
print("CLIENTES")
print("insert into choques (id_usuario, nombre, apellido, direccion, correo, celular, foto, fecha_nacimiento) values")

"""
CREATE TABLE CLIENTES
           (RUT integer PRIMARY KEY,
           digito varchar(1),
           nombre varchar(40),
           apellido varchar(40),
           email varchar(100),
           telefono varchar(10), 
           creado timestamp);
"""


for x in range(0,10):
    y = fake.name()
   comando="({},'{}','{}','{}','{}','{}','{}','{}'),".format(x,
   y.split()[0],
   y.split()[1],
   fake.address(), 
   fake.email(),
   fake.phone_number(),
   fake.url(),
   fake.date())
print(")")

final = time()- tiempo
print "Tiempo total en crearse todos los datos es" , final










