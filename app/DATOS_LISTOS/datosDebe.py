from faker import Faker
from time import time 

fake = Faker()
print("DEBE")
print("insert into choques (id_usuario,id_penalizacion) values")

for x in range(0,10):
    for y in range(0,10):
        print("({},{}),".format(x,y))
print(")")