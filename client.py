import rpyc
from const import *

conn = rpyc.connect(SERVER, port = PORT)

print("Escreva dois numeros:")

a = float(input())

b = float(input())

print (a, '+', b, '=', conn.root.exposed_add(a,b))

print (a, '-', b, '=', conn.root.exposed_subtract(a,b))

print (a, '*', b, '=', conn.root.exposed_multiply(a,b))

print (a, '/', b, '=', conn.root.exposed_divide(a,b))