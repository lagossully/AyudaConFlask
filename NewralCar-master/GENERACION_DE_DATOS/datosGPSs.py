from faker import Faker
from time import time 
from random import random, choice, randint

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
